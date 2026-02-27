from PIL import Image
import numpy as np

def magnification_animation():
    bright = Image.open("cell_bright_30.png")

    bg = Image.new(bright.mode, (300, 300), 0)

    for i in range(10, 310, 10):
        bg.paste(bright.resize((i, i)), (0, 0))
        bg.save(f"cell_bright_size_{i}.png")

def resolution_animation():
    bright = np.array(Image.open("cell_bright.png"))

    for i in range(1, 31):
        Image.fromarray(bright[::i, ::i]).resize((300, 300), Image.NEAREST).save(f"cell_bright_{i}.png")

if __name__ == "__main__":
    resolution_animation()