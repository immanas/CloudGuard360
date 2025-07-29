provider "aws" {
  region  = var.aws_region
  profile = "default"  # Uses credentials from your local AWS CLI
}
