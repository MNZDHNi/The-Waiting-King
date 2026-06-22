"""
素材类
"""
from .color import Color

class Layer:
    def __init__(self, layer, color: Color):
        self.layer = layer
        self.color = color

    def change_color(self, new_color: Color):
        self.color = new_color

class Picture:
    def __init__(self):
        self.layers = []
        self.length = 0
        self.sharp = None

    def init_sharp(self):
        pass

    def add_layer(self, layer: Layer):
        self.layers.append(layer)
        self.length += 1

