from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")
top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")
print(top_text, bottom_text)

print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")
image_number = int(input("Введите номер картинки: "))
image_file = ""

if image_number == 1:
    image_file = "images/cat_in_restaurant.png"
elif image_number == 2:
    image_file = "images/cat_in_glasses.png"
print(image_file)

image = Image.open(image_file)
width, height = image.size
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size=70)

text_size = draw.textbbox((0, 0), top_text, font)
text_width = text_size[2]

draw.text(((width - text_width) / 2, 10), top_text, font=font, fill="blue")

text_size = draw.textbbox((0, 0), bottom_text, font)
text_width = text_size[2]
text_height = text_size[3]

#draw.text((0, 0), top_text, font=font, fill="blue")
#draw.text((0, 100), bottom_text, font=font, fill="blue")

draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill="blue")

image.save("meme.jpg")