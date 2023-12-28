from PIL import Image, ImageDraw


def main():
    im = create_ciphertext("hello world. i am ansel.")
    im.save("ciphertext.png")

def create_ciphertext(text):
    lines = [line.strip() for line in text.split(".")]
    if "" in lines:
        lines.remove("")
    size = max([len(line) for line in lines]) * 32, len(lines) * 32
    im = Image.new("1", size, 1)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            im.paste(draw_character(c), (x * 32, y * 32))
    return im

def draw_character(c):
    size = 32, 32
    im = Image.new("1", size, 1)
    draw = ImageDraw.Draw(im)
    letters = [chr(i) for i in range(97, 123)]
    lines = {
        "top_line": list(range(3, 9)) + list(range(12, 18)),
        "right_line": [0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16],
        "bottom_line": list(range(6)) + list(range(9, 15)),
        "left_line": [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17],
    }
    arrows = {
        "top_arrow": [21, 25],
        "right_arrow": [19, 23],
        "bottom_arrow": [18, 22],
        "left_arrow": [20, 24],
    }
    dot = list(range(9, 18)) + list(range(22, 26))
    if c == " ":
        return im
    letter = letters.index(c)
    if letter < 18:
        for key, value in lines.items():
            if letter in value:
                draw_line(draw, key.removesuffix("_line"))
    else:
        for key, value in arrows.items():
            if letter in value:
                draw_arrows(draw, key.removesuffix("_arrow"))
                break
    if letter in dot:
        draw_dot(draw)
    return im

def draw_line(draw, position):
    match position:
        case "top":
            draw.line((3, 4, 28, 4), width=3)
        case "right":
            draw.line((27, 3, 27, 28), width=3)
        case "bottom":
            draw.line((3, 27, 28, 27), width=3)
        case "left":
            draw.line((4, 3, 4, 28), width=3)

def draw_arrows(draw, direction):
    match direction:
        case "top":
            draw.line((3, 28, 15, 3), width=3)
            draw.line((28, 28, 16, 3), width=3)
        case "right":
            draw.line((4, 3, 28, 15), width=3)
            draw.line((4, 28, 28, 16), width=3)
        case "bottom":
            draw.line((3, 3, 15, 28), width=3)
            draw.line((28, 3, 16, 28), width=3)
        case "left":
            draw.line((3, 15, 27, 3), width=3)
            draw.line((3, 16, 27, 28), width=3)

def draw_dot(draw):
    draw.ellipse((13, 13, 18, 18), fill=0)

if __name__ == "__main__":
    main()
