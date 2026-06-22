from typing import Optional

from .color import Color


class Layer:
    def __init__(self, layer: list[str], color: Color) -> None:
        self.layer: list[str] = layer
        self.color: Color = color

    def change_color(self, new_color: Color) -> None:
        self.color = new_color


class Picture:
    def __init__(self) -> None:
        self.layers: list[Layer] = []
        self.length: int = 0

    def add_layer(self, layer: Layer) -> None:
        self.layers.append(layer)
        self.length += 1
