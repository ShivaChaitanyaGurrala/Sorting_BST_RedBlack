import random


def generator():
    output_file = open("input_sort.txt", 'w+')
    j = 1
    for i in range(5):
        j *= 10
        for p in range(20):
            for k in range(j):
                output_file.write(str(random.randint(0, 2 ** 32 - 1)) + " ")
            output_file.write("\n")

    output_file.close



generator()
