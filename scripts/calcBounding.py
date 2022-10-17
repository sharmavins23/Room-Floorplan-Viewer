# Given a list of points, create an SVG for me so I don't have to


class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Find the top/left bounding box offset
def findTopLeftOffset(box):
    minX = 999999
    minY = 999999

    for point in box:
        if point.x < minX:
            minX = point.x
        if point.y < minY:
            minY = point.y

    pixel = Pixel(minX, minY)

    return f"top: {minY}px, left: {minX}px", pixel


# Transform the points to be relative to the top/left
def transformPoints(box, offset):
    for point in box:
        point.x -= offset.x
        point.y -= offset.y

    return box


# Convert a box to a string of points
def boxToString(box):
    points = ""
    for point in box:
        points += f"{point.x} {point.y}, "

    return points


# Given a box, find the maximal bounding box
def findMaxBox(box):
    maxX = -999999
    maxY = -999999

    for point in box:
        if point.x > maxX:
            maxX = point.x
        if point.y > maxY:
            maxY = point.y

    # Convert this to a string
    return f"0 0 {maxX} {maxY}"


# Do the entire workflow
def convert(fun):
    box = fun()
    offset, offsetPixel = findTopLeftOffset(box)
    box = transformPoints(box, offsetPixel)
    viewbox = findMaxBox(box)
    points = boxToString(box)

    print(f"Offset: {offset}")
    print(f"Points: {points}")
    print(f"Viewbox: {viewbox}")


# ===== Hardcoded boxes ========================================================


def kitchen():
    box = [
        Pixel(65, 468),
        Pixel(472, 468),
        Pixel(472, 694),
        Pixel(607, 694),
        Pixel(607, 836),
        Pixel(480, 836),
        Pixel(480, 990),
        Pixel(65, 990)
    ]

    return box


def livingRoom():
    box = [
        Pixel(607, 990),
        Pixel(607, 694),
        Pixel(472, 694),
        Pixel(472, 234),
        Pixel(582, 121),
        Pixel(582, 61),
        Pixel(834, 61),
        Pixel(834, 121),
        Pixel(950, 235),
        Pixel(950, 290),
        Pixel(954, 290),
        Pixel(954, 898),
        Pixel(752, 898),
        Pixel(752, 990),
    ]

    return box


def balcony():
    box = [
        Pixel(120, 247),
        Pixel(459, 247),
        Pixel(459, 455),
        Pixel(120, 455)
    ]

    return box


def bathroom():
    box = [
        Pixel(766, 1123),
        Pixel(1249, 1123),
        Pixel(1249, 766),
        Pixel(1192, 766),
        Pixel(1102, 764),
        Pixel(967, 764),
        Pixel(967, 786),
        Pixel(965, 876),
        Pixel(965, 912),
        Pixel(766, 912)
    ]

    return box


def bedroom1():
    box = [
        Pixel(967, 750),
        Pixel(1102, 750),
        Pixel(1192, 752),
        Pixel(1209, 752),
        Pixel(1209, 656),
        Pixel(1540, 656),
        Pixel(1540, 290),
        Pixel(967, 290)
    ]

    return box


def bedroom2():
    box = [
        Pixel(1263, 1123),
        Pixel(1749, 1123),
        Pixel(1749, 662),
        Pixel(1552, 662),
        Pixel(1552, 669),
        Pixel(1222, 669),
        Pixel(1222, 752),
        Pixel(1263, 752),
        Pixel(1263, 785)
    ]

    return box


if __name__ == "__main__":
    convert(bedroom2)
