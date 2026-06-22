import os
from typing import TYPE_CHECKING, Optional

import picture.color as color
from picture.picture_class import Picture, Layer

if TYPE_CHECKING:
    from config import InitConfig


class GameScreen:
    """屏幕模块，负责管理屏幕的显示和刷新。"""

    def __init__(self, config: "InitConfig") -> None:
        self.width: int = config.width
        self.height: int = config.height
        self._frame: Optional["GameFrame"] = None

    def clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def update_frame(self, new_frame: Optional["GameFrame"]) -> None:
        if new_frame is not None:
            self._frame = new_frame

    def refresh(self) -> None:
        if self._frame is None:
            return

        self.clear()
        print("/", "-" * self.width, "\\", sep="")

        for i in range(self.height):
            print("|", end="")
            for j in range(self.width):
                print(self._frame.picture[i][j], end="")
            print("|")

        print("\\", "-" * self.width, "/", sep="")
        self._frame = None

    def quick_refresh(self, new_frame: "GameFrame") -> None:
        self.update_frame(new_frame)
        self.refresh()


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
                    self.picture[y + j][x + k] = color.set_color(
                        layer.color, layer.layer[j][k]
                    )
                        
