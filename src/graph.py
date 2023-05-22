import numpy as np

def rgbDiff(pixel1, pixel2):
    return (pixel1[0] - pixel2[0]) ** 2 + (pixel1[1] - pixel2[1]) ** 2 + (pixel1[2] - pixel2[2]) ** 2 

def generateGraph(image, radius):
    height = image.shape[0]
    width = image.shape[1]

    edges = np.empty((), dtype=object)
    for i in range(height):
        for j in range(width):
            for r in range(radius):
                if (i >= r + 1):
                    upperIdx = (i - (r + 1), j)
                    edges.append((rgbDiff(image[i][j], image[upperIdx[0]][upperIdx[1]]), (i, j), upperIdx))

                if (j >= r + 1):
                    leftIdx = (i, j - (r + 1))
                    edges.append((rgbDiff(image[i][j], image[leftIdx[0]][leftIdx[1]]), (i, j), leftIdx))

    return image, edges