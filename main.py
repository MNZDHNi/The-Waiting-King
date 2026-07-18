import config
import class_dir.screen as screen
from class_dir.color import Color
import resources.text_picture as text_picture
import resources.map.box as box

if __name__ == "__main__":
    init_config = config.InitConfig()
    game_screen = screen.GameScreen(init_config)

    game_screen.refresh(empty=True)
    while True:

        key = screen.get_input()
        match key:
            case "1":
                game_frame1 = screen.GameFrame(init_config)
                game_frame1.draw((0, 0), text_picture.picture_1)
                game_screen.quick_refresh(game_frame1)
            case "2":
                game_frame2 = screen.GameFrame(init_config)
                game_frame2.draw((0, 0), text_picture.startPicture)
                game_screen.quick_refresh(game_frame2)
            case "3":
                game_screen.empty_refresh()
            case "4":
                pass