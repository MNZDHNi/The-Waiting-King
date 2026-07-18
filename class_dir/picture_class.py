from .color import Color

def split_by_newline(text: str) -> list[str]:
    list = text.split("\n")
    if list[0] and list[-1] == "":
        list = list[1:-1]
    # if list[0] == "":
    #     list = list[1:]
    # if list[-1] == "":
    #     list = list[:-1]
    return list

class Layer:
    def __init__(self, layer: list[str] | str, color: Color = Color.DEFAULT) -> None:
        if isinstance(layer, str):
            layer = split_by_newline(layer)
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

    def add_layers(self, layers: list[Layer]) -> None:
        self.layers.extend(layers)
        self.length += len(layers)

    def add_layer_chain(self, layer: Layer) -> "Picture":
        self.add_layer(layer)
        return self


class Map(Picture):
    def __init__(self, mapId: int, mapName: str) -> None:
        super().__init__()
        self.mapId = mapId
        self.mapName = mapName
