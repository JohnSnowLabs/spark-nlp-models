import boto as boto3
import sys

def main():

    print (sys.argv)
    bucket_name=sys.argv[1]
    clinical_aws_key=sys.argv[2]
    aws_access_key=sys.argv[3]
    aws_access_secret=sys.argv[4]
    clinical_local_path=sys.argv[5]


    '''
    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_access_secret,
    )
    client = session.client('s3')

    response = client.upload_file(
        Filename=local_path,
        Bucket=bucket_name,
        Key=aws_key
    )
    '''

    s3 = boto3.resource('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_access_secret)

    s3.meta.client.upload_file(clinical_local_path, bucket_name, clinical_aws_key)
    print (clinical_aws_key,' done')

    print ('Done uploading')


main()