import uuid

from pydantic import BaseModel


class SocialMediaEntity(BaseModel):
    id: uuid.UUID = uuid.uuid4()
