my_list = [1,2,3,4,5,6,7,8,9,10]
list_squared = [1,4,9,16,25,36,49,64,81,100]
list_cubed = [1,8,27,64,125,216,343,512,729,1000]

def print_3(list1, list2, list3):
    for i in range(10):
        print(list1[i], ",", list2[i], ",", list3[i])

print_3(my_list, list_squared, list_cubed)
