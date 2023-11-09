import boto3
import os
from dotenv import load_dotenv

load_dotenv()

region = os.getenv('AWS_REGION')

dynamodb = boto3.resource('dynamodb', region_name=region)
table = dynamodb.Table('product')

