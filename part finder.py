import webbrowser


replace_list = [" ", "-", "/", "\\", "(", ")", "[", "]", ",", "."]
while True:
    print("Введите партномер или позиционное обозначение. Пустое поле для завершения")
    number = input()
    for n in replace_list:
        number = number.replace(n, "")
    if number == "":
        break
    print("\n" + number)
    webbrowser.open_new_tab("https://www.google.com/search?q=" + number)
                                        # F L 02L 20 HT-1TR