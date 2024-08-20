import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file(r"C:\Users\yuvi\Desktop\party\index.html",'yuvrajsawant.xyz','index.html')