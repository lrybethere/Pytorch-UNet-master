import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import time

class TrainingThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            # 模拟训练过程
            print("Training...")
            time.sleep(1)
        print("Training stopped.")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("训练界面")
        self.geometry("400x200")

        self.training_thread = None

        # 训练开始按钮
        start_button = ttk.Button(self, text="开始训练", command=self.start_training)
        start_button.pack(pady=10)

        # 训练停止按钮
        stop_button = ttk.Button(self, text="停止训练", command=self.stop_training)
        stop_button.pack(pady=10)

    def start_training(self):
        if self.training_thread is None:
            self.training_thread = TrainingThread()
            self.training_thread.start()
        else:
            messagebox.showinfo("提示", "训练已经开始！")

    def stop_training(self):
        if self.training_thread is not None:
            self.training_thread.stop()
            self.training_thread = None
        else:
            messagebox.showinfo("提示", "训练还未开始！")

if __name__ == "__main__":
    app = App()
    app.mainloop()
