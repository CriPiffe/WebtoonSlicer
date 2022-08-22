import tkinter as tk
import os
from time import time
import chapter
import logger


log = logger.logger()


def checkSetting(entry, default):
    val = entry.get()
    if val.isdigit() and val > 0:
        val = int(val)
    else:
        val = default
    return val

def start():
    log.clearText()

    #check input parameters for page slicing
    minimumsize = checkSetting(minsize, 2500)
    rowDistance= checkSetting(scanDistance, 20)
    border = checkSetting(bordersize, 60)
    space = checkSetting(spacing, 5)

    settings =[minimumsize, rowDistance, border, space]

    # check path input
    orPath = originPath.get()
    svPath = savePath.get()
    
    #check origin folder
    if len(orPath) <=3:
        log.addTextToLabel(communicationLabel, 
            "Type a possible path, this is too short!"
        )
        return
    else:
        orPath = os.path.abspath(originPath.get())
    
    if not os.path.exists(orPath):
        log.addTextToLabel(communicationLabel, 
            "This path does not exist!"
        )  

    #check save folder
    if len(svPath) == 0:
        svPath = None
    elif len(svPath) <= 3:
        log.addTextToLabel(communicationLabel, 
            "Type a possible path, this is too short!"
        )
        return
    else:
        svPath = os.path.abspath(savePath.get())
    start = time()
    chapter.chapter(originPath=orPath, savePath=svPath).brutalSlice(offset=settings)
    finish = str(time() - start) + " s"
    log.addTextToLabel(communicationLabel, 
        "Finished in !"+finish, separator='\n\n'
    ) 

#### HELPER FUNCTION ####
def helpMinsize():
    log.clearText()
    log.addTextToLabel(communicationLabel, 'The pixel minimum height of a sliced page.')
    return True

def helpScdist():
    log.clearText()
    log.addTextToLabel(communicationLabel, 'The pixel distance between two consecutive scanned row.')
    return True

def helpBorder():
    log.clearText()
    log.addTextToLabel(communicationLabel, 'The pixel distance used by the code to detect a possible panel border.')
    return True
    
def helpSpacing():
    log.clearText()
    log.addTextToLabel(communicationLabel, 'The distance between two consecutive pixel when scannig a row.')
    return True

## window spec
window = tk.Tk()
window.geometry('1000x600+0+0')
window.title("Webtoon Slicer")
window.resizable(False, False)
icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon' + os.sep + 'icon.ico')
window.iconbitmap(icon)

######## window frames
# main frame
leftFrame = tk.Frame(master=window, width=500, height=600,
    #highlightbackground="blue", highlightthickness=2
)
leftFrame.pack(side=tk.LEFT)
leftFrame.pack_propagate(0)

rightFrame = tk.Frame(master=window, width=500, height=600, 
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
explain = tk.Label(
    master=pathFrame,
    text="Insert origin and save path"
).pack()

#setting explain label
settingLabel = tk.Label(
    master=settingFrame,
    text="Set all the wanted parameters"
).pack()

#communication log label
communicationLabel = tk.Label(
    master=logFrame,
    height=600, 
    anchor='n',
    relief=tk.GROOVE
)
communicationLabel.pack(fill=tk.BOTH)

###### PATH ENTRY ######

# origin path
orpathFrame = tk.Frame(master=pathFrame)
orpathFrame.pack(fill=tk.X, pady=10)
originLabel = tk.Label(
    master=orpathFrame,
    width=10,
    text="Chapter path"
).pack(side=tk.LEFT)
originPath = tk.Entry(
    master=orpathFrame,
    width=70
)
originPath.pack(fill=tk.X, side=tk.LEFT)

# origin path
svpathFrame = tk.Frame(master=pathFrame)
svpathFrame.pack(fill=tk.X, pady=10)
saveLabel = tk.Label(
    master=svpathFrame,
    width=10,
    text="Saving folder"
).pack(side=tk.LEFT)
savePath = tk.Entry(
    master=svpathFrame,
    width=70
)
savePath.pack(fill=tk.X, side=tk.LEFT)


####### SETTING ENTRY #######

# minimum size of the page
minsizeFrame = tk.Frame(master=settingFrame)
minsizeFrame.pack(fill=tk.X, pady=10)
minsizeLabel = tk.Label(
    master=minsizeFrame,
    width=10,
    text="Minimum\npage size"
).pack(side=tk.LEFT)
minsize = tk.Entry(
    master=minsizeFrame
)
minsize.pack(fill=tk.X, side=tk.LEFT)
helpminsizeButton = tk.Button(
    master=minsizeFrame,
    text="Help",
    command=helpMinsize
)
helpminsizeButton.pack(fill=tk.X, side=tk.LEFT)

# distance between 2 row to be scanned 
scdistFrame = tk.Frame(master=settingFrame)
scdistFrame.pack(fill=tk.X, pady=10)
scdistLabel = tk.Label(
    master=scdistFrame,
    width=10,
    text="Scan\ndistance"
).pack(side=tk.LEFT)
scanDistance = tk.Entry(
    master=scdistFrame
)
scanDistance.pack(fill=tk.X, side=tk.LEFT)
helpScdistButton = tk.Button(
    master=scdistFrame,
    text="Help",
    command=helpScdist
)
helpScdistButton.pack(fill=tk.X, side=tk.LEFT)


# border distance from the margin of the page
borderFrame = tk.Frame(master=settingFrame)
borderFrame.pack(fill=tk.X, pady=10)
borderLabel = tk.Label(
    master=borderFrame,
    width=10,
    text="Border size"
).pack(side=tk.LEFT)
bordersize = tk.Entry(
    master=borderFrame
)
bordersize.pack(fill=tk.X, side=tk.LEFT)
helpborderButton = tk.Button(
    master=borderFrame,
    text="Help",
    command=helpBorder
)
helpborderButton.pack(fill=tk.X, side=tk.LEFT)


# spacing between scanned pixel
spaceFrame = tk.Frame(master=settingFrame)
spaceFrame.pack(fill=tk.X, pady=10)
spaceLabel = tk.Label(
    master=spaceFrame,
    width=10,
    text="Scan spacing"
).pack(side=tk.LEFT)
spacing = tk.Entry(
    master=spaceFrame
)
spacing.pack(fill=tk.X, side=tk.LEFT)
helpspacingButton = tk.Button(
    master=spaceFrame,
    text="Help",
    command=helpSpacing
)
helpspacingButton.pack(fill=tk.X, side=tk.LEFT)


#start button
startButton = tk.Button(
    master=settingFrame,
    text="Start!",
    width=5,
    height=2,
    command=start
)
startButton.pack()


if __name__ == "__main__":
    window.mainloop()