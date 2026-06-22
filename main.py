import config
import screen
import picture.text_picture as text_picture

if __name__ == "__main__":
    init_config = config.InitConfig()
    game_screen = screen.GameScreen(init_config)
    game_frame = screen.GameFrame(init_config)

    game_frame.draw((0, 0), text_picture.picture1)

    game_screen.update_frame(game_frame)
    game_screen.refresh()
