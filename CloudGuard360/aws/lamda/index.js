const AWS = require('aws-sdk');
const s3 = new AWS.S3();

const S3_BUCKET = 'cloudguard360-usage-logs'; // Replace with your actual log bucket

exports.handler = async (event, context) => {
  const usageData = [];

  try {
    const bucketsList = await s3.listBuckets().promise();

    for (const bucket of bucketsList.Buckets) {
      const name = bucket.Name;
      let size = 0;
      let count = 0;

      try {
        const objects = await s3.listObjectsV2({ Bucket: name }).promise();
        if (objects.Contents) {
          for (const obj of objects.Contents) {
            size += obj.Size;
            count += 1;
          }
        }
      } catch (err) {
        continue;
      }

      usageData.push({
        BucketName: name,
        ObjectCount: count,
        TotalSizeGB: +(size / (1024 ** 3)).toFixed(2)
      });
    }

    const timestamp = new Date().toISOString().split('T')[0];
    const filename = `s3-usage-${timestamp}.json`;

    await s3.putObject({
      Bucket: S3_BUCKET,
      Key: filename,
      Body: JSON.stringify(usageData),
      ContentType: 'application/json'
    }).promise();

    return { saved_to_s3: filename, bucket_count: usageData.length };

  } catch (error) {
    console.error('Error:', error);
    return { error: 'Failed to generate usage report' };
  }
};
