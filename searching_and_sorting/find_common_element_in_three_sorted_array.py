ar1 = [1, 5, 10, 20, 40, 80] 
ar2 = [6, 7, 20, 80, 100] 
ar3 = [3, 4, 15, 20, 30, 70, 80, 120] 
def common_elements(ar1,ar2,ar3):
    set1=set(ar1)
    set2=set(ar2)
    set3=set(ar3)
    common_in_set1_set2=set1.intersection(set2)
    set4=set(common_in_set1_set2)
    common_in_set2_set3=list(common_in_set1_set2.intersection(set3))
    common_in_set2_set3.sort()
    return common_in_set2_set3
k=common_elements(ar1,ar2,ar3)
print(k)