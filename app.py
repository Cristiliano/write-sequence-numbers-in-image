from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

words = [i for i in range(1, 4)]

cont = 1

for word in words:
    str_word = ''
    if(word < 10):
        str_word = '00' + str(word)
    elif(word >= 10 and word < 100):
        str_word = '0' + str(word)
    else:
        str_word = str(word)

    img = Image.open('images/great_background_img.jpg')
    draw = ImageDraw.Draw(img)
    fonte = ImageFont.truetype('fonts/ARLRDBD.TTF', 120)
    draw.text((1020,540), str(str_word), font=fonte, fill='Yellow', stroke_width=8, stroke_fill='black')
    img.save(f'images/img_{cont}.jpg')
    cont += 1
