from xml.etree import ElementTree as et
import random

def get_random_pallet():
    with open('C:/Users/Admin/Desktop/Programowanie/Yojijukugo Wallpaper Generator/palettes.txt', 'r') as file:
        data = file.read().replace('\n', '')

    pallets = et.fromstring(data)
    randint = random.randint(0,19)

    # Getting the hex tags from a given pallet
    hex_elems = pallets[randint].iter('hex')

    return [c.text for c in hex_elems]