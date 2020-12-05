from timeit import default_timer as timer


class QuickSort:
    def __init__(self):
        self.list = []
        self.input_file = None
        self.output_file = None
        pass

    def sort(self, list_instance, start, end):
        self.list = list_instance
        start = start
        end = end
        if start < end:
            mid = self.partition(self.list, start, end)
            self.sort(self.list, start, mid - 1)
            self.sort(self.list, mid + 1, end)

    def partition(self, list, start, end):
        pivot = list[end]
        i = start - 1
        for j in range(start, end - 1):
            if list[j] <= pivot:
                i += 1
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
        temp = list[i + 1]
        list[i + 1] = list[end]
        list[end] = temp
        return i + 1

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
            self.sort(instance, 0, len(instance) - 1)
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
        print(" Average Time {0}".format(str(mean)))
        print("Standard Deviation {0}".format(str(res)))


sortlist = QuickSort()
print("Enter the input file path")
input_file = input()
sortlist.read(input_file, "Quick_sort_output.txt")
