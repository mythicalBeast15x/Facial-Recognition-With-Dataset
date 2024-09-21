import os
def find_uniques(set1, set2):
    combined_set = set1 | set2
    if set1.issubset(set2) or set2.issubset(set1) or (len(set1) + len(set2)) /2 == len(combined_set):
        print("all numbers are unique")
        print(combined_set)
    else:
        print(f'detected non-uniques: {set1-set2 | set2-set1}')
        """for filename in list(combined_set):
            if filename in set1:
                #use smaller1
            else:
                #use smaller2"""


m_list = {1, 2, 3, 4}
file_map = {}

with open('list_of_nums.txt', 'r') as file:
    lines = file.readlines()

set1 = {1,2,3,4,5}
set2 = {1,2,3,4}


find_uniques(set1, set2)

