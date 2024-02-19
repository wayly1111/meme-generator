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
