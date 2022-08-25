import cv2
import numpy as np
import os

from . import slicer as slicer
from .assets import Assets


class chapter(object):
    def __init__(self, originPath, savePath=None, pages=[], 
                    nPages=0, width=700, fileExt = ".jpg",
                    nImage=0, totalHeigth=0, 
                    settings=Assets.defaultSetting):
        
        self.originPath = originPath
        
        if savePath == None:
            pardir = os.path.abspath(os.path.join(originPath, os.pardir))
            os.makedirs(os.path.join(pardir, "slicedChapter"))
            self.savePath = os.path.abspath(os.path.join(pardir, "slicedChapter"))
        elif not os.path.exists(savePath):
            os.makedirs(savePath)
            self.savePath = savePath
        else:
            self.savePath = savePath
        
        
        self.nImage = nImage
        self.totalHeigth = totalHeigth
        self.pages = pages
        self.nPages = nPages
        self.width = width
        self.fileExt = fileExt
        self.settings = self.checkSettings(settings)
        self.allPages = self.unificator()
        
    # check if settings are good (and return them in int) 
    # or otherwise return the dfault ones
    def checkSettings(self,settings):
        for i in range(4):
            if type(settings[i]) is str:
                if settings[i].isdigit():
                    settings[i] = int(settings[i])
                else:
                    settings[i] = Assets.defaultSetting[i]
                    continue
            
            if settings[i] < 0:
                settings[i] = Assets.defaultSetting[i]

        return settings

    # unify all the images in the originPath folder 
    # in one image to be more easy to work with
    def unificator(self):
        img = []

        for filename in os.listdir(self.originPath):
    
            if filename.endswith(Assets.supportedExtension):
                imgTemp = cv2.imread(self.originPath + '\\' +filename)
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
    
    # Whenever it finds a row where it can slice, 
    # it slices a page 'till the and of the chapter
    def brutalSlice(self):
        self.pages.clear()     #delete all pages already created from previous works
        pageOffset = self.settings[0]
        rowOffset = self.settings[1]
        borderOffset = self.settings[2]
        spacing = self.settings[3]
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
        os.startfile(self.savePath)

    #from the united chapter to all the pages with only one panel 
    # (at least some given pixel)
    def repage(self):
        self.pages.clear()     #delete all pages already created from previous works
        pageOffset = self.settings[0]
        rowOffset = self.settings[1]
        borderOffset = self.settings[2]
        spacing = self.settings[3]
        rowIndex = pageOffset
        panelDistance = 0
        startNewPage = 0

        while rowIndex < self.totalHeigth - 200:
            while (rowIndex < self.totalHeigth) and not(slicer.checkIfSlice(self.allPages[rowIndex,:], borderOffset=borderOffset, spacing=spacing)):
                rowIndex += rowOffset
            while (rowIndex < self.totalHeigth) and (slicer.checkIfSlice(self.allPages[rowIndex,:], borderOffset=borderOffset, spacing=spacing)):
                rowIndex += rowOffset
                panelDistance += rowOffset

            if panelDistance > 10:
                endPage = rowIndex - panelDistance // 2
                self.pages.append(slicer.slice(self.allPages, startNewPage, endPage, self.width))
                startNewPage = endPage
                self.nPages += 1
                rowIndex += pageOffset
                cv2.imwrite(self.savePath + "\\" + str(self.nPages).zfill(3) + self.fileExt, self.pages[self.nPages-1])
            
            panelDistance = 0
        
        self.pages.append(slicer.slice(self.allPages, startNewPage, self.totalHeigth, self.width))
        self.nPages += 1
        cv2.imwrite(self.savePath + "\\" + str(self.nPages).zfill(3) + self.fileExt,self.pages[self.nPages-1])
        os.startfile(self.savePath)
