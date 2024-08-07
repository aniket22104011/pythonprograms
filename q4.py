def group(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
print("Grouped list:", group(numbers, chunk_size))
