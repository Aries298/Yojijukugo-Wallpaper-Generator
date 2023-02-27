from PIL import ImageFont
import ctypes
from wallpaper_settings import _wallpaper_parameters
from os.path import exists
import random
import csv
import textwrap
from PIL import Image, ImageDraw
import inspect
import patterns

'''
Getting list of available patterns

AVAILABLE PATTERNS
Eectangles with gradient
Triangles with gradient
Cells
Ferns
Circles
'''
name_func_tuples = inspect.getmembers(patterns, inspect.isfunction)
name_func_tuples = [t[1] for t in name_func_tuples if inspect.getmodule(t[1]) == patterns]
PATTERNS = tuple(name_func_tuples)

# Directory where created wallpapers are being kept
WALLPAPER_FOLDER = 'wallpapers'

# Read the csv file and gets a random yojijukugo
def get_random_entry():
    with open('C:/Users/Admin/Desktop/Programowanie/Yojijukugo Wallpaper Generator/Yojijukugo List.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        data = list(csv_reader)
        entry = random.choice(data)
    return entry

# Generated random background with a randomly chosen pattern
def gen_background():
    img = random.choice(PATTERNS)()
    return img

def gen_kanji():
    pass


def gen_wallpaper(entry):
    # Read the data from the entry
    kanji, furigana, definition = entry
    # Prepare the background
    img = gen_background()

    # Set the generated image parameters
    kanji_size = _wallpaper_parameters['kanji_size']
    kanji_pos_x = _wallpaper_parameters['kanji_pos_x']
    kanji_pos_y = _wallpaper_parameters['kanji_pos_y']
    furigana_size = _wallpaper_parameters['furigana_size']
    furigana_pos_x = _wallpaper_parameters['furigana_pos_x']
    furigana_pos_y = _wallpaper_parameters['furigana_pos_y']
    definition_size = _wallpaper_parameters['definition_size']
    definition_offset = _wallpaper_parameters['definition_offset']
    definition_width = _wallpaper_parameters['definition_width']
    definition_pos_x = _wallpaper_parameters['definition_pos_x']
    definition_pos_y = _wallpaper_parameters['definition_pos_y']

    # Create a PIL Image object, draw a background
    draw = ImageDraw.Draw(img)

    # Drawing kanji
    kanji_font_file = 'C:/Users/Admin/Desktop/Programowanie/Yojijukugo Wallpaper Generator/fonts/GenEiLateGo.otf'
    kanji_font = ImageFont.truetype(kanji_font_file, kanji_size)
    offsets = [x // 2 for x in kanji_font.getbbox(kanji)]
    draw.text((kanji_pos_x - offsets[2], kanji_pos_y - offsets[3]), kanji, font=kanji_font, stroke_width=1, stroke_fill='black')

    # Drawing furigana
    furigana_font = ImageFont.truetype(kanji_font_file, furigana_size)
    offsets = [x // 2 for x in furigana_font.getbbox(furigana)]
    draw.text((furigana_pos_x - offsets[2], furigana_pos_y - offsets[3]), furigana, font=furigana_font, stroke_width=1, stroke_fill='black')

    # Drawing definition
    definition_font = ImageFont.truetype(kanji_font_file, definition_size)
    lines = textwrap.wrap(definition, definition_width)

    # Text wrapping
    for i, line in enumerate(lines):
        offset = definition_font.getbbox(line)[2] // 2
        draw.text((definition_pos_x - offset, definition_pos_y + i * definition_size), line, font=definition_font, stroke_width=1, stroke_fill='black')


    number = 1
    wallpaper_name = u"wallpaper_%s_%04d.png" % (kanji, number)
    while(exists(f'C:/Users/Admin/Desktop/Programowanie/Yojijukugo Wallpaper Generator/wallpapers/{wallpaper_name}')):
        number += 1
        wallpaper_name = u"wallpaper_%s_%04d.png" % (kanji, number)

    img.save(f'C:/Users/Admin/Desktop/Programowanie/Yojijukugo Wallpaper Generator/wallpapers/{wallpaper_name}', "PNG")
    full_path = f'C:/Users/Admin/Desktop/Programowanie/Yojijukugo Wallpaper Generator/wallpapers/{wallpaper_name}'
    return full_path

def set_wallpaper():
    entry = get_random_entry()
    path = gen_wallpaper(entry)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 1)

def run():
    set_wallpaper()

if __name__ == '__main__':
    run()
