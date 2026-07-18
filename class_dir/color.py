from enum import Enum

class Color(Enum):
    """
    黑 红 绿 黄 蓝 紫 青 白
    30 31 32 33 34 35 36 37
    """
    DEFAULT = 0
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

def set_color(color: Color, text: str):
    return f"\033[{color.value}m{text}\033[0m"