import logging
from configparser import ConfigParser

from app.utils.exceptions import ConfigNotInitializedException
from app.utils.singleton import Singleton


class Configuration(metaclass=Singleton):
    _config: ConfigParser | None = None
    logger = logging.getLogger()

    #TODO: Use os libary to order to support both Docker and local setup
    CONFIG_FILE_PATHS = ['../config.ini', 'config.ini']

    @classmethod
    def init(cls):
        cls._load_config()
        cls._init_logging_config()

    @classmethod
    def _load_config(cls) -> None:
        config = ConfigParser()
        config.read(cls.CONFIG_FILE_PATHS)
        cls._config = config

    @classmethod
    def _init_logging_config(cls):
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter(
            "[%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d] %(message)s")
        file_handler.setFormatter(formatter)

        cls.logger.addHandler(file_handler)
        cls.logger.setLevel(logging.DEBUG)

    @classmethod
    def get_db_connection_info(cls):
        if cls._config is None:
            cls.logger.error("Configuration properties accessed before initialization")
            raise ConfigNotInitializedException
        db_conn_info = cls._config['db']
        return db_conn_info['database'], db_conn_info['host'], db_conn_info['user'], db_conn_info['password']


