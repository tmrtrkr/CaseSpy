import customtkinter as ctk


class SplashScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")
        self.title("Başlangıç Ekranı")

        label = ctk.CTkLabel(self, text="Markam ve Uygulama İsmi", font=("Arial", 20))
        label.pack(pady=20)

        self.after(3000, self.destroy)  


