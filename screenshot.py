from pathlib import Path
import PIL.ImageGrab

class Screenshot:
    def __init__(self):
        self.save_path = Path.cwd() / "Screen_Shots"  
        self.save_path.mkdir(exist_ok=True)

    def take_shot1(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        file_name = "shot1.png"
        full_path = self.save_path / file_name 
        
        im = PIL.ImageGrab.grab(bbox=(top_left_x, top_left_y, bottom_right_x, bottom_right_y))
        im.save(full_path)
   

    def take_shot2(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        file_name_2 = "shot2.png"
        full_path_2 = self.save_path / file_name_2  

        im2 = PIL.ImageGrab.grab(bbox=(top_left_x, top_left_y, bottom_right_x, bottom_right_y))
        im2.save(full_path_2)
        
    
