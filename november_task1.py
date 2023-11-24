def search_range(nums, target):
    # Создание переменных
    low, high = 0, len(nums)
    left, right = [], []

    # Поиск первого числа
    while low < high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            high = mid
        else:
            low = mid + 1

    left = low
    # Сброс значений переменных для поиска второго числа
    low, high = 0, len(nums)

    # Бинарный поиск для конечной позиции
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > target:
            high = mid # если текущее число больше целевого, свдигаем левее
        else:
            low = mid + 1 # Сдвигаем вправо если не нашли в левой стороне

    right = low - 1

    # Проверка и возврат результата
    if left <= right:
        return [left, right]
    else:
        return [-1, -1]


print(search_range([5, 7, 7, 8, 8, 10], 8))
print(search_range([5, 7, 7, 8, 8, 10], 6))
print(search_range([], 0))
