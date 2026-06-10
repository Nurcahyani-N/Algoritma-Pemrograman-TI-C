data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 
        443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 
        256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71,
        19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 
        59, 98, 55, 99, 280, 303, 16, 25, 321]

# RADIX SORT
def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

def radixSortWithBubbleSort(arr):
  max_val = max(arr)
  exp = 1
  while max_val // exp > 0:
    radixList = [[],[],[],[],[],[],[],[],[],[]]

    for num in arr:
      radixIndex = (num // exp) % 10
      radixList[radixIndex].append(num)

    for bucket in radixList:
      bubbleSort(bucket)
    i = 0
    for bucket in radixList:
      for num in bucket:
        arr[i] = num
        i += 1
    exp *= 10

# MERGE SORT
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        kiri = arr[:mid]
        kanan = arr[mid:]

        merge_sort(kiri)
        merge_sort(kanan)

        i = j = k = 0

        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                arr[k] = kiri[i]
                i += 1
            else:
                arr[k] = kanan[j]
                j += 1
            k += 1

        while i < len(kiri):
            arr[k] = kiri[i]
            i += 1
            k += 1

        while j < len(kanan):
            arr[k] = kanan[j]
            j += 1
            k += 1

# LINEAR SEARCH
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i, arr[i]
    return -1, None

# BINARY SEARCH
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, None

print('Data sebelum disorting: ')
print(data)

# Radix Sort
data_radix = data.copy()
radixSortWithBubbleSort(data_radix)
print('\nHasil Radix Sort: ', data_radix)

# Merge Sort
data_merge = data.copy()
merge_sort(data_merge)
print('\nHasil Merge Sort: ', data_merge)

# Input user
target = int(input('\nMasukkan angka yang ingin dicari: '))

# Linear Search
indexL, valueL= linear_search(data, target)
if indexL != -1:
    print(f'\nLinear Search -> Angka telah ditemukan di index {indexL} dengan nilai {valueL}.')
else:
    print('\nLinear Search -> Angka yang dicari tidak ada.')

# Binary Search
indexB, valueB = binary_search(data_merge, target)
if indexB != -1:
    print(f'Binary Search -> Angka telah ditemukan di index {indexB} dengan nilai {valueB}.')
else:
    print('Binary Search -> Angka yang dicari tidak ada.')