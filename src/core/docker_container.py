from dataclasses import dataclass

from docker import DockerClient
from docker.models.containers import Container


@dataclass
class DockerContainer:
    id: str
    name: str
    status: str
    image: str
    started_at: str

    # Used to create a factory filled class
    @classmethod
    def factory(cls, container: Container) -> 'DockerContainer':

        # Container Attributes
        attrs = container.attrs

        return cls(
            id=container.short_id,  # Used to stop containers
            name=container.name or "Unnamed",
            status=container.status,
            image=attrs["Config"]["Image"],
            started_at=attrs["State"]["StartedAt"]
        )

    def update_status(self, client: DockerClient):
        self.status = client.containers.get(self.id).status
