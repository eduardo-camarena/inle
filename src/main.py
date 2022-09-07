# python packages
import os
import json

# pypi packages
import tweepy

# local
from config import CONFIG
from storage_provider.S3_storage_provider import S3StorageProvider
# from storage_provider.local_storage_provider import LocalStorageProvider

def get_twitter_api() -> tweepy.API:
  auth = tweepy.OAuth1UserHandler(
    CONFIG['twitter']['api_key'],
    CONFIG['twitter']['api_secret'],
    CONFIG['twitter']['api_access_token'],
    CONFIG['twitter']['api_token_secret']
  )

  return tweepy.API(auth)

if __name__ == '__main__':
  api = get_twitter_api()
  tweets = api.home_timeline(count=1)

  storageProvider = S3StorageProvider()
  # storageProvider = LocalStorageProvider()
  image = storageProvider.get_image('dami (1).jpg')
  print(image)
