def lensort(strings):
    return sorted(strings, key=len)
string_list = ["apple", "banana", "cherry", "date", "fig", "grape"]
print("Strings sorted by length:", lensort(string_list))
