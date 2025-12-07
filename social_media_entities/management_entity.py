from social_media_entities.abc import SocialMediaEntity
from social_media_entities.exceptions import EntityTypeException
from social_media_entities.social_media_storage import SocialMediaStorage


class EntityController:
    def __init__(self, entity_storage: SocialMediaStorage | None = None):
        self.entity_storage = entity_storage

    def add_entity(self, social_media_entity: SocialMediaEntity) -> bool:
        if not isinstance(social_media_entity, SocialMediaEntity):
            raise EntityTypeException(social_media_entity)

    def get_entity(self, social_media_entity: SocialMediaEntity) -> SocialMediaEntity:
        if not isinstance(social_media_entity, SocialMediaEntity):
            raise EntityTypeException(social_media_entity)


class VirtualEntityStructure:
    pass
