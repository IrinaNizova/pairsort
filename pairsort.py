from itertools import permutations

def pairsort(lst):
    switch = True
    while switch:
        switch = False
        for i in range(0, len(lst)-3):
            if lst[i]*10+lst[i+1] > lst[i+2]*10+lst[i+3]:
                lst[i:i+2], lst[i+2: i+4] = lst[i+2: i+4], lst[i:i+2]
                switch = True
    return lst

def is_sorted(lst):
    return False if any(1 for i in range(len(lst)-1) if lst[i]>lst[i+1]) else True



if __name__ == "__main__":
    sorted = 0
    not_sorted = 0
    for lst in permutations([1,2,3,4,5,6]):
        if is_sorted(pairsort(list(lst))):
            sorted += 1
        else:
            not_sorted += 1

    print("Can sorted {} combinations".format(sorted))
    print("Can not sorted {} combinations".format(not_sorted))

