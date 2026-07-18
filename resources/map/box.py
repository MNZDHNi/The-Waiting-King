from class_dir.picture_class import Picture, Layer
from class_dir.color import Color

def get_box(width: int, height: int, color: Color = Color.DEFAULT):
    box = Picture().add_layer_chain(Layer(
        ["┌" + "─" * (width - 2) + "┐"] + \
        ["│" + " " * (width - 2) + "│"] * (height - 2) + \
        ["└" + "─" * (width - 2) + "┘"], color))
    return box

def get_dot_box(width: int, height: int, color: Color = Color.DEFAULT):
    box = Picture().add_layer_chain(Layer(
        ["/" + "-" * (width - 2) + "\\"] + \
        ["|" + " " * (width - 2) + "|"] * (height - 2) + \
        ["\\" + "-" * (width - 2) + "/"], color))
    return box