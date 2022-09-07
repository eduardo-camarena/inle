from abc import ABC, abstractmethod

class StorageProvider(ABC):
  @abstractmethod
  def get_image(self, file_name: str):
    pass
