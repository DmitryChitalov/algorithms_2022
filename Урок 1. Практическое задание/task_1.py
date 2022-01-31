
#Задание 1.
#Сложность: O(n)
def check_1(lst_obj):
    lst_to_set = set(lst_obj)  # O(n)
    return lst_to_set  # O(1)
#T(n)=n+1

#Сложность: O(n**2)
def check_2(lst_obj):
   for j in range(len(lst_obj)): #O(n)
        if lst_obj[j] in lst_obj[j+1:]: #O(n)
            return False #O(1)
        return True #O(1)
#T(n)=n*n+1+1=n**2 + 2

#Сложность: O(n**2)
def check_3(lst_obj):

    lst_copy = list(lst_obj) #O(n)
    lst_copy.sort() #O(nlogn)
    for i in range(len(lst_obj) - 1): #T(n)=O(n)+O(1)+O(1)=n+2=O(n)
        if lst_copy[i] == lst_copy[i+1]: #T(n)=O(1)+O(1)+O(n)+O(n)=2+2n=O(n)
            return False #O(1)
    return True #O(1)

#T(n)=n+nlogn+n+n+1+1=n+nlogn+n**2+2
