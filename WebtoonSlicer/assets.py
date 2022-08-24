import logger
import os
## my variable

class Assets(object):
    log = logger.logger()
    pathToIcon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon' + os.sep + 'icon.ico')
    defaultSetting = [2500, 20, 40, 5]
    supportedExtension = ['jpg', 'png']
    settingLabel = [
        "Min. page size", "Scan distance", 
        "Border size", "Scan spacing", 
        "Input extension"
    ]
    helpButton =[
        'The pixel minimum height of a sliced page.',
        'The pixel distance between two consecutive scanned row.',
        'The pixel distance used by the code to detect a possible panel border.',
        'The distance between two consecutive pixel when scannig a row.',
        'The extension of the file you want to slice: only ' + ', '.join(supportedExtension) + ' supported'
    ]