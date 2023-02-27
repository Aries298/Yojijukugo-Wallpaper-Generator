def draw_circle(ic, x, y, r, color):
    x, y, r = int(x), int(y), int(r)
    ic.ellipse([x - r, y - r, x + r, y + r], fill=color)

def concentric_circles(ic, x, y, max_r, circle_count, color, max_opacity):
    for i in range(circle_count):
        draw_circle(
            ic,
            x, y,
            int(max_r * (circle_count - i) / circle_count),
            f"{color[:-2]}{max_opacity}"
        )

def square45(ic, x, y, size, color):
    x, y, size = int(x), int(y), int(size)
    halfsize = size // 2
    points = ((x-halfsize,y),(x,y+halfsize),(x+halfsize,y),(x,y-halfsize))
    ic.polygon(points, fill=color)

def hexagon(ic, x, y, size, color):
    x, y, size = int(x), int(y), int(size)
    halfsize = size // 2
    quartersize = size // 4
    points = ((x-halfsize,y),(x-quartersize,y+halfsize),(x+quartersize,y+halfsize),(x+halfsize,y),(x+quartersize,y-halfsize),(x-quartersize,y-halfsize))
    ic.polygon(points, fill=color)