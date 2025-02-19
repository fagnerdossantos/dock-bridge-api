import docker
from docker import DockerClient


class LocalClient:
    def __init__(self):
        self.client: DockerClient = docker.client.from_env()
