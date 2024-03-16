import csv


def read(path):
    """Считывает данные из файла.
    path – путь к файлу с данными
    """
    file = open(path, encoding="utf-8")
    reader = csv.reader(file, delimiter="№")

    data = []
    for row in reader:
        data.append(row)

    return data
def write(data, path):
    """Записывает данные в csv файл.
    data – таблица с данными
    path – путь к файлу для записи
    """
    file = open(path, "w", encoding="utf-8", newline="")
    writer = csv.writer(file, delimiter="№")

    for row in data:
        writer.writerow(row)

def problem1(data):
    """Cчитает количество необходимых трав, записывает данные о них в файл "magicaPotions.csv".
    data – таблица с данными
    """
    herbs = {}
    total = 0

    for i in range(1, len(data)):
        if data[i][1] == "-1":
            for j in range(2, 5):
                if data[i][j] in herbs:
                    herbs[data[i][j]] += 1
                else:
                    herbs[data[i][j]] = 1
                total += 1

    herbs_data = [["magic_herbs", "count_herbs"]]
    for herb in herbs:
        herbs_data.append([herb, str(herbs[herb])])
    write(herbs_data, "magicaPotions.csv")

    print(f"Общее кол-во всех трав {total}")
def problem2(data):
    """Сортирует данные таблицы в лексикографическом порядке по названию зелий с помощью алгоритма сортировки пузырьком. Выводит информацию о первых трех зельях, содержащих иван-чай.
    data – таблица с данными
    """
    for i in range(len(data)-1, 0, -1):
        for j in range(0, i-1):
            if data[j][0] > data[j+1][0]:
                data[j], data[j+1] = data[j+1], data[j]

    ivan_chai = []
    for i in range(1, len(data)):
        if "Иван-чай" in data[i][2:5]:
            ivan_chai.append(data[i])

    for i in range(3):
        print(f"Зелье {ivan_chai[i][0]} имеет в своем составе иван-чай")
def problem3(data):
    """Осуществляет интерактивный поиск по таблице: при запросе по названию травы выводит зелье, содержащее ее, с самым маленьким количеством в аптеках.
    data – таблица с данными
    """
    while True:
        herb = input()
        if herb == "стоп":
            break

        potion = None
        count = None

        for i in range(1, len(data)):
            if data[i][2] == herb:
                if (count == None or int(data[i][1]) < count) and int(data[i][1]) != -1:
                    potion = data[i][0]
                    count = int(data[i][1])

        if potion == None:
            print("Такую траву мы не используем")
        else:
            print(f"По вашему запросу: {herb} найден следующий вариант: {herb} используется в {potion}, его количество составляет: {count}")
def problem4(data):
    """Формирует список искристых зелий и выводит информацию о них.
    data – таблица с данными
    """
    sparkle = []

    for i in range(1, len(data)):
        if "Искристое" in data[i][0] and data[i][1] != "-1":
            sparkle.append(data[i])

    for potion in sparkle:
        print(f"{potion[0]} осталось в наличии {potion[1]} штук")
def problem5(data):
    """Формирует хэш-таблицу (словарь) по хеш кодам названий зелий. Выводит информацию о зелье с самым большим количеством рецептов.
    data – таблица с данными
    """
    table = {}

    for i in range(1, len(data)):
        potion_hash = hash(data[i][0])
        if data[i][0] in table:
            table[data[i][0]] += 1
        else:
            table[data[i][0]] = 1

    max_recipes = None
    max_potion = None

    for potion in table:
        if max_recipes == None or max_recipes < table[potion]:
            max_recipes = table[potion]
            max_potion = potion

    print(f"Зелье с максимальным количеством рецептов {max_potion} - {max_recipes}.")

def main():
    """Точка входа программы.
    """
    data = read("magical.txt")
    problem1(data)

main()
