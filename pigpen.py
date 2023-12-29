from PIL import Image, ImageDraw


CHARACTER_SIZE = 64
ALPHABET = [chr(i) for i in range(97, 123)]
DOTS = set(range(9, 18)).union(set(range(22, 26)))
ARROWS = {
    "top": {21, 25},
    "right": {19, 23},
    "bottom": {18, 22},
    "left": {20, 24},
}
LINES = {
    "top": set(range(3, 9)).union(set((range(12, 18)))),
    "right": {0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16},
    "bottom": set(range(6)).union(set(range(9, 15))),
    "left": {1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17},
}
POSITIONS_TO_ANGLES = {
    "top": 0,
    "right": -90,
    "bottom": 180,
    "left": 90,
}


def create_ciphertext(plaintext, alphabet=ALPHABET):
    lines = [line.strip().lower() for line in plaintext.split(".")]
    lines.remove("") if "" in lines else None
    size = (
        max([len(line) for line in lines]) * CHARACTER_SIZE,
        len(lines) * CHARACTER_SIZE,
    )
    im = Image.new("RGBA", size, (255, 255, 255, 255))
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            im.alpha_composite(
                draw_character(character, alphabet),
                (x * CHARACTER_SIZE, y * CHARACTER_SIZE),
            )
    return im


def draw_character(character, alphabet):
    size = CHARACTER_SIZE, CHARACTER_SIZE
    im = Image.new("RGBA", size)
    if character == " ":
        return im
    letter = alphabet.index(character)
    if letter in DOTS:
        im = draw_element(im, "dot")
    if letter > 17:
        for key, value in ARROWS.items():
            if letter in value:
                im = draw_element(im, "arrow", POSITIONS_TO_ANGLES[key])
                break
    else:
        for key, value in LINES.items():
            if letter in value:
                im = draw_element(im, "line", POSITIONS_TO_ANGLES[key])
    return im


def draw_element(im, element, angle=0):
    element_im = Image.new("RGBA", im.size)
    draw = ImageDraw.Draw(element_im)
    black = (0, 0, 0, 255)
    match element:
        case "dot":
            draw.ellipse((27, 27, 36, 36), fill=black)
        case "arrow":
            draw.line((4, 60, 32, 4), fill=black, width=5)
            draw.line((59, 60, 31, 4), fill=black, width=5)
            draw.rectangle((31, 2, 32, 3), fill=black)
        case "line":
            draw.line((2, 4, 61, 4), fill=black, width=5)
    element_im = element_im.rotate(angle)
    im.alpha_composite(element_im)
    return im
