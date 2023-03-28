import pytest

from app.configuration.configuration import Configuration
from app.utils.exceptions import ConfigNotInitializedException


async def test_configuration_throws_exception_when_we_try_to_get_config_attributes_before_vales_are_initialized():
    with pytest.raises(ConfigNotInitializedException):
        Configuration.get_db_connection_info()