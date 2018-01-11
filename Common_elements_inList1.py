
#L1 = ['a', 'b', 'c']
#L2 = ['b', 'd']

def common_elements_in_list1(L1, L2): #Defining function to get common elements from two lists
    L3 = []                 # taking empty list to append common elements
    for i in L1:            # loop through list1 elements
        if i in L2:         # checking if list1 element is present in list2 or not
            L3.append(i)    # if true, append that element to empty list 
    return L3               # return appended list

print("enter elements ( only a to z ) to list1:")       # promt user to enter elements to list1
L1 = [str(x) for x in input().split()]                  # reding no.of elements as list1
print("enter elements ( only a to z ) to list2:")       # promt user to enter elements to list2
L2 = [str(y) for y in input().split()]                  # reding no.of elements as list2
print("common elements in list1:")                      
print(common_elements_in_list1(L1,L2))                  # calling function with list1 and list2 as paramenters and getting output


