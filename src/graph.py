import numpy as np
import math

def rgbDiff(pixel1, pixel2):
    pixel1Int = (int(pixel1[0]), int(pixel1[1]), int(pixel1[2]))
    pixel2Int = (int(pixel2[0]), int(pixel2[1]), int(pixel2[2]))
    return (pixel1Int[0] - pixel2Int[0]) ** 2 + (pixel1Int[1] - pixel2Int[1]) ** 2 + (pixel1Int[2] - pixel2Int[2]) ** 2

def generateGraph(image, radius):
    height = image.shape[0]
    width = image.shape[1]

    edges = np.zeros(height * width * radius * 2, 'int32, int32, int32, int32, int32')
    edgeCount = 0

    for i in range(height):
        for j in range(width):
            for r in range(radius):
                if (i >= r + 1):
                    upperIdx = (i - (r + 1), j)
                    edges[edgeCount] = (rgbDiff(image[i][j], image[upperIdx[0]][upperIdx[1]]), i, j, upperIdx[0], upperIdx[1])
                    edgeCount += 1
                    # edges.append((colorDist(image[i][j], image[upperIdx[0]][upperIdx[1]]), (i, j), upperIdx))

                if (j >= r + 1):
                    leftIdx = (i, j - (r + 1))
                    edges[edgeCount] = (rgbDiff(image[i][j], image[leftIdx[0]][leftIdx[1]]), i, j, leftIdx[0], leftIdx[1])
                    edgeCount += 1
                    # edges.append((colorDist(image[i][j], image[leftIdx[0]][leftIdx[1]]), (i, j), leftIdx))

    return image, np.resize(edges, edgeCount)
