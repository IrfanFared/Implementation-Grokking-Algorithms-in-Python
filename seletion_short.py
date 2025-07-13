def seltion_sort(arr):
    
    for i in range(len(arr)):
        nilai_terkecil = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[nilai_terkecil]:
                nilai_terkecil = j
        arr[i] , arr[nilai_terkecil] = arr[nilai_terkecil] , arr[i]
    return arr

list1 = [12,3,10,1,2,0]
b = seltion_sort(list1)
print(b)

    