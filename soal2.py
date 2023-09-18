nilai = set({3,6,9,2,5,7}) 
#proses menambah elemen
nilai.update({1,4,8,10})
print("nilai = ", nilai)

#proses menghapus elemen
nilai.discard(1)
nilai.discard(3)
nilai.discard(4)
nilai.discard(5)
nilai.discard(7)
nilai.discard(8)
nilai.discard(10)

print("nilai = ", nilai)