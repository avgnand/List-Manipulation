import random

def sum_list(list_obj):
    """Sum all numbers in a list."""
    sum = 0
    for num in list_obj:
        sum += num
    return sum

def find_list_max(list_obj):
    max = 0
    for item in list_obj:
        if item > max:
            max = item
    return max

def show_rel_wt(list_obj):
    """Return a list with relative weights each member comprises of the given list."""
    total = sum_list(list_obj)
    wt_list = []
    
    for num in list_obj:
        weight = int((num / total) * 100)
        wt_list.append(f"{weight}%")
    
    return wt_list

def check_list(list_obj, limit):
    """
    Check if a list is longer than a given limit, 
    and split it into sublists; otherwise, return the list
    """
    if len(list_obj) > limit:
        num_of_lists = int(len(list_obj) / limit) + 1
        sublist = []
        k = 0
        while k < num_of_lists:
            x = list_obj[limit*k:limit*(k+1)]
            sublist.append(x)
            k += 1

        return sublist

    return list_obj

def create_wild_lists(amount,length):
    """Create a list of (amount) number of lists of length (length)."""
    box = []

    k = 0
    while k < amount:
        sublist = []
        j = 0
        while j < length:
            num = random.randint(1, 100)
            sublist.append(num)
            j += 1
        box.append(sublist)
        k += 1

    if amount == 1:
        return sublist

    return box

def create_unique_lists(amount):
    """
    Create a given number of lists, each of random length, 
    with members of random values.
    """
    _len_list = create_wild_lists(1, amount)

    box = []
    i = 0
    while i < amount:
        h = create_wild_lists(1, _len_list[i])
        box.append(h)
        i += 1
    
    return box

def check_list_weight(list_obj, max_wt):
    list_wt = sum_list(list_obj)
    if list_wt > max_wt:
        list_max = find_list_max(list_obj)
        print(list_max)
        box = []
        box.append(list_max)
        list_obj.remove(list_max)
        check_list_weight(list_obj, max_wt)
        return list_obj
    
    return list_obj

dummy = create_wild_lists(1, 5)
print(dummy)
dummy_checked = check_list_weight(dummy, 50)
print(dummy_checked)

# New Function:
# if sum of a list is greater than given max, 
# remove largest members until the sum is within max, 
# while adding removed members to a new list

# main = create_unique_lists(4)
# # for li in main:
# #     sub = check_list(li, 4)
# print(main)
# print(len(sub))
# print(sub)
