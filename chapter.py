import cv2
import numpy as np
import os
import slicer

class chapter(object):
    def __init__(self, originPath, savePath=None, nImage=0, totalHeigth=0, 
                 pages=[], nPages=0, width=700, fileExt = ".jpg"):
        
        self.originPath = originPath
        
        if savePath == None:
            pardir = os.path.abspath(os.path.join(originPath, os.pardir))
            os.makedirs(os.path.join(pardir, "slicedChapter"))
            self.savePath = os.path.abspath(os.path.join(pardir, "slicedChapter"))
        else:
            self.savePath = savePath
        self.nImage = nImage
        self.totalHeigth = totalHeigth
        self.allPages = self.unificator(originPath)
        self.pages = pages
        self.nPages = nPages
        self.width = width
        self.fileExt = fileExt


    def unificator(self, path):
        img = []

        for filename in os.listdir(path):
    
            if filename.endswith('.jpg'):
                imgTemp = cv2.imread(path + '\\' +filename)
                img.append(imgTemp)
                self.totalHeigth += imgTemp.shape[0]
                self.nImage += 1

        self.width = imgTemp.shape[1]
        allPages = np.zeros((self.totalHeigth, self.width, 3), dtype=np.uint8)
        allPages[:,:] = (255,255,255)

        hPrev = 0
        for i in range(self.nImage):
            hNext = img[i].shape[0]
            allPages[hPrev:hPrev+hNext, :, :3] = img[i]
            hPrev += hNext
        return allPages
    
    
    def brutalSlice(self, offset=[2500,20,60,5]):
        pageOffset = offset[0]
        rowOffset = offset[1]
        borderOffset = offset[2]
        spacing = offset[3]
        rowIndex = pageOffset
        startNewPage = 0

        while rowIndex < self.totalHeigth - 200:
            if(slicer.checkIfSlice(self.allPages[rowIndex,:], borderOffset=borderOffset, spacing=spacing)):

                ##slice and create a new page
                self.pages.append(slicer.slice(self.allPages, startNewPage, rowIndex, self.width))
                self.nPages += 1
                startNewPage = rowIndex
                rowIndex += pageOffset
                cv2.imwrite(self.savePath + "\\" + str(self.nPages).zfill(3) + self.fileExt, self.pages[self.nPages-1])
            else:
                rowIndex += rowOffset

        self.pages.append(slicer.slice(self.allPages, startNewPage, self.totalHeigth, self.width))
        self.nPages += 1
        cv2.imwrite(self.savePath + "\\" + str(self.nPages).zfill(3) + self.fileExt,self.pages[self.nPages-1])

            

