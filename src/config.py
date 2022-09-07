# python packages
import os

# pypi packages
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
  'twitter': {
    'api_key': os.getenv('TWITTER_API_KEY'),
    'api_secret': os.getenv('TWITTER_API_SECRET'),
    'api_access_token': os.getenv('TWITTER_ACCESS_TOKEN'),
    'api_token_secret': os.getenv('TWITTER_TOKEN_SECRET'),
  },
  'aws': {
    'access_key_id': os.getenv('AWS_ACCESS_KEY_ID'),
    'secret_key': os.getenv('AWS_SECRET_KEY'),
    'bucket': os.getenv('AWS_BUCKET')
  }
}