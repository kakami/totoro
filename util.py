import os
import shutil
import importlib.util

CONFIG_FILE = "config.py"
DEFAULT_CONFIG_FILE = "config.default.py"

def ensure_config_exists():
    if not os.path.exists(CONFIG_FILE):
        shutil.copyfile(DEFAULT_CONFIG_FILE, CONFIG_FILE)

def load_config():
    spec = importlib.util.spec_from_file_location("config", CONFIG_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module