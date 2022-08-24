# class for the communication label like a logger

class logger(object):
    def __init__(self):
        self.__text = ''

    def getText(self):
        return self.__text

    def printText(self, label):
        label["text"] = self.__text

    def addText(self, text, separator='\n'):
        self.__text = self.__text + separator + text

    def addTextToLabel(self, label, text, separator='\n'):
        self.addText(text, separator=separator)
        self.printText(label)

    def clearText(self):
        self.__text = ''

    def presentation(self, label):
        text = 'Welcome to Webtoon Slicer 1.0!!'
        self.addText(text, separator='\n')

        text = "Insert the chapter's origin folder and the output folder (not mandatory)."
        self.addText(text, separator='\n\n')

        text = "You can also insert the desidered parameters (default already setted)."
        self.addText(text, separator=' ')

        text = "When you're ready press the 'Start' button and wait a few seconds."
        self.addText(text, separator='\n')

        self.printText(label)