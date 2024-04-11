import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText

def create_log_window():
    app = ctk.CTk()
    app.geometry("300x300")
    app.title("Log Ekranı")

    log_text = ScrolledText(app, width=40, height=10, wrap='word', state='normal', font=("Helvetica", 10))
    log_text.pack(padx=10, pady=10, fill='both', expand=True)

    def add_log_message():
        # Log sayacını artır
        add_log_message.counter += 1
        # Yeni log mesajını ekle
        log_text.insert('end', f"Log mesajı {add_log_message.counter}\n")
        # Görünümü sona kaydır
        log_text.yview('end')
        # 3000 ms sonra yani 3 saniye sonra bu fonksiyonu tekrar çağır
        app.after(1000, add_log_message)

    # İlk mesajı eklemek için sayaç
    add_log_message.counter = 0

    # İlk çağrıyı başlat
    add_log_message()

    app.mainloop()

create_log_window()
