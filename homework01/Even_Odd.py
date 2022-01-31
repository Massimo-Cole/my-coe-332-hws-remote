my_int_list = [1,2,5,4,5,6,16,8,2,10,12,22]

def EvenOdd(mylist):
    for i in mylist:
        if (i % 2 == 0):
            print(i, "Even")
        else:
            print(i, "Odd")

EvenOdd(my_int_list)
