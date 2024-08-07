def write_to_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)
def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return content

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = []
        line = file.readline()
        while line:
            lines.append(line.strip())
            line = file.readline()
        return lines

filename = 'example.txt'
lines_to_write = ['First line\n', 'Second line\n', 'Third line\n']
write_to_file(filename, lines_to_write)
content = read_from_file(filename)
print("File content read using read():")
print(content)
lines = read_lines(filename)
print("\nFile lines read using readline():")
print(lines)
