resource "aws_s3_bucket" "prediction_data" {
  bucket = "${var.project_prefix}-ai-data"

  tags = {
    Name        = "Prediction Data Bucket"
    Environment = "dev"
  }
}

resource "aws_iam_role" "billing_lambda_role" {
  name = "${var.project_prefix}-billing-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_policy" "billing_lambda_policy" {
  name        = "${var.project_prefix}-billing-policy"
  description = "Allows access to S3 and Cost Explorer"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = [
          "s3:GetObject",
          "s3:ListBucket"
        ],
        Resource = [
          "arn:aws:s3:::${var.project_prefix}-ai-data",
          "arn:aws:s3:::${var.project_prefix}-ai-data/*"
        ]
      },
      {
        Effect   = "Allow",
        Action   = [
          "ce:GetCostAndUsage"
        ],
        Resource = "*"
      },
      {
        Effect   = "Allow",
        Action   = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "attach_policy" {
  role       = aws_iam_role.billing_lambda_role.name
  policy_arn = aws_iam_policy.billing_lambda_policy.arn
}
resource "aws_lambda_function" "cloud_cost_monitor" {
  function_name = "${var.project_prefix}-cost-monitor"
  role          = aws_iam_role.billing_lambda_role.arn
  handler       = "cloud_cost_monitor.lambda_handler"
  runtime       = "python3.12"

  filename         = "${path.module}/lambda/cloud_cost_monitor.zip"
  source_code_hash = filebase64sha256("${path.module}/lambda/cloud_cost_monitor.zip")

  timeout      = 30
  memory_size  = 128

  environment {
    variables = {
      BUCKET_NAME = "${var.project_prefix}-ai-data"
      FILE_KEY    = "predicted_cost.json"
    }
  }

  tags = {
    Name = "CloudGuard360 Cost Monitor Lambda"
  }
}
