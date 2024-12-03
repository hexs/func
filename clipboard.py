import time
from datetime import datetime
import tkinter as tk

root = tk.Tk()
root.withdraw()

while True:
    t1 = datetime.now()
    clipboard_content = root.clipboard_get()
    print("Clipboard content:", clipboard_content)
    t2 = datetime.now()
    print((t2 - t1).total_seconds())
    time.sleep(1)