def find_missing(list1, list2):
    if list1 == [] and list2 == []:
        return 0
    elif list1 == list2:
        return 0
    else:
        return (set(list1) ^ set(list2)).pop()
