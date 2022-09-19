from typing import IO, List
from io import BytesIO

import boto3

from storage_provider.storage_provider_interface import StorageProvider
from config import CONFIG

class S3StorageProvider(StorageProvider):
  def __init__(self):
    self.client = boto3.client(
      's3',
      aws_access_key_id=CONFIG['aws']['access_key_id'],
      aws_secret_access_key=CONFIG['aws']['secret_key']
    )

  def get_image(self, file_name: str) -> IO:
    img = self.client.get_object(
      Bucket=CONFIG['aws']['bucket'],
      Key=file_name
    )
    return BytesIO(img['Body'].read())

  def list_available_images(self) -> List[str]:
    response = self.client.list_objects(
      Bucket=CONFIG['aws']['bucket'],
      Prefix=CONFIG['aws']['hourly_folder']
    ).get('Contents', [])

    return [val['Key'] for val in response]
