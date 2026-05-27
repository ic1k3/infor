numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

total_sum = sum(y for y in numbers if y is not None) # TODO заменить значение пропущенного элемента средним арифметическим
index_None = numbers.index(None)
Average_Number = total_sum / len(numbers)
numbers[index_None] = Average_Number
Average_Number = round(Average_Number, 2)
print("Измененный список:", numbers)
