"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""



def first_way(companies: dict) -> list:
    """Функция принимает в себя словарь с компаниями и значениями их годовых прибылей.
    И возвращает три компании с наибольшей прибылью. Требование сортировки прибыли в ТЗ отсутствует
    PS: Можно было бы и в 1 строчку, но это совсем уже не читаемо.
    Сложность: N^2"""
    top_income = sorted(list(companies.values()), reverse=True)[:3]  # Сортировка O(log N) #Срез O(b-a)
    return [key for key, value in companies.items() if value in top_income]  # Перебор значений словаря O(n) #Проверка на входимость O(n)
