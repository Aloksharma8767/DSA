array=['54','546','548','60']
for i in range(len(array)):
        for j in range(1+i,len(array)):
            if array[j]+array[i]>array[i]+array[j]:
                array[i],array[j]=array[j],array[i]
                print(array)
result="".join(array)
print(result)