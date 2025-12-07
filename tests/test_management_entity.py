import pytest

from social_media_entities.exceptions import EntityTypeException
from social_media_entities.management_entity import EntityController


@pytest.mark.parametrize("input_value", [1, 0.2, ([1, 4, 5])])
def test_exception_entity_type_add_entity(input_value):
    with pytest.raises(EntityTypeException):
        EntityController().add_entity(input_value)
