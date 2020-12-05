from timeit import default_timer as timer


class HeapSort:
    def __init__(self):
        self.list = []
        self.input_file = None
        self.heapsize = None
        self.output_file = None
        pass

    def build_max_heap(self, list):
        self.heapsize = len(list) - 1
        i = len(list)//2
        while i > 0:
            self.max_heapify(list, i)
            i = i//2
        self.max_heapify(list,i)

    def sort(self, array):
        self.list = array
        self.build_max_heap(self.list)
        for i in range(len(self.list)-1, 0, -1):
            temp = self.list[0]
            self.list[0] = self.list[i]
            self.list[i] = temp
            self.heapsize -= 1
            self.max_heapify(self.list, 0)

    def max_heapify(self, list, i):
        left = 2 * i
        right = 2 * i + 1
        if left <= self.heapsize and list[left] > list[i]:
            largest = left
        else:
            largest = i
        if right <= self.heapsize and list[right] > list[largest]:
            largest = right
        if largest != i:
            temp = list[i]
            list[i] = list[largest]
            list[largest] = temp
            self.max_heapify(list, largest)

    def read(self, input_file, output_file):
        self.input_file = open(input_file, 'r')
        self.output_file = open(output_file, 'w+')
        lines = self.input_file.readlines()
        output_instance = []
        temp = []
        count = 0
        start_timer = timer()
        last_size = 0
        last_list = []
        for instance in lines:
            if (timer() - start_timer) > 7200:
                print("Exiting as processing time exceeds 2 Hours !!")
                self.input_file.close()
                self.write_file(output_instance)
                return
            instance = [int(i) for i in instance.split()]
            if count == 20:
                count = 0
                print("Instance size: {0}".format(int(len(instance) / 10)))
                self.print_status(temp)
                last_size = len(instance)
                last_list = temp
                temp.clear()
            start = timer()
            self.sort(instance)
            end = timer()
            temp.append(end - start)
            count += 1
            output_instance.append(instance)
        print("Instance size: {0}".format(last_size))
        self.print_status(last_list)
        self.input_file.close()
        print("-------------------------------------")
        print("Writing To File!!")
        self.write_file(output_instance)

    def write_file(self, output_instances):
        for line in output_instances:
            self.output_file.writelines([str(i) + " " for i in line])
            self.output_file.writelines("\n")
        self.output_file.close()

    def print_status(self, list_i):
        mean = sum(list_i) / len(list_i)
        variance = sum([((x - mean) ** 2) for x in list_i]) / len(list_i)
        res = variance ** 0.5
        print("     Average Time           :{0}".format(str(mean)))
        print("     Standard Deviation     :{0}".format(str(res)))


sortlist = HeapSort()
print("Enter the input file path")
input_file = input()
sortlist.read(input_file, "heap_sort_output.txt")