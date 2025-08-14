array = [4,3,2,1,6,7,5];

len = len(array)

print("Before Sorting", array)
for i in range(1,len):
    index = i
    previous = array.pop(i)
    # print('\n',array[i]);
    for j in range(i - 1, -1, -1):
        if(array[j] > previous):
            index = j
    array.insert(index,previous)

print("After Sorting", array)



# Using thw while Loop

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

for m in range(1, len(my_array)):
    key = my_array[m]
    
    # Compare with all elements in the sorted part (going backwards)
    for n in range(m-1, -2, -1):  # goes down to -1
        if n >= 0 and key < my_array[n]:
            my_array[n+1] = my_array[n]  # shift
        else:
            my_array[n+1] = key
            break  # found correct position
    
    print(f"Pass {m}: {my_array}")

print("\nSorted array:", my_array)
