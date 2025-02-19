from dataclasses import dataclass

from docker.models.images import Image


@dataclass
class DockerImage:
    name: str
    size: int
    creation: str

    # Used to create a factory filled class
    @classmethod
    def factory(cls, image: Image) -> 'DockerImage':

        # Image attributes
        attrs = image.attrs

        return cls(
            name=attrs["RepoTags"][0] if attrs["RepoTags"] else "Unknown",
            size=attrs["Size"] if attrs["Size"] else 0,
            creation=attrs["Created"] if attrs["Created"] else "Unknown",
        )
