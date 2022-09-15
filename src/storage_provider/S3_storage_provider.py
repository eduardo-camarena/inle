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

  def get_image(self, file_name: str) -> str:
    local_file_name = file_name.split('/')[1]
    self.client.download_file(
      Bucket=CONFIG['aws']['bucket'],
      Key=file_name,
      Filename=local_file_name
    )
    return local_file_name

  def list_available_images(self):
    response = self.client.list_objects(
      Bucket=CONFIG['aws']['bucket'],
      Prefix=CONFIG['aws']['hourly_folder']
    ).get('Contents', [])

    return [val['Key'] for val in response]
