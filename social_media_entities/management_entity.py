from typing import Self, Type, TypeVar

from social_media_entities.abc import SocialMediaEntity
from social_media_entities.exceptions import EntityTypeException


# Исключение нет сущностей данного класса
# Исключение нет сущностей данного класса при изъятии значения. Не должно быть пустого списка

SocialMediaEntityType = TypeVar("SocialMediaEntityType", bound="SocialMediaEntity")


class EntityController:
    """ """

    def __init__(self) -> None:
        self.__entity_storage: dict[str, list[SocialMediaEntity]] = {}

    @staticmethod
    def update_sequence_entity(
        sequence_entity: list[SocialMediaEntity], social_media_entity: SocialMediaEntity
    ) -> list[SocialMediaEntity]:
        print(sequence_entity)
        sequence_entity = [social_media_entity] + sequence_entity
        print(sequence_entity)
        return sequence_entity

    def add_entity(self, social_media_entity: SocialMediaEntity) -> Self:
        if not isinstance(social_media_entity, SocialMediaEntity):
            raise EntityTypeException(social_media_entity)
        sequence_entity = self.__entity_storage.get(
            social_media_entity.__class__.__name__
        )
        if not sequence_entity:
            self.__entity_storage[social_media_entity.__class__.__name__] = [
                social_media_entity
            ]
        else:
            sequence_entity = self.__entity_storage.get(
                social_media_entity.__class__.__name__
            )
            self.update_sequence_entity(sequence_entity, social_media_entity)
            self.__entity_storage[social_media_entity.__class__.__name__] = (
                self.update_sequence_entity(sequence_entity, social_media_entity)
            )
        return self

    def get_entity(
        self, social_media_type: Type[SocialMediaEntityType]
    ) -> SocialMediaEntityType:
        sequence_entity = self.__entity_storage.get(social_media_type.__name__)
        social_media_entity = sequence_entity.pop()
        self.__entity_storage[social_media_type.__name__] = sequence_entity
        return social_media_entity


test_1 = TestSocialMediaEntity(test_str="test_1", status=True)
test_2 = TestSocialMediaEntity(test_str="test_2", status=True)
test_3 = TestSocialMediaEntity(test_str="test_3", status=True)
print(test_1)

entity_controller = EntityController()
entity_controller3 = entity_controller.add_entity(test_1)
print(entity_controller3)
entity_controller.add_entity(test_2)
print(entity_controller3)
print(entity_controller.add_entity(test_2))
print(entity_controller.get_entity(TestSocialMediaEntity))
data = entity_controller.get_entity(TestSocialMediaEntity)
print(data)
print(entity_controller3)

entity_controller2 = EntityController()

entity_controller2.add_entity(test_3)
