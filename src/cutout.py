from segmentation import findRoot
from PIL import Image

def cutout(image, rootMat):
    height = image.shape[0]
    width = image.shape[1]

    sumDict = {}
    countDict = {}

    # find sum and count for each segment
    for i in range(height):
        for j in range(width):
            #currRoot = findRoot(rootMat, (i, j))
            currRoot = rootMat[i][j]

            if (currRoot not in sumDict):
                sumDict[currRoot] = (0, 0, 0)
                countDict[currRoot] = 0

            sumDict[currRoot] = (sumDict[currRoot][0] + image[i][j][0], sumDict[currRoot][1] + image[i][j][1], sumDict[currRoot][2] + image[i][j][2])
            countDict[currRoot] += 1

    # change pixel value to average
    for i in range(height):
        for j in range(width):
            #currRoot = findRoot(rootMat, (i, j))
            currRoot = rootMat[i][j]
            image[i][j][0] = sumDict[currRoot][0] // countDict[currRoot]
            image[i][j][1] = sumDict[currRoot][1] // countDict[currRoot]
            image[i][j][2] = sumDict[currRoot][2] // countDict[currRoot]

    return Image.fromarray(image)
