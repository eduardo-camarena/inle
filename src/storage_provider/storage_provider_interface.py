from abc import ABC, abstractmethod
from typing import List

class StorageProvider(ABC):
  @abstractmethod
  def get_image(self, file_name: str) -> str:
    pass

  @abstractmethod
  def list_available_images(self) -> List[str]:
    pass
