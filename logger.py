# class for the communication label like a logger

class logger(object):
    def __init__(self):
        self.__text = ''

    def getText(self):
        return self.__text

    def addText(self, text, separator='\n'):
        
        self.__text = self.__text + separator + text

    def addTextToLabel(self, label, text, separator='\n'):
        
        self.addText(text, separetor=separator)
        label["text"] = self.__text