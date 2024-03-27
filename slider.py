import tkinter as tk
import random as r

root = tk.Tk()
root.geometry("600x400")
root.title('スライドショー')
canvas = tk.Canvas(bg="black", width=600,height=400,highlightthickness=0)
canvas.place(x=0,y=0)


def showphoto():
    global photo
    file_name = f'images/s{str(r.randint(2,8))}.png'
    photo = tk.PhotoImage(file=file_name)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    root.after(3000, showphoto)
#一回目のshowphoto呼び出し
showphoto()
# メインループ(最後に必ず書く)
root.mainloop()