import pigpen


def main():
    im = pigpen.create_ciphertext("Hello World. I am Ansel.")
    im.save("ciphertext.png")


if __name__ == "__main__":
    main()
