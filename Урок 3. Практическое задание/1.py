import csv

# сначала запишем файл 'names.csv', который
# потом прочитаем как список словарей
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
# 13
# 13
# 16
#
# читаем CSV файл как список словарей, ключи
# которого заданы первой строкой файла 'names.csv'
with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])

# Eric Idle
# John Cleese
# >>> print(row)
# {'first_name': 'John', 'last_name': 'Cleese'}