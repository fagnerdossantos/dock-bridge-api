from dataclasses import dataclass

from core.docker_container import DockerContainer
from core.docker_image import DockerImage


from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Cache:
    #
    images: List[DockerImage] = field(default_factory=list)
    containers: Dict[str, DockerContainer] = field(default_factory=dict)

    # Add
    def add_image(self, image: DockerImage):
        self.images.append(image)

    def add_container(self, container: DockerContainer):
        # Add container using ID as Key
        self.containers[container.id] = container

    # Get
    def get_container(self, id: str) -> Optional[DockerContainer]:
        return self.containers.get(id)
    
    # Remove
    def remove_container(self, id: str):
        self.containers.pop(id, None)

    def clear_containers(self):
        self.containers.clear()

    def clear_images(self):
        self.images.clear()
