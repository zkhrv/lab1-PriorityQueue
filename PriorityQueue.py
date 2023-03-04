class PriorityQueue:
    def __init__(self):
        self.size = 0
        self.arr = []

    def add_element(self, tmp):
        self.arr.append(tmp)
        self.size += 1
        i = self.size // 2 - 1
        while i >= 0:
            self.rewrite(self.arr, self.size, i)
            i -= 1

    def rewrite(self, arr, n, max):
        i = max
        id_left = i * 2 + 1
        id_right = i * 2 + 2
        if id_left < n and arr[id_left] > arr[i]:
            i = id_left
        if id_right < n and arr[id_right] > arr[i]:
            i = id_right
        if i != max:
            arr[i], arr[max] = arr[max], arr[i]
            self.rewrite(arr, n, i)

    def del_max_el(self):
        if self.size > 0:
            self.arr.pop(0)
            self.size -= 1
            i = self.size // 2 - 1
            while i >= 0:
                self.rewrite(self.arr, self.size, i)
                i -= 1
        else:
            print("Очередь пуста!")

    def del_element(self, del_el):
        if self.size > 0:
            tmp = -1
            for i in range(self.size):
                if self.arr[i] == del_el:
                    tmp = i
                    break
            if tmp >= 0:
                self.arr.pop(tmp)
                self.size -= 1
                i = self.size // 2 - 1
                while i >= 0:
                    self.rewrite(self.arr, self.size, i)
                    i -= 1
            else:
                print("Такого элемента нет в очереди")
        else:
            print("Очередь пуста!")

    def get_max_el(self):
        return self.arr[0]

    def count(self):
        print(f"Элементов в очереди: {self.size}")

    def write(self):
        print(self.arr)