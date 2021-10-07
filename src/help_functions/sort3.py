# metoda służy to sortowania 3 list równolegle, wedle klucza sortowania pierwszej listy
'''
list1 jest najistotniejszą listą, to według niej pozostałe listy będą posortowane
list2 to druga lista, będąca posortowana wedle list1
list3 to trzecia lista, będąca posortowana wedle list1
'''
def sort3(list1, list2, list3):
    zipped_lists = zip(list1, list2, list3)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    l1, l2, l3 = [list(tuple) for tuple in tuples]
    return l1, l2, l3
