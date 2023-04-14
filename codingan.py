#!/usr/bin/env python
# coding: utf-8

# In[2]:

#Buat Database
import mysql.connector

#Buat Database
dataBase = mysql.connector.connect(
    user  = 'root',
    host = 'localhost'
)
cursorObject = dataBase.cursor()

#Membuat database dengan nama "db_sales_V3922032"
cursorObject.execute("CREATE DATABASE db_sales_V3922032")


# In[6]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'db_sales_V3922032'
)

cursorObject = dataBase.cursor()

#Membuat tabel database 
studentRecord = """CREATE TABLE DATA_STOK_BARANG (
                    id_Barang VARCHAR(10) PRIMARY KEY,
                    nama_barang VARCHAR(20),
                    harga_barang FLOAT,
                    stok_awal INT,
                    barang_masuk INT,
                    Barang_Keluar INT,
                    Stok_Akhir INT
                    )"""

cursorObject.execute(studentRecord)

dataBase.close()


# In[8]:



import mysql.connector

#Koneksi ke database
dataBase = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    database = 'db_sales_V3922032'
)

cursorObject = dataBase.cursor()

#Menambahkan data ke tabel
def insert_data( Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir ):
    sql = "INSERT INTO DATA_STOK_BARANG (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)    VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)
    
    cursorObject.execute(sql, val)
    dataBase.commit()

    print(" ")
    print("Data berhasil ditambahkan")

#Menampilkan data dari tabel
def show_data():
    query = "SELECT * FROM DATA_STOK_BARANG"
    
    cursorObject.execute(query)

    myresult = cursorObject.fetchall()

    for x in myresult:
        print(x)
        
    print(" ")
    print("Data berhasil ditampilkan")

#Mengupdate data di tabel
def update_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir):
    sql = "UPDATE DATA_STOK_BARANG SET Nama_Barang = %s, Harga_Barang = %s, Stok_Awal = %s, Barang_Masuk = %s, Barang_Keluar = %s, Stok_Akhir = %s WHERE Id_Barang = %s"
    val = (Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir, Id_Barang)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil diupdate")

#Menghapus data dari tabel
def delete_data(Id_Barang):
    sql = "DELETE FROM DATA_STOK_BARANG WHERE Id_Barang = %s"
    val = (Id_Barang,)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil dihapus")

#Mencari data berdasarkan Id_Barang
def search_data(id_barang):
    sql = "SELECT * FROM DATA_STOK_BARANG WHERE Id_Barang = %s"
    val = (id_barang,)

    cursorObject.execute(sql, val)

    myresult = cursorObject.fetchall()

    if myresult:
        print("+------------+----------------------+--------------+-----------+--------------+---------------+------------+")
        print("| Id_Barang  | Nama_Barang          | Harga_Barang | Stok_Awal | Barang_Masuk | Barang-Keluar | Stok_Akhir |")
        print("+------------+----------------------+--------------+-----------+--------------+---------------+------------+")
        for row in myresult:
            print("| {:<10} | {:<20} | {:>12,.2f} | {:>9} | {:>12} | {:>13} | {:>10} |".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            ))
        print("+------------+----------------------+--------------+-----------+--------------+---------------+------------+")
        print("Data berhasil dicari")
    else:
        print("Id Barang tidak ditemukan.")




#Pilihan menu
while True:
    print(" ")
    print("=== SISTEM PENCATATAN DATA BARANG ===")
    print("1. Input Data Barang")
    print("2. Tampilkan Data Barang")
    print("3. Update Data Barang")
    print("4. Hapus Data Barang")
    print("5. Cari Data Barang")
    print("6. Keluar Sistem")
    print("-------------------")
    menu = input("Pilih Nomor 1-6 : ") #input untuk pilihan menu yang akan dicari
    print(" ")

    #pilihan 1 "insert data"
    if menu == "1":
        Id_Barang = input("Masukkan Id Barang :")
        Nama_Barang = input("Masukkan Nama Barang :")
        Harga_Barang = int(input("Masukkan Harga Barang :"))
        Stok_Awal = int(input("Masukkan Stok Awal :"))
        Barang_Masuk = int(input("Masukkan Barang Masuk :"))
        Barang_Keluar = int(input("Masukkan Barang Keluar :"))
        
        #Rumus untuk mencari stok_akhir
        Stok_Akhir = Stok_Awal + Barang_Masuk - Barang_Keluar
        
        #mencetak Stok_Akhir dari rumus sebelumnya
        print("Stok Akhir : ", Stok_Akhir)
        
        insert_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)
    
    #pilihan 2 "show data"
    elif menu == "2":
        cursorObject.execute("SELECT * FROM DATA_STOK_BARANG")
        data = cursorObject.fetchall()
        if len(data) == :
            print("Tidak ada data yang tersimpan")
        else:
            # printing table headers
            print("+------------+----------------------+-----------------+------------+-----------------+------------------+------------+")
            print(f"| {'ID_Barang'.ljust(10)} | {'Nama_Barang'.ljust(20)} | {'Harga_Barang'.ljust(15)} | {'Stok_Awal'.ljust(10)} | {'Barang_Masuk'.ljust(15)} | {'Barang_Keluar'.ljust(15)} | {'Stok_Akhir'.ljust(10)} |")
            print("+------------+----------------------+-----------------+------------+-----------------+------------------+------------+")
            # printing table rows
            for row in data:
                print(f"| {str(row[0]).ljust(10)} | {row[1].ljust(20)} | {str(row[2]).ljust(15)} | {str(row[3]).ljust(10)} | {str(row[4]).ljust(15)} | {str(row[5]).ljust(15)} | {str(row[6]).ljust(10)} |")
            print("+------------+----------------------+-----------------+------------+-----------------+------------------+------------+")


    #pilihan 3 "update data"
    elif menu == "3":
        Id_Barang = input("Masukkan Id Barang yang akan diupdate :")
        Nama_Barang = input("Masukkan Nama Barang baru :")
        Harga_Barang = int(input("Masukkan Harga Barang baru :"))
        Stok_Awal = int(input("Masukkan Stok Awal baru :"))
        Barang_Masuk = int(input("Masukkan Barang Masuk baru :"))
        Barang_Keluar = int(input("Masukkan Barang Keluar baru :"))
        
        Stok_Akhir = Stok_Awal + Barang_Masuk - Barang_Keluar
        print("Stok Akhir setelah diupdate : ", Stok_Akhir)
        
        update_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)

    #pilihan 4 "hapus data"
    elif menu == "4":
        Id_Barang = input("Masukkan Id Barang yang ingin dihapus :")
        
        delete_data(Id_Barang)

    #pilihan 5 "cari data"
    elif menu == "5":
        Id_Barang = input("Masukkan Id Barang yang ingin dicari:")
        result = search_data(Id_Barang)

    #pilihan 6 "keluar dari program"
    elif menu == "6":
        print("Semangat broo")
        break

    #ketika menginputkan tidak sesuai dengan pilihan yang tertera
    else:
        print("Pilihan anda tidak valid, Mohon coba lagi dan pilihlah dengan benar")2


# In[ ]:




