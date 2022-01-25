correct_array = False
no_sort_list = []
number = None


def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] < element <= array[middle + 1]:
        return middle
    elif element <= array[middle]:
        return binary_search(array, element, left, middle)
    else:
        return binary_search(array, element, middle, right)


while True:
    try:
        if not no_sort_list:
            no_sort_list = [int(x) for x in input("Введите числа: ").split()]
            print(merge_sort(no_sort_list))
        correct_array = True
        number = int(input("Введите число: "))
        break
    except ValueError:
        print('Неверное значение')
    except Exception:
        print('Неизвестная ошибка')

sort_list = merge_sort(no_sort_list)

if min(sort_list) >= number or max(sort_list) < number:
    print('Число меньше либо равно минимальному или больше максимального')
else:
    print(binary_search(sort_list, number, 0, len(sort_list)))