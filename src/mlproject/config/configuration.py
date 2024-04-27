from src.mlproject.constants import *
from src.mlproject.utils.common import read_yaml, create_directories
from src.mlproject.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_file_path=CONFIG_FILE_PATH,
        params_file_path=PARAMS_FILE_PATH,
        schema_file_path=SCHAMA_FILE_PATH,
    ):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([self.config.root_dir])

        dataingestionconfig = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_URL,
            local_data_file=local_data_file,
            unzip_dir=unzip_dir,
        )
        return dataingestionconfig
