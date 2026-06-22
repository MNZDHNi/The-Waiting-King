import config
import screen
import get_input

import picture.text_picture as text_picture

if __name__ == "__main__":
    # 初始化配置，屏幕和帧
    init_config = config.InitConfig()
    game_screen = screen.GameScreen(init_config)
    game_frame = screen.GameFrame(init_config)

    # 绘制frame
    game_frame.draw((0, 0), text_picture.picture1)
    
    # 初始化screen和frame后，先绘制一次，显示初始界面
    game_screen.update_frame(game_frame)
    game_screen.refresh()

    # 主循环，等待用户输入
    """
    while True:
        match get_input.GetKey():
            case "1":
                pass
            case "2":
                pass
            case _:
                raise ValueError("按你mb呢")
    """