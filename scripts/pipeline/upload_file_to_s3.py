import boto3
import sys

def main():

    print (sys.argv)
    bucket_name=sys.argv[1]
    public_aws_key=sys.argv[2]
    clinical_aws_key=sys.argv[3]
    aws_access_key=sys.argv[4]
    aws_access_secret=sys.argv[5]
    public_local_path=sys.argv[6]
    clinical_local_path=sys.argv[7]


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

    s3.meta.client.upload_file(public_local_path, bucket_name, public_aws_key)
    print (public_aws_key, ' done')
    s3.meta.client.upload_file(clinical_local_path, bucket_name, clinical_aws_key)
    print (clinical_aws_key,' done')

    print ('Done uploading')


main()