from PIL import Image, ImageDraw


def main():
    size = 32, 32
    im = Image.new("1", size, 1)
    draw = ImageDraw.Draw(im)
    draw_diagonal_lines(draw, "top")
    draw_straight_lines(draw, [1, 1, 1, 1])
    draw_dot(draw)
    im.save("test.png")

def draw_straight_lines(draw, positions):
    top, right, bottom, left = positions
    if top:
        draw.line((3, 4, 28, 4), width=3)
    if right:
        draw.line((27, 3, 27, 28), width=3)
    if bottom:
        draw.line((3, 27, 28, 27), width=3)
    if left:
        draw.line((4, 3, 4, 28), width=3)

def draw_diagonal_lines(draw, direction):
    match direction:
        case "top":
            draw.line((3, 28, 15, 3), width=3)
            draw.line((28, 28, 16, 3), width=3)
        case "right":
            draw.line((3, 3, 28, 15), width=3)
            draw.line((3, 28, 28, 16), width=3)
        case "bottom":
            draw.line((3, 3, 15, 28), width=3)
            draw.line((28, 3, 16, 28), width=3)
        case "left":
            draw.line((3, 15, 28, 3), width=3)
            draw.line((3, 16, 28, 28), width=3)

def draw_dot(draw):
    draw.ellipse((13, 13, 18, 18), fill=0)

if __name__ == "__main__":
    main()
