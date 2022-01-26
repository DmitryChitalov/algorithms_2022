

base_сompany = {
    'yandex': 2000,
    'gazprom': 500,
    'microsoft': 2300,
    'perecrestok': 5400,
    'rosnano': 10,
    'appel': 2000,
    'biocad': 4030,
    'apteka': 299,
    'hiomi': 569,
    'wacom': 8901,
    'adidas': 4313,
    'acron': 6703
}


# первый вариант - O(N^2)
def sorted_1(base_сompany):
    list_from_dict = list(base_сompany.items())
    for i in range(len(list_from_dict)):
        lowest_value_index = i
        for j in range(i + 1, len(list_from_dict)):
            if list_from_dict[j][1] > \
                    list_from_dict[lowest_value_index][1]:
                lowest_value_index = j
        list_from_dict[i], list_from_dict[lowest_value_index] =\
            list_from_dict[lowest_value_index], list_from_dict[i]
    print(list_from_dict[0:3])


# второй вариант - O(N*logN)
def sorted_2(base_сompany):
    list_from_dict = list(base_сompany.items())
    list_from_dict.sort(key=lambda i: i[1], reverse=True)
    for i in range(3):
        print(f"{list_from_dict[i][0]}: {list_from_dict[i][1]}")


# третий вариант - O(N)
def sorted_3(base_сompany):
    input_max = {}
    list_d = dict(base_сompany)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    print(input_max)


sorted_1(base_сompany)
sorted_2(base_сompany)
sorted_3(base_сompany)


"""
Лучшим вариантом будет третий, т.к. имеет минимальную вычислительную 
сложность и решает поставленную задачу без изменение исходного словаря 
и без лишней сортировки
"""
