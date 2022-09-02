from typing import Any, Generator

class DockerContainer():
  def __init__(self, defaultContainer: Any) -> None:
    self.container = defaultContainer

  def logs(self) -> Generator:
    return self.container.logs(stream=True)

  def stop(self) -> None:
    self.container.stop()

  def remove(self) -> None:
    self.container.remove()
