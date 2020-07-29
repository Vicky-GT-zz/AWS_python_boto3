import boto3

s3_object=boto3.resource('s3',  aws_access_key_id=access_key, aws_secret_access_key=secret_key)

for each_b in s3_object.buckets.all():
        print each_b.name
