import boto3

s3_object=boto3.resource('s3', aws_access_key_id="your access key", aws_secret_access_key=" your secret key")

for each_b in s3_object.buckets.all():
        print each_b.name
