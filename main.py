import sys
from PIL import Image, ImageDraw


def getImageInfo(path):
    ogImage = Image.open(path)
    imWidth, imHeight = ogImage.size
    print(f"{imWidth} x {imHeight}")
    checkSize(ogImage, imWidth, imHeight)


def checkSize(image, width, height):
    pixels = image.load()
    countX = 0  # same color pixel
    cooX = 0  # last color change
    unitX = width  # smallest horizontal unit
    countY = 0
    cooY = 0
    unitY = height  # smallest vertical unit
    unit = 0

    print("rgb values left to right")
    #look for color change and calculate unit size by distance
    for x, i in zip(range(width), range(height)):
        if pixels[cooX, i] != pixels[x, i]:
            if countX < unitX:
                unitX = countX
            cooX = x
            countX = 1
        else:
            countX += 1
        print(f"{cooX} | {countX}")

    print("rgb values top to bottom")
    for y, i in zip(range(width), range(height)):
        if pixels[i, cooY] != pixels[i, y]:
            if countY < unitY:
                unitY = countY
            cooY = y
            countY = 1
        else:
            countY += 1
        print(f"{cooY} | {countY}")

    if unitX > unitY:
        unit = unitY
    elif unitX < unitY:
        unit = unitX
    elif unitX > 1 and unitY > 1 and unitX == unitY:
        unit = unitX
    elif unitX == 1 or unitY == 1:
        print("Pixel art not detected!")
        sys.exit(0)
    else:
        print("Pixel art not detected!")
        sys.exit(0)

    print(f"\nOG Size\nWidth: {width}\tHeight: {height}\n"
          f"CalcSize:\nWidth: {cooX + countX}\tHeight: {cooY + countY}\n"
          f"Smallest unit size:\nHorizontal: {unitX}\tVertical: {unitY}\n"
          f"Pixel size: {unit}")

    pencil = ImageDraw.Draw(image)
    for x in range(0, width, unit):
        pencil.line((x, 0, x, height), fill="black")
    for y in range(0, height, unit):
        pencil.line((0, y, width, y), fill="black")
    image.save("out.png")
    print("Image saved!")


if __name__ == '__main__':
    print("Drag&Drop an image from your pc!")
    path = input()
    getImageInfo(path)
