numbers = [10, 25, 7, 42, 18, 5]

print("Not Sorted array", numbers)

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if(numbers[j] > numbers[j + 1]):
           temp = numbers[j]
           numbers[j] = numbers[j + 1]
           numbers[j + 1] = temp

print("Sorted array", numbers)

# Time complexity of this code is O(n^2)