def findRoot(rootMat, position):
    i = position[0]
    j = position[1]
    temp = rootMat[i][j]

    if (temp[i] != i and temp[j] != j):
        return findRoot(rootMat, temp[i], temp[j])
    
    return temp

def mergeRoot(rootMat, root1, root2):
    firstRoot = findRoot(rootMat, root1)
    secondRoot = findRoot(rootMat, root2)
    rootMat[secondRoot[0]][secondRoot[1]] = firstRoot

def rgbDiff(pixel1, pixel2):
    return (pixel1[0] - pixel2[0]) ** 2 + (pixel1[1] - pixel2[1]) ** 2 + (pixel1[2] - pixel2[2]) ** 2 

def segmentation(image, edges, threshold):
    rootMat = []
    rootMat
    edgesCount = edges.size
    edges = sorted
    i = 0
    while (i < edgesCount and edges[i][0] <= threshold):
        firstNode = edges[i][1]
        secondNode = edges[i][2]

        if (findRoot(rootMat, firstNode) != findRoot(rootMat, secondNode)):
            mergeRoot(rootMat, firstNode, secondNode)

        i += 1
    
    return image, rootMat