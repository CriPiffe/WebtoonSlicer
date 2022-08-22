import tkinter as tk
import os
import chapter
import logger


log = logger.logger()


def checkSetting(entry, default):
    val = entry.get()
    if val.isdigit():
        val = int(val)
    else:
        val = default
    return val

def start():
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
        log.addTextToLabel(communicationEntry, 
            "Type a possible path, this is too short!"
        )   
        return
    else:
        orPath = os.path.abspath(originPath.get())
    
    if not orPath.isdir():
        log.addTextToLabel(communicationEntry, 
            "This path does not exist!"
        )  

    #check save folder
    if len(svPath) == 0:
        svPath = None
        return
    elif len(svPath) <= 3:
        log.addTextToLabel(communicationEntry, 
            "Type a possible path, this is too short!"
        )  
        return
    else:
        svPath = os.path.abspath(savePath.get())
    
    chapter.chapter(originPath=orPath, savePath=svPath).brutalSlice(offset=settings)
    log.addTextToLabel(communicationEntry, 
        "finished!", separator='\n\n'
    ) 


## window spec
window = tk.Tk()
window.geometry('1000x600+0+0')
window.title("Page Slicer 3000")
window.resizable(False, False)
##window.iconbitmap(pathToIcon)

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
pathFrame = tk.Frame(master=leftFrame, highlightbackground="yellow", highlightthickness=2)
pathFrame.pack(fill=tk.X)

logFrame = tk.Frame(master=rightFrame, height=600, highlightbackground="yellow", highlightthickness=2)
logFrame.pack(fill=tk.BOTH)

settingFrame = tk.Frame(master=leftFrame, highlightbackground="yellow", highlightthickness=2)
settingFrame.pack(fill=tk.X, pady=20)


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
communicationEntry = tk.Label(
    master=logFrame,
    height=600, 
    anchor='n',
    #highlightbackground="green", highlightthickness=2
)
communicationEntry.pack(fill=tk.BOTH)

#path entry in path frame
originPath = tk.Entry(
    master=pathFrame
)
originPath.pack(fill=tk.X, pady=10)

savePath = tk.Entry(
    master=pathFrame
)
savePath.pack(fill=tk.X, pady=10)

# setting entry
minsizeFrame = tk.Frame(master=settingFrame)
minsizeFrame.pack(fill=tk.X, pady=10)
minsizeLabel = tk.Label(
    master=minsizeFrame,
    text="Minimum\npage size", highlightbackground="green", highlightthickness=2
).pack(side=tk.LEFT)
minsize = tk.Entry(
    master=minsizeFrame
)
minsize.pack(fill=tk.X, side=tk.LEFT)
#minsize.insert(tk.END,"Insert min size of the sliced page")

scanDistance = tk.Entry(
    master=settingFrame
)
scanDistance.pack(fill=tk.X, pady=10)
#minsize.insert(tk.END,"Insert distance between consecutive row scan")

bordersize = tk.Entry(
    master=settingFrame
)
bordersize.pack(fill=tk.X, pady=10)
#minsize.insert(tk.END,"Insert size for border check")

spacing = tk.Entry(
    master=settingFrame
)
spacing.pack(fill=tk.X, pady=10)
#minsize.insert(tk.END,"Insert spacing for row check")

#window button
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