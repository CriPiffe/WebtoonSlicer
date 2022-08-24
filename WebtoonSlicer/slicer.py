import numpy as np

'''Check if in the given row there is a panel border (left or/and right)
if not, then check if the raw has the same color all along'''
def checkRow(row, color, borderOffset=40, spacing=5):

    for i in range(borderOffset):
        if not (np.array_equal(row[i,:], color)) or not (np.array_equal(row[-i,:], color)):
            return False

    for i in range(borderOffset, len(row), spacing):
        if not (np.array_equal(row[i,:], color)):
            return False
    
    return True


def checkIfSlice(row, borderOffset=40, spacing=5):
    
    color = row[0,:] 
    return checkRow(row,color, borderOffset = borderOffset, spacing=spacing)



def slice(chapter, start, end, width):

    page = np.zeros((end-start, width, 3), dtype=np.uint8)
    page[:,:,:] = chapter[start:end,:,:]

    return page
