import numpy as np

def findRoot(rootMat, position, posCopy):
    temp = rootMat[position[0]][position[1]]

    if (temp == position):
        rootMat[posCopy[0]][posCopy[1]] = temp
        return temp
    else:
        return findRoot(rootMat, temp, posCopy)


def mergeRoot(rootMat, root1, root2, node2Copy):
    rootMat[root2[0]][root2[1]] = root1
    rootMat[node2Copy[0]][node2Copy[1]] = root1

def segmentation(image, edges, threshold):
    rootMat = [[(i,j) for j in range(image.shape[1])] for i in range(image.shape[0])]
    edgesCount = edges.size

    # kruskal algorithm
    edges = np.array(sorted(edges, key = lambda x: x[0]))

    i = 0
    while (i < edgesCount and edges[i][0] <= threshold):
        firstNode = (edges[i][1], edges[i][2])
        secondNode = (edges[i][3], edges[i][4])

        firstRoot = findRoot(rootMat, firstNode, firstNode)
        secondRoot = findRoot(rootMat, secondNode, secondNode)

        # find-union algorithm
        if (firstRoot != secondRoot):
            mergeRoot(rootMat, firstRoot, secondRoot, secondNode)

        i += 1

    return image, rootMat
