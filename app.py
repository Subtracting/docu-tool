from pynput.keyboard import Key, Listener
import pyperclip
import tkinter as tk
import pyautogui as pya
import pyperclip
import time
import webbrowser

target_dict = {"test": "https://www.google.com/",
               "prestatiecode": "definitie prestatiecode"}


def open_link(hyperlink):
    webbrowser.open(hyperlink)


def copy_clipboard():
    pyperclip.copy("")
    pya.hotkey('ctrl', 'c')
    time.sleep(.02)
    return pyperclip.paste()


def initiate_popup(selected_text):

    hyperlink = target_dict[selected_text]

    x, y = pya.position()
    WINDOW_WIDTH = len(hyperlink)*8
    WINDOW_HEIGHT = 20

    popup = tk.Tk()
    popup.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

    popup.overrideredirect(True)
    popup.lift()
    popup.attributes('-topmost', True)
    popup.grab_set()

    label = tk.Label(popup, text=hyperlink)
    label.pack()

    link_label = tk.Label(popup, text=hyperlink, fg="blue", cursor="hand2")
    link_label.pack()
    # link_label.bind("<Button-1>", open_link(hyperlink))

    popup.update()
    popup.after(2000, popup.destroy)
    popup.mainloop()


def check_selected_text(selected_text):

    if selected_text in target_dict:
        initiate_popup(selected_text)


def on_release(key):
    if key == Key.f2:
        selected_text = copy_clipboard()
        check_selected_text(selected_text)
    if key == Key.esc:
        return False


while True:
    with Listener(
            on_release=on_release) as listener:
        listener.join()
