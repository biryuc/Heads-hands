import numpy as np

def random_list_of_arr(n):
    assert type(n) == int and n>0,'The number of arrays must be integer and greater than zero'
    list_arr,size = [],[]
    for i in range(n):
        k = int(np.random.random()*100) #Верхняя граница для диапазона размеров и диапазона значений массива
        if k<=1: k+=1
        m = np.random.randint(1,k) # Значение размера выбирается из случайного диапазона значений
        if m in size : m =np.random.randint(1,k)
        size.append(m)
        arr = np.random.randint(k, size=size[i])
        if i%2 == 0 : list_arr.append(sorted(arr))
        else : list_arr.append(sorted(arr,reverse=True))
    print(list_arr)

    return list_arr

if __name__ == '__main__':
    random_list_of_arr(-1)

