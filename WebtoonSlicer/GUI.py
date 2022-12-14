import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import os
from time import time

from . import chapter
from .assets import Assets

def start():
    Assets.log.clearText()

    settings =[minsize.get(), scanDistance.get(), bordersize.get(), spacing.get()]
    if extension.get() in Assets.supportedExtension:
        inputeExtension = '.' + extension.get()
    else:
        Assets.log.addTextToLabel(communicationLabel, 
            extension.get() + " is not supported!"
        )
        return

    # check path input
    orPath = originPath.get()
    svPath = savePath.get()
    
    #check origin folder
    if len(orPath) <=3:
        Assets.log.addTextToLabel(communicationLabel, 
            "Type a possible path, this is too short!"
        )
        return
    else:
        orPath = os.path.abspath(originPath.get())
    
    if not os.path.exists(orPath):
        Assets.log.addTextToLabel(communicationLabel, 
            "This path does not exist!"
        )  

    #check save folder
    if len(svPath) == 0:
        svPath = None
    elif len(svPath) <= 3:
        Assets.log.addTextToLabel(communicationLabel, 
            "Type a possible path, this is too short!"
        )
        return
    else:
        svPath = os.path.abspath(savePath.get())
        
    Assets.log.addTextToLabel(communicationLabel, 
        "Starting to slice!!", separator='\n\n'
    )
    start=time()
    cap = chapter.chapter(
        originPath=orPath, 
        savePath=svPath,
        fileExt=inputeExtension, 
        settings=settings
    )
    if slicerSel.get() == Assets.supportedSlicing[0]:
        cap.brutalSlice()
    else:
        cap.optimalSlice()
    del cap
    Assets.log.addTextToLabel(communicationLabel, 
        "Finished in " + str(time()-start) + 's!', separator='\n\n'
    )

#### BROWSE FUNCTION ####
def browseFolder(entry):
    entry.delete(0, tk.END)
    path = filedialog.askdirectory()
    entry.insert(0, path)

#### HELPER FUNCTION ####
def help(n):
    Assets.log.clearText()
    Assets.log.addTextToLabel(communicationLabel, Assets.helpButton[n])

## window spec
window = tk.Tk()
window.geometry('1000x400+0+0')
window.title("Webtoon Slicer")
window.resizable(False, False)
#window.iconbitmap(Assets.pathToIcon)

######## window frames
# main frame
leftFrame = tk.Frame(master=window, width=600, height=400,
    #highlightbackground="blue", highlightthickness=2
)
leftFrame.pack(side=tk.LEFT)
leftFrame.pack_propagate(0)

rightFrame = tk.Frame(master=window, width=400, height=400, 
    #highlightbackground="blue", highlightthickness=2
)
rightFrame.pack(side=tk.RIGHT)
rightFrame.pack_propagate(0)

#sub frame
pathFrame = tk.Frame(
    master=leftFrame,
    #highlightbackground="yellow", highlightthickness=2
    )
pathFrame.pack(fill=tk.X, pady=20)

logFrame = tk.Frame(
    master=rightFrame, 
    height=600, 
    #highlightbackground="yellow", highlightthickness=2
    )
logFrame.pack(fill=tk.BOTH)

settingFrame = tk.Frame(
    master=leftFrame
    #highlightbackground="yellow", highlightthickness=2
    )
settingFrame.pack(fill=tk.X, pady=10)


#path explain label
explain = ttk.Label(
    master=pathFrame,
    text="Insert origin and save path"
).pack()

#setting explain label
settingLabel = ttk.Label(
    master=settingFrame,
    text="Set all the wanted parameters"
).pack()

#communication log label
communicationLabel = ttk.Label(
    master=logFrame,
    anchor='n',
    justify=tk.CENTER,
    wraplengt=350,
    relief=tk.GROOVE
)
communicationLabel.pack(fill=tk.BOTH, ipady=300)

###### PATH ENTRY ######

# origin path
orpathFrame = tk.Frame(master=pathFrame)
orpathFrame.pack(fill=tk.X, pady=10)
originLabel = ttk.Label(
    master=orpathFrame,
    width=14,
    text="Chapter path"
).pack(side=tk.LEFT)
originPath = ttk.Entry(
    master=orpathFrame,
    width=70
)
originPath.pack(fill=tk.X, side=tk.LEFT)
browsePathButton = ttk.Button(
    master=orpathFrame,
    text="Browse...",
    command=lambda: browseFolder(originPath)
)
browsePathButton.pack(fill=tk.X, side=tk.LEFT)


# origin path
svpathFrame = tk.Frame(master=pathFrame)
svpathFrame.pack(fill=tk.X, pady=10)
saveLabel = ttk.Label(
    master=svpathFrame,
    width=14,
    text="Saving folder"
).pack(side=tk.LEFT)
savePath = ttk.Entry(
    master=svpathFrame,
    width=70
)
savePath.pack(fill=tk.X, side=tk.LEFT)
browsePathButton = ttk.Button(
    master=svpathFrame,
    text="Browse...",
    command=lambda: browseFolder(savePath)
)
browsePathButton.pack(fill=tk.X, side=tk.LEFT)


####### SETTING FRAME #######

setFrame=[]
for i in range(6):
    setFrame.append(tk.Frame(master=settingFrame))
    setFrame[i].pack(fill=tk.X, pady=5)
    minsizeLabel = ttk.Label(
        master=setFrame[i],
        width=14,
        text=Assets.settingLabel[i]
    ).pack(side=tk.LEFT)

# minimum size of the page
minsize = ttk.Entry(
    master=setFrame[0]
)
minsize.pack(fill=tk.X, side=tk.LEFT)
minsize.insert(0, "2500")

# distance between 2 row to be scanned 
scanDistance = ttk.Entry(
    master=setFrame[1]
)
scanDistance.pack(fill=tk.X, side=tk.LEFT)
scanDistance.insert(0, "20")

# border distance from the margin of the page
bordersize = ttk.Entry(
    master=setFrame[2]
)
bordersize.pack(fill=tk.X, side=tk.LEFT)
bordersize.insert(0, "40")

# spacing between scanned pixel
spacing = ttk.Entry(
    master=setFrame[3]
)
spacing.pack(fill=tk.X, side=tk.LEFT)
spacing.insert(0, "5")

# spacing between scanned pixel
extension = ttk.Entry(
    master=setFrame[4]
)
extension.pack(fill=tk.X, side=tk.LEFT)
extension.insert(0, "jpg")

for i in range(5):
    helpButton = ttk.Button(
        master=setFrame[i],
        text="Help",
        command=lambda: help(i)
    ).pack(fill=tk.X, side=tk.LEFT)


#slicer selection
slicerSel = tk.StringVar()
slicerOpt = ttk.OptionMenu(
    setFrame[5],
    slicerSel,
    *Assets.supportedSlicing
).pack(side=tk.LEFT)

#start button
startButton = ttk.Button(
    master=setFrame[5],
    text="Start!",
    command=start
)
startButton.pack(side=tk.RIGHT, padx=20)


def main():
    Assets.log.presentation(communicationLabel)
    window.mainloop()

if __name__ == "__main__":
    main()
    