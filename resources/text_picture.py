from class_dir import color
from class_dir.picture_class import Layer, Picture

startPictureLayer0 = Layer(
    ["Welcome to the game!",
     "Check the mode and settings.",
     "1. Start game!",
     "2. Settings",
     "3. Exit"],
    color.Color.YELLOW,
)

startPicture = Picture().add_layer_chain(startPictureLayer0)
picture_1 = Picture().add_layer_chain(
    Layer(
        ["This is picture 1.",
         "You can add more layers to this picture.",
         "Each layer can have its own color and content."],
        color.Color.GREEN,
    )
)
