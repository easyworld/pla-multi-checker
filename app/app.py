from enum import Enum
import os
import sys

def get_resource_path(relative_path):
    """
    获取资源文件的路径。根据是否在 PyInstaller 打包环境中，使用不同的路径。
    """
    # 如果是在 PyInstaller 打包后的环境中，使用 _MEIPASS 路径
    if getattr(sys, '_MEIPASS', False):
        base_path = sys._MEIPASS
    else:
        # 否则使用当前工作目录
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

class AppMode(Enum):
    WEB = "WEB"
    LOCAL = "LOCAL"
    DEV = "DEV"
    PACK = "PACK"

_resources = {
    AppMode.WEB: '/home/cappy/pla-multi-checker-web/',
    AppMode.LOCAL: './static/',
    AppMode.DEV: '../static/',
    AppMode.PACK: get_resource_path('static/')
}

APP_MODE = AppMode.LOCAL
RESOURCE_PATH = _resources[APP_MODE]