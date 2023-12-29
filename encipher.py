import argparse
import re
import pigpen


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dest_file", help="name output file")
    parser.add_argument("-k", "--key", action="store_true", help="specify key used")
    args = parser.parse_args()
    im = pigpen.create_ciphertext(get_valid_text(), get_valid_key(args.key))
    im.save(args.dest_file + ".png", "PNG")
    print(f"Pigpen ciphertext saved to '{args.dest_file}.png'")


def get_valid_text():
    while True:
        try:
            plaintext = input("Enter plaintext (use '.' for newlines): ")
            if not plaintext.strip():
                raise ValueError("Please enter some text")
            if re.search(r"[^a-z\. ]", plaintext, re.IGNORECASE):
                raise ValueError("Please only use letters, spaces and periods")
        except ValueError as e:
            print(e)
        else:
            return plaintext


def get_valid_key(specify_key):
    template = """
       |   |         |   |   
     a | b | c     j | k | l
       |   |        •| • |•  
    ---+---+---   ---+---+---
       |   |         |   |   
     d | e | f     m•| n |•o 
       |   |         | • |   
    ---+---+---   ---+---+---
       |   |        •| • |•  
     g | h | i     p | q | r 
       |   |         |   |   
    
    \\  s /   \\  w /
     \\  /     \\ •/ 
     t\\/u    x•\\/•y
      /\\       /\\  
     /  \\     / •\\ 
    /  v \\   /  z \\
    """
    print(template)
    print("Default key: abcdefghijklmnopqrstuvwxyz")
    if not specify_key:
        return pigpen.KEY
    while True:
        try:
            key = input("Enter key: ").lower().strip()
            if not key:
                raise ValueError("Please enter the key")
            key_list = [letter for letter in key if letter in pigpen.KEY]
            if sorted(key_list) != pigpen.KEY:
                raise ValueError("Please use one of each letter")
        except ValueError as e:
            print(e)
        else:
            grid = template
            for i in range(26):
                grid = grid.replace(pigpen.KEY[i], str(i))
            for index, value in enumerate(key_list):
                grid = grid.replace(str(index), value, 1)
            print(grid)
            print(f"Entered key: {key}")
            return key_list


if __name__ == "__main__":
    main()
