ec2 = boto3.resource('ec2')

# Code to create EC2 instances in single region
# Region will be selected based on your aws configure options

instances = ec2.create_instances(
     ImageId='',
     MinCount=,
     MaxCount=,
     InstanceType='',
     KeyName=''
 )
