import datetime
import logging
import boto
from botocore.exceptions import UnknownKeyError

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def job_finder(event, context):
    
