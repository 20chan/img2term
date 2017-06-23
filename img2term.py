from PIL import Image

def rgb2ansi(r, g, b):
    '''
    r, g, b should be 0 ~ 5
    '''
    # r, g, b = r // 51, g // 51, b // 51
    return 16 + 36 * r + 6 * g + b

def point2ansi(r, g, b, dr, dg, db):
    return '\x1b[48;5;{}m\x1b[38;5;{}m▄'.format(rgb2ansi(r, g, b), rgb2ansi(dr, dg, db))

def img2code(img):
    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    res = ''
    for y in range(0, height // 2, 2):
        for x in range(0, width // 2, 2):
            r, g, b = pixels[2*y][2*x]
            r, g, b = r // 51, g // 51, b // 51

            dr, dg, db = pixels[2*y+1][2*x]
            dr, dg, db = dr // 51, dg // 51, db // 51
            res += point2ansi(r, g, b, dr, dg, db)
        res += '\n'
    return res

def test():
    img = Image.open('cat.jpg')
    img.thumbnail((img.size[0] // 3, img.size[1] // 3))
    open('cat', 'w+').write(img2code(img))

if __name__ == '__main__':
    test()
