# Введите количество кустов (N)
N = int(input("Введите количество кустов: "))

# Инициализируйте список урожайности для каждого куста
harvest = []

# Пользователь вводит урожайность для каждого куста
for i in range(N):
    yield_of_bush = int(input(f"Введите урожайность для куста {i + 1}: "))
    harvest.append(yield_of_bush)

# Рассчитываем максимальную урожайность и индексы тройки кустов с максимальной урожайностью
max_harvest = 0
max_indices = (0, 1, 2)

for i in range(N):
    current_harvest = harvest[i] + harvest[(i + 1) % N] + harvest[(i + 2) % N]
    if current_harvest > max_harvest:
        max_harvest = current_harvest
        max_indices = (i, (i + 1) % N, (i + 2) % N)

# Выводим введенные данные и индексы тройки кустов с максимальной урожайностью
print("Количество кустов:", N)
print("Урожайность на каждом кусте:", harvest)
print("Индексы тройки кустов с максимальной урожайностью:", max_indices)
print("Максимальная урожайность за один заход собирающего модуля:", max_harvest)

