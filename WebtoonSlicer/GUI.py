import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import os
from time import time

import chapter
from assets import Assets

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
    chapter.chapter(
        originPath=orPath, 
        savePath=svPath,
        fileExt=inputeExtension, 
        settings=settings
    ).brutalSlice()
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
window.iconbitmap(Assets.pathToIcon)

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


####### SETTING ENTRY #######

#TODO:  function for settingFrame = []

# minimum size of the page
minsizeFrame = tk.Frame(master=settingFrame)
minsizeFrame.pack(fill=tk.X, pady=5)
minsizeLabel = ttk.Label(
    master=minsizeFrame,
    width=14,
    text="Min. page size"
).pack(side=tk.LEFT)
minsize = ttk.Entry(
    master=minsizeFrame,

)
minsize.pack(fill=tk.X, side=tk.LEFT)
minsize.insert(0, "2500")
helpminsizeButton = ttk.Button(
    master=minsizeFrame,
    text="Help",
    command=lambda: help(0)
)
helpminsizeButton.pack(fill=tk.X, side=tk.LEFT)

# distance between 2 row to be scanned 
scdistFrame = tk.Frame(master=settingFrame)
scdistFrame.pack(fill=tk.X, pady=5)
scdistLabel = ttk.Label(
    master=scdistFrame,
    width=14,
    text="Scan distance"
).pack(side=tk.LEFT)
scanDistance = ttk.Entry(
    master=scdistFrame
)
scanDistance.pack(fill=tk.X, side=tk.LEFT)
scanDistance.insert(0, "20")
helpScdistButton = ttk.Button(
    master=scdistFrame,
    text="Help",
    command=lambda: help(1)
)
helpScdistButton.pack(fill=tk.X, side=tk.LEFT)


# border distance from the margin of the page
borderFrame = tk.Frame(master=settingFrame)
borderFrame.pack(fill=tk.X, pady=5)
borderLabel = ttk.Label(
    master=borderFrame,
    width=14,
    text="Border size"
).pack(side=tk.LEFT)
bordersize = ttk.Entry(
    master=borderFrame
)
bordersize.pack(fill=tk.X, side=tk.LEFT)
bordersize.insert(0, "40")
helpborderButton = ttk.Button(
    master=borderFrame,
    text="Help",
    command=lambda: help(2)
)
helpborderButton.pack(fill=tk.X, side=tk.LEFT)


# spacing between scanned pixel
spaceFrame = tk.Frame(master=settingFrame)
spaceFrame.pack(fill=tk.X, pady=5)
spaceLabel = ttk.Label(
    master=spaceFrame,
    width=14,
    text="Scan spacing"
).pack(side=tk.LEFT)
spacing = ttk.Entry(
    master=spaceFrame
)
spacing.pack(fill=tk.X, side=tk.LEFT)
spacing.insert(0, "5")
helpspacingButton = ttk.Button(
    master=spaceFrame,
    text="Help",
    command=lambda: help(3)
)
helpspacingButton.pack(fill=tk.X, side=tk.LEFT)

# spacing between scanned pixel
extFrame = tk.Frame(master=settingFrame)
extFrame.pack(fill=tk.X, pady=5)
extLabel = ttk.Label(
    master=extFrame,
    width=14,
    text="Input extension"
).pack(side=tk.LEFT)
extension = ttk.Entry(
    master=extFrame
)
extension.pack(fill=tk.X, side=tk.LEFT)
extension.insert(0, "jpg")
helpextButton = ttk.Button(
    master=extFrame,
    text="Help",
    command=lambda: help(4)
)
helpextButton.pack(fill=tk.X, side=tk.LEFT)


#start button
startButton = ttk.Button(
    master=settingFrame,
    text="Start!",
    command=start
)
startButton.pack()


def main():
    Assets.log.presentation(communicationLabel)
    window.mainloop()

if __name__ == "__main__":
    main()
    