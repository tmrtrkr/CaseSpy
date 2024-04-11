import customtkinter as ctk
import threading
from screenshot import Screenshot
import totxt
from gpt import send_prompt
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import mss
from screeninfo import get_monitors
import numpy as np


class LiveScreenCapture(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        monitor = get_monitors()[0]
        self.capture_area = {
            'top': monitor.y,
            'left': monitor.x,
            'width': monitor.width,
            'height': monitor.height
        }

        self.image_label = tk.Label(self)
        self.image_label.pack()

    
        self.update_capture()



    def capture_screen(self):
        with mss.mss() as sct:
            sct_img = sct.grab(self.capture_area)
            img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)

            target_width = 400
            target_height = 250
            resize_ratio_width = target_width / sct_img.width
            resize_ratio_height = target_height / sct_img.height
            resize_ratio = min(resize_ratio_width, resize_ratio_height)

          
             
            new_size = (int(sct_img.width * resize_ratio), int(sct_img.height * resize_ratio))

            img = img.resize(new_size)
            return img


    def update_capture(self):
        img = self.capture_screen()
        img_tk = ImageTk.PhotoImage(image=img)
        self.image_label.imgtk = img_tk
        self.image_label.configure(image=img_tk)

        
        self.after(50, self.update_capture)


class CustomGUI(tk.Tk):
    def __init__(self):
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()
        self.app.geometry("1500x750")
        self.app.title("CaseSpy")

        self.setup_widgets()




    def setup_widgets(self):

        
        self.api_key_entry = ctk.CTkEntry(self.app, width=400, placeholder_text="OpenAI API Key:")
        self.api_key_entry.place(x=50,y=50)

  



        #First ScreenShot
         
        #Screenshot label
        self.area_label = ctk.CTkLabel(self.app, text="First Screenshot")
        self.area_label.place(x=50,y=170)
        
        #top-right x label
        self.topleftLabel_X = ctk.CTkLabel(self.app, text="Top-right x")
        self.topleftLabel_X.place(x=200,y=140)

        self.topleft_x1 = ctk.CTkEntry(self.app, width=100, placeholder_text="topLeft x1 (px)")
        self.topleft_x1.place(x=200,y=170)
        self.topleft_x1.insert(0,"0")

        
        #top-right y label
        self.topleftLabel_Y = ctk.CTkLabel(self.app, text="Top-right y")
        self.topleftLabel_Y.place(x=320,y=140)

        self.topleft_y1 = ctk.CTkEntry(self.app, width=100, placeholder_text="topLeft y1 (px)")
        self.topleft_y1.place(x=320,y=170)
        self.topleft_y1.insert(0,"0")



        #bottom-left X label
        self.bottomleftLabel_X = ctk.CTkLabel(self.app, text="Bottom-Left X")
        self.bottomleftLabel_X.place(x=440,y=140)

        self.bottomRight_x1 = ctk.CTkEntry(self.app, width=100, placeholder_text="bottomRight x1 (px)")
        self.bottomRight_x1.place(x=440,y=170)
        self.bottomRight_x1.insert(0,"0")

        #bottom-left Y label
        self.bottomleftLabel_Y = ctk.CTkLabel(self.app, text="Bottom-Left Y")
        self.bottomleftLabel_Y.place(x=560,y=140)

        self.bottomRight_y1 = ctk.CTkEntry(self.app, width=100, placeholder_text="bottomRight y1 (px)")
        self.bottomRight_y1.place(x=560,y=170)
        self.bottomRight_y1.insert(0,"0")


        #Second ScreenShot

        self.area_label = ctk.CTkLabel(self.app, text="Second Screenshot")
        self.area_label.place(x=50,y=210)
        
        self.topleft_x2 = ctk.CTkEntry(self.app, width=100, placeholder_text="topLeft x2 (px)")
        self.topleft_x2.place(x=200,y=210)
        self.topleft_x2.insert(0,"0")

        
        self.topleft_y2 = ctk.CTkEntry(self.app, width=100, placeholder_text="topLeft y2 (px)")
        self.topleft_y2.place(x=320,y=210)
        self.topleft_y2.insert(0,"0")


        self.bottomRight_x2 = ctk.CTkEntry(self.app, width=100, placeholder_text="bottomRight x2 (px)")
        self.bottomRight_x2.place(x=440,y=210)
        self.bottomRight_x2.insert(0,"0")


        self.bottomRight_y2 = ctk.CTkEntry(self.app, width=100, placeholder_text="bottomRight y2 (px)")
        self.bottomRight_y2.place(x=560,y=210)
        self.bottomRight_y2.insert(0,"0")
       
        
        #Send buttonss
        
    
        self.screenshotBTN1 = ctk.CTkButton(self.app, width=90, height=30,corner_radius=30, text="TakeShot1",     command=lambda: self.sendScreenShotData1())
        self.screenshotBTN1.place(x=680,y=170)

        self.screenshotBTN2 = ctk.CTkButton(self.app, width=90, height=30,corner_radius=30, text="TakeShot2",     command=lambda: self.sendScreenShotData2())
        self.screenshotBTN2.place(x=680,y=210)



        self.solve_button = ctk.CTkButton(self.app, text="Solve", command=self.sendToApi, width=100, height=50)
        self.solve_button.place(x=50,y=100)


        self.output_frame = ctk.CTkFrame(self.app, width=1400, height=400, corner_radius=20, fg_color="white")
        self.output_frame.pack_propagate(False)
        self.output_frame.place(x=50, y=330)

        self.result_text = ctk.StringVar()

        self.result_label = ctk.CTkLabel(self.output_frame, pady=4, padx=4, textvariable=self.result_text, wraplength=1500, text_color="black", font=("Arial", 14))
        self.result_label.pack(side='left', anchor='nw')

        self.previous_button = ctk.CTkButton(self.app, text="Solve", width=100, height=50)

      

        #Logs box
        log_text = ScrolledText(self.app, width=50, height=15, wrap='word', state='normal', font=("Helvetica", 10))
        log_text.place(x=1430,y=50)
        





        self.live_capture = LiveScreenCapture(self.app)
        self.live_capture.place(x=1000, y=50, width=400, height=250)
     
        

    #Sending Screenshot position data for shot1
    def sendScreenShotData1(self):
        self.screenshot = Screenshot()
      
        self.result_label = "Loading..."
        threading.Thread(target=self.screenshot.take_shot1, args=(int(self.topleft_x1.get()), int(self.topleft_y1.get()), int(self.bottomRight_x1.get()), int(self.bottomRight_y1.get()))).start()


    #Sending Screenshot position data for shot2
    def sendScreenShotData2(self):
        self.screenshot = Screenshot()
     
        threading.Thread(target=self.screenshot.take_shot2, args=(int(self.topleft_x2.get()), int(self.topleft_y2.get()), int(self.bottomRight_x2.get()), int(self.bottomRight_y2.get()))).start()
       
       
    # trigger send imgtotxt, convert its return to prompt, send the prompt and api key to gpt
    def sendToApi(self):
        self.result_text.set("Loading...")
        self.totxt = totxt.Totxt()  
        prompt_text = self.totxt.imgToTxt()  
        
        if(prompt_text == "no screenshot found"):
            self.result_text.set(prompt_text)

        else:
            api_key = self.api_key_entry.get()  

            def thread_target(prompt_text, api_key):
                response = send_prompt(prompt_text, api_key)
                self.app.after(0, self.showApiResponse, response)

            thread = threading.Thread(target=thread_target, args=(prompt_text, api_key))
            thread.start()


    #show gpt response on the screen and log http 200 if success
    def showApiResponse(self, response):
        print("Response SUCCCESFUL!")
        self.result_text.set(response)



    


    def run(self):
        self.app.mainloop()

