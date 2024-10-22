numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

skip1 = numbers[0:4]
skip2 = numbers[5:]
alt = skip1 + skip2

total = sum(alt)
count = len(alt) + 1
average = total / count

numbers[4] = average
#print(skip1)
#print(skip2)
#print(alt)
#print(total)
#print(count)
#print(average)
#numbers[4] = sum(numbers) / len(numbers)


print("Измененный список:", numbers)
