# File objects

# Method 1

f = open('text.txt', 'r')

print(f.name)
print(f.mode)

f.close()


# Method 2 preferred method - Context manager

with open('text.txt', 'r') as f:
    # f_contents = f.read()
    # f_contents = f.readlines()

    # f_contents = f.readline()
    # print(f_contents, end='')

    # for line in f:
    #     print(line, end='')

    # f_contents = f.read(100)
    # print(f_contents, end='')

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)

    print(f.tell())

    # while len(f_contents) > 0:
    #     print(f_contents, end='')
    #     f_contents = f.read(size_to_read)

    with open('text2.txt', 'w') as fi:
        fi.write('Text')
        fi.seek(0)
        fi.write('R')

with open('text.txt', 'r') as rf:
    with open('text_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# Reading image files
with open('dog.jpeg', 'rb') as rf:
    with open('dog_copy.jpeg', 'wb') as wf:
        for line in rf:
            wf.write(line)

# Reading image files in chunk sizes
with open('dog.jpeg', 'rb') as rf:
    with open('dog_copy_chunk.jpeg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

