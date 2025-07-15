import random  # opsional kalau pakai pivot acak

def quicksort(arr: list) -> list:
    """
    Mengurutkan list menggunakan algoritma Quick Sort (rekursif).
    """
    if len(arr) <= 1:
        return arr

    # Ganti pivot ke arr[0] atau random.choice(arr) untuk performa lebih baik
    pivot = arr[0]  # atau: pivot = random.choice(arr)

    # Bagi elemen ke kiri dan kanan berdasarkan pivot
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    # Gabungkan hasil rekursi kiri + pivot + kanan
    return quicksort(left) + [pivot] + quicksort(right)

# Contoh pemakaian
nilai = [1, 2, 5, 1,2, 6, 12, 13, 7, 19]
hasil = quicksort(nilai)
print(hasil)
