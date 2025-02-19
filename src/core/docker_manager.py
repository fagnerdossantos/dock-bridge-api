from core.local_client import LocalClient
from core.docker_container import DockerContainer
from core.docker_image import DockerImage
from data.cache import Cache


class DockerManager:
    def __init__(self, client: LocalClient, cache: Cache):
        self.client = client.client
        self.cache = cache

    # Return all available images
    def load_images(self) -> list[DockerImage]:

        #
        if not self.cache.images:

            self.cache.images.extend(
                DockerImage.factory(image) for image in self.client.images.list()
            )

        return self.cache.images.copy()

    #! Ensure containers are loaded into cache before performing any container actions.
    #! This is necessary because the cache holds all currently running containers,
    #! and we need to ensure the cache is up-to-date before interacting with the containers.
    # Returns a list of all available containers from the cache, loading them if necessary.

    def load_containers(self) -> list[DockerContainer]:

        # Check if cache is void
        if not self.cache.containers:

            containers = self.client.containers.list()
            for container in containers:
                docker_container = DockerContainer.factory(container)

                # Add in cache
                self.cache.containers[docker_container.id] = docker_container

        return list(self.cache.containers.values())

    def start_container(self, image_name: str) -> DockerContainer:

        #
        container = self.client.containers.run(image_name, detach=True)

        # Fetch the container again by short ID to ensure it is actually running,
        # because the object returned by run() may not contain the most up-to-date data.
        container = self.client.containers.get(container.short_id)

        docker_container = DockerContainer.factory(container)

        self.cache.add_container(docker_container)

        return docker_container

    def stop_container(self, container_id: str) -> bool:

        #
        if container_id not in self.cache.containers:
            return False

        self.client.containers.get(container_id).stop()
        self.cache.remove_container(container_id)

        return True

    # !! NOT TESTED YET
    # Pause a running container
    def pause_container(self, container_id: str) -> bool:

        #
        if container_id not in self.cache.containers:
            return False

        self.client.containers.get(container_id).pause()

        # Update status in cache
        container: DockerContainer = self.cache.containers[container_id]
        container.status = "Paused"

        return True

    # Unpause a running container
    def unpause_container(self, container_id: str):

        #
        if container_id not in self.cache.containers:
            return False

        self.client.containers.get(container_id).unpause()

        # Update status in cache
        container: DockerContainer = self.cache.containers[container_id]
        container.status = "Running"

        return True
