import os
import shutil
import importlib.util
from atomic_int import AtomicInt

CONFIG_FILE = "config.py"
DEFAULT_CONFIG_FILE = "config.default.py"

# 设置几个全局变量
dev = 15
concurrency = 5
output_dir = "/home/iuz/output_15"
counter = AtomicInt(0)

def ensure_config_exists():
    if not os.path.exists(CONFIG_FILE):
        shutil.copyfile(DEFAULT_CONFIG_FILE, CONFIG_FILE)

def load_config():
    spec = importlib.util.spec_from_file_location("config", CONFIG_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
