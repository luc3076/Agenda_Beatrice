import locale
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

locale.setlocale(locale.LC_TIME, "de_DE.utf8")


def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = " ".join(current_line + [word])
        if draw.textlength(test_line, font=font) <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]

    if current_line:
        lines.append(" ".join(current_line))

    return "\n".join(lines)


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

wochenplan = {
    0: "Heute 09:00 Altersheim treff", #Montag
    1: "Heute 10:00 Claudia Zmittag", #Dienstag
    2: "Heute Keine Termine", #Mittwoch
    3: "Heute 17:00 Znacht bei Reto", #Donnerstag
    4: "Heute Keine Termine", #Freitag
    5: "Heute 09:00 kommt Reto vorbei", #Samstag
    6: "Heute 12:00 Zmittag mit Luc", #Sonntag
}

heutiger_text = wochenplan.get(now.weekday(), "Keine Termine")
heutiger_text = wrap_text(heutiger_text, font_big, 260, draw)

draw.text((20, 25), "Agenda Béatrice", font=font_small, fill=0)
draw.line((20, 65, 280, 65), fill=0, width=2)
draw.text((20, 95), now.strftime("%A"), font=font_small, fill=0)
draw.text((20, 130), now.strftime("%d.%m.%Y"), font=font_big, fill=0)
draw.multiline_text((20, 210), heutiger_text, font=font_small, fill=0, spacing=6)

image.save("/home/luc/Cloud_RPI/pic/4in2.bmp")
print("Bild erstellt: /home/luc/Cloud_RPI/pic/4in2.bmp")
