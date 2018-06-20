from PIL import Image, ImageDraw


def median_filter(src, dst, size=3):
    img1 = Image.open(src)
    draw = ImageDraw.Draw(img1)
    width = img1.size[0]
    height = img1.size[1]
    pix = img1.load()
    if size == 3:
        for i in range(1, width - 1):
            for j in range(1, height - 1):
                r = [pix[i,j][0], pix[i-1,j-1][0], pix[i+1,j+1][0], pix[i-1,j+1][0], pix[i+1,j-1][0], pix[i-1,j][0], pix[i+1,j][0], pix[i,j-1][0], pix[i,j+1][0]]
                g = [pix[i,j][1], pix[i-1,j-1][1], pix[i+1,j+1][1], pix[i-1,j+1][1], pix[i+1,j-1][1], pix[i-1,j][1], pix[i+1,j][1], pix[i,j-1][1], pix[i,j+1][1]]
                b = [pix[i,j][2], pix[i-1,j-1][2], pix[i+1,j+1][2], pix[i-1,j+1][2], pix[i+1,j-1][2], pix[i-1,j][2], pix[i+1,j][2], pix[i,j-1][2], pix[i,j+1][2]]
                r.sort()
                g.sort()
                b.sort()
                r = r[int(len(r) / 2)]
                g = g[int(len(g) / 2)]
                b = b[int(len(b) / 2)]
                draw.point((i, j), (r, g, b))
        img1.save(dst)
    elif size == 5:
        for i in range(2, width - 2):
            for j in range(2, height - 2):
                r = [pix[i - 2, j - 2][0], pix[i - 2, j - 1][0], pix[i - 2, j][0], pix[i - 2, j + 1][0],
                     pix[i - 2, j + 2][0],
                     pix[i - 1, j - 2][0], pix[i - 1, j - 1][0], pix[i - 1, j][0], pix[i - 1, j + 1][0],
                     pix[i - 1, j + 2][0],
                     pix[i, j - 2][0], pix[i, j - 1][0], pix[i, j][0], pix[i, j + 1][0], pix[i, j + 2][0],
                     pix[i + 1, j - 2][0], pix[i + 1, j - 1][0], pix[i + 1, j][0], pix[i + 1, j + 1][0],
                     pix[i + 1, j + 2][0],
                     pix[i + 2, j - 2][0], pix[i + 2, j - 1][0], pix[i + 2, j][0], pix[i + 2, j + 1][0],
                     pix[i + 2, j + 1][0]]

                g = [pix[i - 2, j - 2][1], pix[i - 2, j - 1][1], pix[i - 2, j][1], pix[i - 2, j + 1][1],
                     pix[i - 2, j + 2][1],
                     pix[i - 1, j - 2][1], pix[i - 1, j - 1][1], pix[i - 1, j][1], pix[i - 1, j + 1][1],
                     pix[i - 1, j + 2][1],
                     pix[i, j - 2][1], pix[i, j - 1][1], pix[i, j][1], pix[i, j + 1][1], pix[i, j + 2][1],
                     pix[i + 1, j - 2][1], pix[i + 1, j - 1][1], pix[i + 1, j][1], pix[i + 1, j + 1][1],
                     pix[i + 1, j + 2][1],
                     pix[i + 2, j - 2][1], pix[i + 2, j - 1][1], pix[i + 2, j][1], pix[i + 2, j + 1][1],
                     pix[i + 2, j + 1][1]]

                b = [pix[i - 2, j - 2][2], pix[i - 2, j - 1][2], pix[i - 2, j][2], pix[i - 2, j + 1][2],
                     pix[i - 2, j + 2][2],
                     pix[i - 1, j - 2][2], pix[i - 1, j - 1][2], pix[i - 1, j][2], pix[i - 1, j + 1][2],
                     pix[i - 1, j + 2][2],
                     pix[i, j - 2][2], pix[i, j - 1][2], pix[i, j][2], pix[i, j + 1][2], pix[i, j + 2][2],
                     pix[i + 1, j - 2][2], pix[i + 1, j - 1][2], pix[i + 1, j][2], pix[i + 1, j + 1][2],
                     pix[i + 1, j + 2][2],
                     pix[i + 2, j - 2][2], pix[i + 2, j - 1][2], pix[i + 2, j][2], pix[i + 2, j + 1][2],
                     pix[i + 2, j + 1][2]]
                r.sort()
                g.sort()
                b.sort()
                r = r[int(len(r) / 2)]
                g = g[int(len(g) / 2)]
                b = b[int(len(b) / 2)]
                draw.point((i, j), (r, g, b))
        img1.save(dst)


src = "lenaShum.jpg"
dst = "lenaShumFiltered.jpg"
median_filter(src, dst, 5)