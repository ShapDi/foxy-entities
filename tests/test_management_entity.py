import pytest

from social_media_entities.abc import SocialMediaEntity
from social_media_entities.exceptions import EntityTypeException
from social_media_entities.management_entity import EntityController


class TestSocialMediaEntity(SocialMediaEntity):
    test_str: str


@pytest.mark.parametrize("input_value", [1, 0.2, ([1, 4, 5])])
def test_exception_entity_type_add_entity(input_value):
    with pytest.raises(EntityTypeException):
        EntityController().add_entity(input_value)


# append the accumulated fields to the messages for the next request


# Тестовый кейс добавляется 2 элемента . 1 должен быть последний
def test_add_entity_position():
    pass


def test_unique_sequences_objects():
    pass
