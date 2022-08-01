import textwrap
from PIL import Image, ImageDraw, ImageFont
 
def createImage(text, name):
    font = ImageFont.truetype("./fonts/Noto_Sans/NotoSans-Medium.ttf", 24)
    img = Image.new('RGB', (500, 300), color = (255, 255, 255))
    d = ImageDraw.Draw(img)

    margin = offset = 20
    for line in textwrap.wrap(text, width=35):
        d.text((margin, offset), line, font=font, fill="#000000")
        offset += font.getsize(line)[1]

    img.save(f"./images/{name}.png")