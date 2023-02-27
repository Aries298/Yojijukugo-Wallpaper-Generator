import random

from wallpaper_settings import _wallpaper_parameters
from PIL import Image, ImageDraw
from colorlovers import get_random_pallet
from draw_shapes import draw_circle, concentric_circles, square45, hexagon
from rest import gennum

def gen_circle_random():
    wallpaper_width = _wallpaper_parameters['wallpaper_width']
    wallpaper_height = _wallpaper_parameters['wallpaper_height']
    scale_factor = 4  # Resize scaling for antialiasing
    img_size = (wallpaper_width, wallpaper_height)  # Final image size desired

    img_size_scaled = tuple(x * scale_factor for x in img_size)

    img = Image.new("RGB", img_size_scaled)
    ic = ImageDraw.Draw(img, "RGBA")  # Specified RGBA

    pallet = get_random_pallet()  # Getting a top pallet

    step = 120 * scale_factor

    randnum = gennum()
    for i in range(16 + 2):
        for j in range(9 + 2):
            draw_circle(
                ic,
                step * i, step * j,
                step + randnum,
                f"#{pallet[i % len(pallet)]}66"  # Opacity set at 66 (in hex)
            )

    img = img.resize(img_size, resample=Image.LANCZOS)
    return img

def gen_random_concentric():
    wallpaper_width = _wallpaper_parameters['wallpaper_width']
    wallpaper_height = _wallpaper_parameters['wallpaper_height']
    scale_factor = 4  # Resize scaling for antialiasing
    img_size = (wallpaper_width, wallpaper_height)  # Final image size desired

    img_size_scaled = tuple(x * scale_factor for x in img_size)

    img = Image.new("RGB", img_size_scaled)
    ic = ImageDraw.Draw(img, "RGBA")  # Specified RGBA

    pallet = get_random_pallet()  # Getting a top pallet

    step = 120 * scale_factor

    randnum = gennum()
    randopa = random.randint(10,30)
    randcircles = random.randint(2,10)

    for i in range(16 + 2):
        for j in range(9 + 2):
            concentric_circles(
                ic,
                step * i, step * j,
                step + randnum,
                randcircles,
                f"#{pallet[i % len(pallet)]}66",
                randopa
            )
    img = img.resize(img_size, resample=Image.LANCZOS)
    return img

def gen_square45():
    wallpaper_width = _wallpaper_parameters['wallpaper_width']
    wallpaper_height = _wallpaper_parameters['wallpaper_height']
    scale_factor = 4  # Resize scaling for antialiasing
    img_size = (wallpaper_width, wallpaper_height)  # Final image size desired

    img_size_scaled = tuple(x * scale_factor for x in img_size)

    img = Image.new("RGB", img_size_scaled)
    ic = ImageDraw.Draw(img, "RGBA")  # Specified RGBA

    pallet = get_random_pallet()  # Getting a top pallet

    step = 120 * scale_factor

    multip = random.randint(1,5)
    for i in range(16*multip + 2):
        for j in range(9*multip + 2):
            square45(
                ic,
                step // multip * i, step // multip * j,
                step * multip * 2,
                f"#{pallet[i % len(pallet)]}66"
            )

    img = img.resize(img_size, resample=Image.LANCZOS)
    return img

def gen_hexagon():
    wallpaper_width = _wallpaper_parameters['wallpaper_width']
    wallpaper_height = _wallpaper_parameters['wallpaper_height']
    scale_factor = 4  # Resize scaling for antialiasing
    img_size = (wallpaper_width, wallpaper_height)  # Final image size desired

    img_size_scaled = tuple(x * scale_factor for x in img_size)

    img = Image.new("RGB", img_size_scaled)
    ic = ImageDraw.Draw(img, "RGBA")  # Specified RGBA

    pallet = get_random_pallet()  # Getting a top pallet

    step = 120 * scale_factor




    for i in range(16*2 + 2):
        for j in range(9*2 + 2):
            #print(((i%2)*step)//2)
            hexagon(
                ic,
                #step * i + ((i%2)*step)//2, step * j + ((j%2)*step)//2,
                step * i + step//2, step * j,
                int(step*0.5),
                f"#{pallet[i % len(pallet)]}66"
            )

    for i in range(16*2 + 2):
        for j in range(9*2 + 2):
            hexagon(
                ic,
                step * i , step * j+ step//2,
                int(step*0.5),
                f"#{pallet[i % len(pallet)]}66"
            )

    for i in range(16*2 + 2):
        for j in range(9*2 + 2):
            hexagon(
                ic,
                step * i, step * j,
                int(step*0.75),
                f"#{pallet[i % len(pallet)]}66"
            )

    for i in range(16*2 + 2):
        for j in range(9*2 + 2):
            hexagon(
                ic,
                step * i + step//2, step * j + step//2,
                int(step*0.75),
                f"#{pallet[i % len(pallet)]}66"
            )

    img = img.resize(img_size, resample=Image.LANCZOS)
    return img