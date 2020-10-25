class list:
            
    def linear_search(self,lst,n):
        for i in range(len(lst)):
            if lst[i] == n:
                return f'Position :{i}'
        return -1
    
    def insertion_sort(self,lst):
        for i in range(len(lst)):
            
            index = lst[i]
            
            c = i - 1
            
            while c >= 0 and lst[c] > index:
                lst[c + 1] = lst[c]
                c -= 1
                
            lst[c+1]  = index
            
        return lst
    
    def merge(self,lst,lst2):
         lst.extend(lst2)
         print(lst)
    
    def reverse(self,lst):
        return lst[::-1]

lst = [1,3,6,7,10]
lst2 = [2,4,5,8,9]
l = list()
print(l.linear_search(lst,7))
print(l.linear_search(lst2,4))
print(l.merge(lst,lst2))
print(l.insertion_sort(lst))
print(l.reverse(lst))