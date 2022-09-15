from fileinput import filename
import sqlite3
from typing import List

def add_entities(connection: sqlite3.Connection, files_to_add: List[str]) -> None:
  cursor = connection.cursor()
  file_names = cursor.execute('SELECT file_name FROM hourly_bot')
  files_to_add = [f'("{file_name}")' for file_name in files_to_add if file_name not in file_names.fetchall()]

  values = ", ".join(files_to_add)
  cursor.execute(f'INSERT INTO hourly_bot(file_name) VALUES{values}')
  connection.commit()

def get_random_image(connection: sqlite3.Connection) -> str:
  cursor = connection.cursor()
  image = cursor.execute('SELECT file_name FROM hourly_bot WHERE used=0 ORDER BY RANDOM() LIMIT 1')
  return image.fetchone()[0];

def mark_file_as_used(connection: sqlite3.Connection, file_name: str) -> None:
  cursor = connection.cursor()
  cursor.execute(f'UPDATE hourly_bot SET used=1 WHERE file_name={file_name}')
  connection.commit()
