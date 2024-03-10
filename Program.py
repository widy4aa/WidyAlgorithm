# Algoritma Untuk Sorting String Berdasar Number
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        i_isi.append(i)
        for j in range(0,n-i-1):
            j_isi.append(j)
            if arr[j] < arr [j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

# Contoh penggunaan:
arr = [64, 34, 25, 12,1,100,2,21,31]
i_isi = []
j_isi = []

bubble_sort(arr)
print(arr,"\n",i_isi,"\n",j_isi)

