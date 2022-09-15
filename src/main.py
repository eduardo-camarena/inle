# python packages
import os
import json
import sqlite3
from time import sleep

# pypi packages
import schedule
import tweepy

# local
from config import CONFIG
from storage_provider.S3_storage_provider import S3StorageProvider
from storage_provider.storage_provider_interface import StorageProvider
from database import add_entities, get_random_image

connection = sqlite3.connect('hourly_bot.db')
cursor = connection.cursor()

def get_twitter_api() -> tweepy.API:
  auth = tweepy.OAuth1UserHandler(
    CONFIG['twitter']['api_key'],
    CONFIG['twitter']['api_secret'],
    CONFIG['twitter']['api_access_token'],
    CONFIG['twitter']['api_token_secret']
  )

  return tweepy.API(auth)

def post_to_twitter(api: tweepy.API, storageProvider: StorageProvider) -> None:
  storage_provider_file_name = get_random_image(connection)
  file_name = storageProvider.get_image(storage_provider_file_name)

  api.media_upload(file_name)
  api.update_status(status='', media_ids=['asd'])
  os.remove(f'./{file_name}')

def update_database(storageProvider: StorageProvider) -> None:
  available_images = storageProvider.list_available_images()
  add_entities(connection, available_images)
  print(get_random_image(connection))

if __name__ == '__main__':
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

  api = get_twitter_api()

  storageProvider = S3StorageProvider()

  schedule.every().hour.do(post_to_twitter, api=api, storageProvider=storageProvider)
  schedule.every(24).hour.do(update_database, storageProvider=storageProvider)

  while True:
    schedule.run_pending()
    sleep(1)
