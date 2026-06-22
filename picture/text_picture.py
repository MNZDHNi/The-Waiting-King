from . import picture_class
from . import color

layer1 = picture_class.Layer(
        ["1.This is a sample text1.",
        "2.This is a sample text2."],
        color.Color.RED
)

layer2 = picture_class.Layer(
        ["1.This is",
         "2.This is"],
        color.Color.GREEN
)

picture1 = picture_class.Picture()
picture1.add_layer(layer1)
picture1.add_layer(layer2)