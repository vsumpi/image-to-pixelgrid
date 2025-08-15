from PIL import Image, ImageDraw

def getImageInfo(path):
    ogImage = Image.open(path)
    imWidth,imHeight = ogImage.size
    print(f"{imWidth} x {imHeight}")
    pixels = ogImage.load()
    print("rgb values top to bottom")
    countX = 0
    cooX = 0
    unitX = imWidth
    countY = 0
    cooY = 0
    unitY = imHeight
    unit = 0

    print("rgb values left to right")
    for i in range(imWidth):
        #print(pixels[i,0])
        if pixels[cooX,0] != pixels[i,0]:
            if countX < unitX:
                unitX = countX
            cooX = i
            countX = 1
        else:
            countX+=1
        print(f"{cooX} | {countX}")
    
    for i in range(imHeight):
        #print(pixels[0,i])
        if pixels[0,cooY] != pixels[0,i]:
            if countY < unitY:
                unitY = countY
            cooY = i
            countY = 1
        else:
            countY+=1
        print(f"{cooY} | {countY}")
    if unitX > unitY:
        unit = unitY
    else:
        unit = unitX
        
    print(f"\nOG Size\nWidth: {imWidth}\tHeight: {imHeight}\nCalcSize:\nWidth: {cooX+countX}\tHeight: {cooY+countY}\nSmallest unit size:\nHorizontal: {unitX}\tVertical: {unitY}\nPixel size: {unit}")
    
    pencil = ImageDraw.Draw(ogImage)
    for x in range(0, imWidth, unit):
        pencil.line((x, 0, x, imHeight), fill="black")
    for y in range(0, imHeight, unit):
        pencil.line((0, y, imWidth, y), fill="black")
    ogImage.save("out.jpg")
    

if __name__ == '__main__':
    print("Drag&Drop an image from your pc!")
    path = input()
    getImageInfo(path)