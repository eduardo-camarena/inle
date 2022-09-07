import boto3

from storage_provider.storage_provider_interface import StorageProvider
from config import CONFIG

class S3StorageProvider(StorageProvider):
  def __init__(self):
    self.session = boto3.client(
      's3',
      aws_access_key_id=CONFIG['aws']['access_key_id'],
      aws_secret_access_key=CONFIG['aws']['secret_key']
    )

  def get_image(self, file_name: str):
    return self.session.get_object(
      Bucket=CONFIG['aws']['bucket'],
      Key=file_name
    )
