bucket_name=$1
public_aws_key=$2
clinical_aws_key=$3
aws_access_key=$4
aws_access_secret=$5
public_local_path=$6
clinical_local_path=$7

# Remove any existing versions of a ZIP
#rm -rf $local_path

# Create a zip of the current directory.
#zip -r $local_path . -x .git/ .git/*** .github/workflows/release.yml scripts/pipeline/release.sh scripts/pipeline/upload_file_to_s3.py .DS_Store

# Install required dependencies for Python script.
pip3 install boto3

# Run upload script
python3 scripts/pipeline/upload_file_to_s3.py $bucket_name $public_aws_key $clinical_aws_key $aws_access_key $aws_access_secret $public_local_path $clinical_local_path