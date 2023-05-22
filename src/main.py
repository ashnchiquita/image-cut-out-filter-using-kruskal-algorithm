from PIL import Image
from preprocessing import preprocess
from graph import generateGraph
from segmentation import segmentation
from cutout import cutout

def validateInput(path, threshold, radius):
    return True

# Main Program
inputPath = input("Input Image Path : ")
outputPath = input("Output Image Path : ")
threshold = int(input("Filter Threshold : "))
radius = int(input("Edge Radius : "))

while (not(validateInput(inputPath, threshold, radius))):
    print("Invalid input, please try again.")
    inputPath = input("Input Image Path : ")
    outputPath = input("Output Image Path : ")
    threshold = int(input("Filter Threshold : "))
    radius = int(input("Edge Radius : "))

print("Preprocessing image...")
preprocessed = preprocess(inputPath)
print("Image preprocessing is done. Generating graph...")
graphImage = generateGraph(preprocessed, radius)
print("Graph generated succesfully. Segmenting image...")
segmented = segmentation(graphImage, threshold)
print("Image segmented. Applying cut out filter...")
filtered = cutout(segmented)
print("Cut out filter applied. Saving image...")
# save
print("All done!")