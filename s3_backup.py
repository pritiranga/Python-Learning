# Script to take a backup from local to AWS S3
# boto3 is used to do AWS tasks using Python

import boto3  # if not exists, install using "pip install boto3"

s3=boto3.resource("s3")

def upload_backup(s3, file_name, bucket_name, key_name):  # backup should be uploaded on "s3", "file_name" of the file of which backup should be taken, "bucket_name" where backup will be uploaded, "key_name" will be the new name of backup that should be written on s3
    data=open(file_name, 'rb')  # rb means read binary
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded successfully")

bucket_name="pythonfordevops"
region="eu-north-1"

file_name="C:\\Users\\Priti Ranga\\Documents\\Python Workshop\\backups\\backup_2024-09-03.tar.gz"
upload_backup(s3, file_name, bucket_name, "my-first-backup.tar.gz")