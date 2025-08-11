numbers = [10, 25, 7, 42, 18, 5]

print("Not  Sorted Array", numbers);

len = len(numbers)

for i in range(len):
    firstindex = i
    # print(f"\nPass {i+1}: Starting with {numbers}")
    for j in range(i + 1, len):
        # print(f"  Comparing {numbers[j]} with {numbers[firstindex]}")
        if(numbers[j] < numbers[firstindex]):
            firstindex = j
    numbers[i], numbers[firstindex] = numbers[firstindex], numbers[i]

print("Sorted Array", numbers)