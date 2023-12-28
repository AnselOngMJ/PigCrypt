from PIL import Image, ImageDraw


LINES = {
    "top": list(range(3, 9)) + list(range(12, 18)),
    "right": [0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16],
    "bottom": list(range(6)) + list(range(9, 15)),
    "left": [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17],
}
ARROWS = {
    "top": [21, 25],
    "right": [19, 23],
    "bottom": [18, 22],
    "left": [20, 24],
}
DOTS = list(range(9, 18)) + list(range(22, 26))
ALPHABET = [chr(i) for i in range(97, 123)]


def main():
    im = create_ciphertext("hello world. i am ansel.")
    im.save("ciphertext.png")


def create_ciphertext(plaintext):
    lines = [line.strip() for line in plaintext.split(".")]
    if "" in lines:
        lines.remove("")
    size = max([len(line) for line in lines]) * 32, len(lines) * 32
    im = Image.new("1", size, 1)
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            im.paste(draw_character(character), (x * 32, y * 32))
    return im


def draw_character(character):
    size = 32, 32
    im = Image.new("1", size, 1)
    draw = ImageDraw.Draw(im)
    if character == " ":
        return im
    letter = ALPHABET.index(character)
    if letter < 18:
        for key, value in LINES.items():
            if letter in value:
                draw_line(draw, key)
    else:
        for key, value in ARROWS.items():
            if letter in value:
                draw_arrows(draw, key)
                break
    if letter in DOTS:
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
