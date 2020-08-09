import boto3,simplejson,io
def get_cache_item(name,bucket_name,region_name="",endpoint_url="",aws_access_key_id="",aws_secret_access_key=""):
    credentials=boto3.Session().get_credentials()
    if(credentials==None and aws_access_key_id==""):
        raise Exception("Aws credentials must be set or aws_access_key_id must be set when calling get_cache_item function")
    if(credentials==None and aws_secret_access_key=="" ):
        raise Exception("Aws credentials must be set or aws_secret_access_key must be set when calling get_cache_item function")
    if(aws_access_key_id==""):
        aws_access_key_id=credentials.access_key
    if(aws_secret_access_key==""):
        aws_secret_access_key=credentials.secret_key
    try:
        if(region_name=="" or endpoint_url==""):
            result=boto3.client('s3',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key).get_object(Bucket=bucket_name,Key=name)['Body'].read().decode("utf-8")
        else:
            result=boto3.client('s3',region_name=region_name,endpoint_url=endpoint_url,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key).get_object(Bucket=bucket_name,Key=name)['Body'].read().decode("utf-8")
        return simplejson.loads(result)
    except:
        return None


def put_cache_item(name,value,bucket_name,region_name="",endpoint_url="",aws_access_key_id="",aws_secret_access_key=""):
    credentials=boto3.Session().get_credentials()
    if(credentials==None and aws_access_key_id==""):
        raise Exception("Aws credentials must be set or aws_access_key_id must be set when calling put_cache_item function")
    if(credentials==None and aws_secret_access_key=="" ):
        raise Exception("Aws credentials must be set or aws_secret_access_key must be set when calling put_cache_item function")
    if(aws_access_key_id==""):
        aws_access_key_id=credentials.access_key
    if(aws_secret_access_key==""):
        aws_secret_access_key=credentials.secret_key
    if(region_name=="" or endpoint_url==""):
        boto3.client('s3',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key).upload_fileobj(io.BytesIO(bytes(simplejson.dumps(value), 'utf-8')),bucket_name,name)
    else:
        boto3.client('s3',region_name=region_name,endpoint_url=endpoint_url,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key).upload_fileobj(io.BytesIO(bytes(simplejson.dumps(value), 'utf-8')),bucket_name,name)
    return True
