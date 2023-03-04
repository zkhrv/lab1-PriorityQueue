from PriorityQueue import PriorityQueue


if __name__ == '__main__':
    test = PriorityQueue()
    test.add_element(1)
    test.add_element(70)
    test.add_element(3)
    test.add_element(5)
    test.add_element(8)
    test.add_element(15)
    test.write()
    test.del_max_el()
    test.write()
    test.del_element(3)
    test.write()
    test.count()