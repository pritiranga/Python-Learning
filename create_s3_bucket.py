import boto3

s3=boto3.resource("s3")

# Function to create s3 bucket
def create_bucket(s3, bucket_name, region):
    s3.create_bucket(Bucket=bucket_name, 
                     CreateBucketConfiguration={
                         'LocationConstraint':region,
                        },)
    print("Bucket created successfully")

# Function to show all existed buckets 
def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

bucket_name="pythonfordevops787"
region="eu-north-1"

create_bucket(s3, bucket_name, region)
show_buckets(s3)