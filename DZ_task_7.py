def polindrom(string):
    ll = list(string)
    ll_w = ""
    word_w = ""

    while True: # убираем пробелы
        if " " in ll:
            ll.remove(" ")
        else:
            break

    word = ll.copy()
    word.reverse()

    for i in ll: # превращаем списки в слова
        ll_w += i
    for i in word:
        word_w += i

    if word_w == ll_w:
        print("это полиндром!")
    else:
        print("Не полиндром!")


polindrom("молоко делили ледоколом")