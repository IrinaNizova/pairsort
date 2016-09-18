from itertools import permutations


def pairsort(lst):
    for i in range(0, len(lst)-3):
        curr_pair = num_from_lst(lst[i:i+2])
        min_pair_index = i
        # Find right of the current pair smaller pair
        for j in range(i+2, len(lst)-1):
            if lst[j]*10 + lst[j+1] < curr_pair:
                min_pair_index = j
                curr_pair = num_from_lst(lst[j:j+2])
        # Change current pair and smaller pair if we found it
        if min_pair_index != i:
            lst[i:i+2], lst[min_pair_index:min_pair_index+2] = \
                lst[min_pair_index:min_pair_index+2], lst[i:i+2]
    return lst

def num_from_lst(lst):
    return lst[0]*10 + lst[1]

def is_sorted(lst):
    return False if any(1 for i in range(len(lst)-1) if lst[i] > lst[i+1]) else True

if __name__ == "__main__":
    been_sorted = 0
    not_sorted = 0
    for lst in permutations([1, 2, 3, 4, 5, 6]):
        if is_sorted(pairsort(list(lst))):
            been_sorted += 1
        else:
            not_sorted += 1

    print("Can sorted {} combinations".format(been_sorted))
    print("Can not sorted {} combinations".format(not_sorted))

