def postprocess(image, prevSize, path):
    image = image.resize((prevSize[0], prevSize[1]))
    image.show()
    image.save(path)
