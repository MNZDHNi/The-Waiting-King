import os
from typing import TYPE_CHECKING, Optional

from .color import Color, set_color
from .picture_class import Picture, Layer

if TYPE_CHECKING:
    from config import InitConfig


class GameScreen:
    """屏幕模块，负责管理屏幕的显示和刷新。"""

    def __init__(self, config: "InitConfig") -> None:
        self.config: "InitConfig" = config
        self.width: int = config.width
        self.height: int = config.height
        self._frame: Optional["GameFrame"] = None
        self.flag: bool = False

    def clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def update_frame(self, new_frame: Optional["GameFrame"]) -> None:
        if new_frame is not None:
            self._frame = new_frame

    def refresh(self, mode: int = 0, empty: bool = False) -> None:
        if empty:
            self._frame = GameFrame(self.config)
        elif self._frame is None:
            return

        if mode == 0:
            if not self.flag:
                self.flag = True
                self.clear()
            print("\033[H", end="")  # 将光标移动到屏幕左上角
        elif mode == 1:
            self.clear()
        else:
            raise ValueError("Invalid refresh mode. Use 0 or 1.")

        print("┌", "─" * self.width, "┐", sep="")

        for i in range(self.height):
            print("│", end="")
            for j in range(self.width):
                print(self._frame.picture[i][j], end="")
            print("│")

        print("└", "─" * self.width, "┘", sep="")
        self._frame = None

    def quick_refresh(self, new_frame: "GameFrame") -> None:
        self.update_frame(new_frame)
        self.refresh()

    def empty_refresh(self) -> None:
        self.refresh(empty=True)


class GameFrame:
    """帧模块，负责管理当前帧的内容。"""

    def __init__(self, config: "InitConfig") -> None:
        self.width: int = config.width
        self.height: int = config.height
        self.picture: list[list[str]] = [
            [" " for _ in range(self.width)] for _ in range(self.height)
        ]

    def draw(self, position: tuple[int, int], content: Picture) -> None:
        x, y = position
        if content.length == 0:
            return

        for li in range(content.length):
            layer: Layer = content.layers[li]
            for j in range(len(layer.layer)):
                for k in range(len(layer.layer[j])):
                    if not (0 <= y + j < self.height and 0 <= x + k < self.width):
                        raise ValueError("绘制内容超出屏幕范围")
                    if layer.layer[j][k] is None:
                        self.picture[y + j][x + k] = " "
                        continue
                    if layer.layer[j][k] == " ":
                        continue
                    self.picture[y + j][x + k] = set_color(
                        layer.color, layer.layer[j][k]
                    )
                        

def get_input() -> str:
    """获取用户输入的按键"""
    return input("please input a key: ")