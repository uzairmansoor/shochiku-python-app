import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME')
    S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
    SAFETENSORS_PATH = os.environ.get('SAFETENSORS_PATH')
    PRETRAINED_MODEL_CACHE_DIR = os.environ.get('PRETRAINED_MODEL_CACHE_DIR')
    SAFETENSORS_FILES_DIR=os.environ.get('SAFETENSORS_FILES_DIR')

	
