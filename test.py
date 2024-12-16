from utils import test_nod, fact, sort_list, fibo


class TestApiIdcAdminRole:

    def test_check_all_methods(self):
        li = [5, 2, 7, 4, 0, 9, 8, 6]

        print(sort_list(li))
        print(fact(5))
        print(test_nod(18, 27))
        print(fibo(9))
