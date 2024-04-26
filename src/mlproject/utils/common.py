import os
from box.exception import BoxValueError
import yaml
from src.mlproject import logger
import json
import joblib
from ensure import ensure_annotation
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotation
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml(str): path like input

    Raises:
        ValueError: if yaml is empty
        e:empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        return e


@ensure_annotation
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories(list): list of path of directories
        ignore_log (bool,optional):ignore if multiple dirs is to be create Defauts to False
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotation
def save_json(path: Path, data: dict):
    """save json files data

    Args:
        path(Path): path to json file
        data(dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at {path}")


@ensure_annotation
def load_json(path: Path) -> ConfigBox:
    """save json files data

    Args: path(Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.infor(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotation
def save_bin(data: Any, path: Path):
    """Save binary file

    Args:
        data(any) : data to be saved as binary file
        path(Path) : path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotation
def load_bin(path: Path) -> Any:
    """load binary file

    Args:
        path(Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotation
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"
