import tkinter as tk
import os
import chapter

def start():
    orPath = originPath.get()
    svPath = savePath.get()
    
    #check origin folder
    if len(orPath) <=3:
        communicationEntry.insert(tk.END, "\nType a possible path, this is too short!")
        return
    else:
        orPath = os.path.abspath(originPath.get())
    
    #check save folder
    if len(svPath) == 0:
        chapter.chapter(originPath=orPath).brutalSlice()
        communicationEntry.insert(tk.END, "\nfinished!")
        return
    elif len(svPath) <= 3:
        communicationEntry.insert(tk.END, "\nType a possible path, this is too short!")
        return
    else:
        svPath = os.path.abspath(savePath.get())

    
    chapter.chapter(originPath=orPath, savePath=svPath).brutalSlice()
    communicationEntry.insert(tk.END, "\nfinished!")
    





window = tk.Tk()
window.geometry("600x200")
window.title("Page Slicer 3000")

explain = tk.Label(
    text="Insert origin and save path"
).pack(side=tk.TOP)

originPath = tk.Entry(width=100)
originPath.pack()
savePath = tk.Entry(width=100)
savePath.pack()

communicationEntry = tk.Entry(width=100)
communicationEntry.pack()

startButton = tk.Button(
    text="Start!",
    width=25,
    height=5,
    command=start
)
startButton.pack(side=tk.BOTTOM)


if __name__ == "__main__":
    window.mainloop()