list_buku=[['Algoritma', 2000], 
           ['Basis Data', 25000], 
           ['Strukdat',3000],
           ['Aljabar',4000], 
           ['Arsikom',5000]]

print('===DAFTAR DENDA BUKU===')
tampilkan_list=[]
for i in range (len(list_buku)):
    print (i+1)
    print((list_buku[i]))

nomor_buku = int(input('Masukkan nomor buku yang dicari: '))
if nomor_buku < 0 and nomor_buku > 5 :
    print (tampilkan_list[i])
else:
    print ('Nomor tidak valid')