import logging

import boto3
from flask import Flask
from watchtower import CloudWatchLogHandler

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes


if not app.debug:
    client = boto3.client(
        'logs',
        aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
        region_name=app.config['AWS_REGION_NAME']
    )
    log_group_name = 'arajin-error-log'
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = CloudWatchLogHandler(log_group_name=log_group_name, boto3_client=client)
    logger.addHandler(handler)
