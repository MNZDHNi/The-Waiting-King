from . import color
from .picture_class import Layer, Picture

layer1 = Layer(
    ["1.This is a sample text1.", "2.This is a sample text2."],
    color.Color.RED,
)

layer2 = Layer(
    ["1.This is", "2.This is"],
    color.Color.GREEN,
)

picture1 = Picture()
picture1.add_layer(layer1)
picture1.add_layer(layer2)
