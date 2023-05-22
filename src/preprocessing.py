from PIL import Image, ImageFilter
import numpy as np

def preprocess(path):
    image = Image.open(path)

    # smoothing filter
    # image = image.filter(ImageFilter.SMOOTH_MORE)
    prevSize = image.size
    sizeThreshold = 500

    # resize if too big
    if (prevSize[0] > sizeThreshold or prevSize[1] > sizeThreshold):
        factor = max(prevSize[0]/sizeThreshold, prevSize[1]/sizeThreshold)
        image = image.resize((round(prevSize[0]/factor), round(prevSize[1]/factor)))

    imageMat = np.array(image)
    return imageMat, prevSize
