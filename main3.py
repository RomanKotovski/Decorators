from main2 import logger

class FlatIterator:

    def __init__(self, list_of_list):
        self.main_list = list_of_list

    def __iter__(self):
        self.main_list_cursor = 0
        self.nested_list_cursor = 0
        return self

    def __next__(self):
        if self.main_list_cursor == len(self.main_list):
            raise StopIteration
        item_1 = self.main_list[self.main_list_cursor]
        item_2 = item_1[self.nested_list_cursor]
        self.nested_list_cursor += 1
        if self.nested_list_cursor == len(item_1):
            self.nested_list_cursor = 0
            self.main_list_cursor += 1

        return item_2


def test_3():
    @logger('log_iter.log')
    def list_of_lists(lol):
        return FlatIterator(lol).main_list

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    main_list = list_of_lists(list_of_lists_1)


if __name__ == '__main__':
    test_3()