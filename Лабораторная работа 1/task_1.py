numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

first_half = numbers [:4]
second_half = numbers [5:]
average = (sum(first_half) + sum(second_half)) / len(numbers)
numbers[4] = average
print('Измененный список:', numbers)
