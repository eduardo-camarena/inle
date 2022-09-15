# python packages
import os
import json
import sqlite3

# pypi packages
import tweepy

# local
from config import CONFIG
from storage_provider.S3_storage_provider import S3StorageProvider
# from storage_provider.local_storage_provider import LocalStorageProvider
from database import add_entities, get_random_image

def get_twitter_api() -> tweepy.API:
  auth = tweepy.OAuth1UserHandler(
    CONFIG['twitter']['api_key'],
    CONFIG['twitter']['api_secret'],
    CONFIG['twitter']['api_access_token'],
    CONFIG['twitter']['api_token_secret']
  )

  return tweepy.API(auth)

if __name__ == '__main__':
  connection = sqlite3.connect('hourly_bot.db')
  cursor = connection.cursor()

  table = cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='hourly_bot'"
  );

  if (table.fetchall() == []):
    cursor.execute(
      """CREATE TABLE hourly_bot(
        file_name TEXT UNIQUE,
        used TINYINT DEFAULT 0
        )"""
    )

  # api = get_twitter_api()
  # tweets = api.home_timeline(count=1)

  storageProvider = S3StorageProvider()
  # storageProvider = LocalStorageProvider()
  # available_images = storageProvider.list_available_images()
  # add_entities(connection, available_images)
  print(get_random_image(connection))

  connection.close()
