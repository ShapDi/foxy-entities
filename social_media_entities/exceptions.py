from typing import Any


class EntityTypeException(Exception):
    """The value does not correspond to the abc class SocialMediaEntity"""

    def __init__(self, message: Any):
        self.message = (
            f"{message} does not correspond to the abc class SocialMediaEntity"
        )

    def __str__(self):
        return self.message
