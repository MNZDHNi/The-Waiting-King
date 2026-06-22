import os
import picture.color as color
import picture.picture_class as picture_class

"""
屏幕模块，包含GameScreen和GameFrame类。
GameScreen负责管理屏幕的显示和刷新，GameFrame负责管理当前帧的内容。
"""
class GameScreen:
    def __init__(self, InitConfig):
        self.width = InitConfig.width
        self.height = InitConfig.height
        self.have_new_frame = False

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def update_frame(self, new_frame):
        if new_frame is not None:
            self.have_new_frame = new_frame

    def refresh(self):
        if not self.have_new_frame:
            return
        
        self.clear()
        print("/", "-" * self.width, "\\", sep="")

        for i in range(self.height):
            print("|", end="")
            for j in range(self.width):
                if self.have_new_frame is not None:
                    print(self.have_new_frame.picture[i][j], end="")
                else:
                    print(" ", end="")
            print("|")

        print("\\", "-" * self.width, "/", sep="")
        self.have_new_frame = False

    def qiuck_refresh(self, new_frame):
        self.update_frame(new_frame)
        self.refresh()


class GameFrame:
    def __init__(self, InitConfig):
        self.width = InitConfig.width
        self.height = InitConfig.height
        self.picture = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def draw(self, position, content: picture_class.Picture):
        x, y = position
        if content.length == 0 :
            return
        
        for i in range(content.length):
            for j in range(len(content.layers[i].layer)):
                for k in range(len(content.layers[i].layer[j])):
                    if 0 <= y + j < self.height and 0 <= x + k < self.width:
                        if content.layers[i].layer[j][k] is None:
                            self.picture[y + j][x + k] == " "
                            continue
                        elif content.layers[i].layer[j][k] is " ":
                            continue
                        self.picture[y + j][x + k] = color.set_color(content.layers[i].color, content.layers[i].layer[j][k])
                    else:
                         raise ValueError("绘制内容超出屏幕范围")
                        
