def sort2(list1, list2):
    zipped_lists = zip(list1, list2)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    l1, l2 = [list(tuple) for tuple in tuples]
    return l1, l2


def sort3(list1, list2, list3):
    zipped_lists = zip(list1, list2, list3)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    l1, l2, l3 = [list(tuple) for tuple in tuples]
    return l1, l2, l3
