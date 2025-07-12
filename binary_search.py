def binary_search(lis_angka,target):
    low = 0
    high = len(lis_angka) - 1

    while low <= high:
        mid = (low + high)// 2
        nilai_tengah = lis_angka[mid]
        if nilai_tengah == target:
            return nilai_tengah
        elif nilai_tengah < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

lis_angka = [1,2,3,4,5,6,7,8,9,10,11]
target = 3
print(f"{binary_search(lis_angka,target)}")