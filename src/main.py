from preprocessing import preprocess
from graph import generateGraph
from segmentation import segmentation
from cutout import cutout
from postprocessing import postprocess
from PIL import Image
import os.path
import time

def validateInput(inputPath, threshold, radius, outputPath):
    if (os.path.exists(inputPath) and (inputPath.endswith(".jpg") or inputPath.endswith(".jpeg") or inputPath.endswith(".png") or inputPath.endswith(".bmp")) and not(os.path.exists(outputPath)) and threshold > 0 and radius >= 0):
        return True
    return False

# Main Program
inputPath = input("Input Image Path : ")
outputPath = input("Output Image Path : ")
threshold = int(input("Filter Threshold : "))
radius = int(input("Edge Radius : "))

while (not(validateInput(inputPath, threshold, radius, outputPath))):
    print("Invalid input, please try again.")
    inputPath = input("Input Image Path : ")
    outputPath = input("Output Image Path : ")
    threshold = int(input("Filter Threshold : "))
    radius = int(input("Edge Radius : "))

t1 = time.time()
print("Preprocessing image...")
preprocessed, prevSize = preprocess(inputPath)
print("Image preprocessing is done. Generating graph...")

graphImage, edges = generateGraph(preprocessed, radius)
print("Graph generated succesfully. Segmenting image...")
segmented, rootMat = segmentation(graphImage, edges, threshold)
print("Image segmented. Applying cut out filter...")
filtered = cutout(segmented, rootMat)
print("Cut out filter applied. Saving image...")
postprocess(filtered, prevSize, outputPath)
t1 = (time.time() - t1)
print("All done in", t1, "s!!")
