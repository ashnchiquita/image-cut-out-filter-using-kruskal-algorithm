from PIL import Image
import numpy as np

def preprocess(path):
    image = np.array(Image.open(path))
    return image