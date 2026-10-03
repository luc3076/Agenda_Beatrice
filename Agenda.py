from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

WIDTH = 300
HEIGHT = 400

image = Image.new("1", (WIDTH, HEIGHT), 255)
draw = ImageDraw.Draw(image)

font_big = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42
)
font_small = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24
)

now = datetime.now()

draw.text((20, 25), "Agenda Beatrice", font=font_small, fill=0)
draw.line((20, 65, 380, 65), fill=0, width=2)
draw.text((20, 95), now.strftime("%H:%M"), font=font_big, fill=0)
draw.text((20, 160), now.strftime("%A, %d.%m.%Y"), font=font_small, fill=0)
draw.text((20, 230), "Display-Test_2", font=font_small, fill=0)

image.save("/home/luc/Cloud_RPI/pic/4in2.bmp")
print("Bild erstellt: /home/luc/Cloud_RPI/pic/4in2.bmp")
