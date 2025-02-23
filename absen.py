import json


absensi_list = []

def simpan_ke_file():
    with open("absensi.json", "w") as file:
        json.dump(absensi_list, file, indent=4)

def tambah_absensi(nama, tanggal, status):
    absensi = {"id": len(absensi_list) + 1, "nama": nama, "tanggal": tanggal, "status": status}
    absensi_list.append(absensi)
    simpan_ke_file()
    print("Absensi berhasil ditambahkan!")

def lihat_absensi():
    if not absensi_list:
        print("Tidak ada data absensi.")
    for absensi in absensi_list:
        print(absensi)

def update_absensi(id_absensi, nama, tanggal, status):
    for absensi in absensi_list:
        if absensi["id"] == id_absensi:
            absensi["nama"] = nama
            absensi["tanggal"] = tanggal
            absensi["status"] = status
            simpan_ke_file()
            print("Absensi berhasil diperbarui!")
            return
    print("Data absensi tidak ditemukan!")

def hapus_absensi(id_absensi):
    global absensi_list
    absensi_list = [absensi for absensi in absensi_list if absensi["id"] != id_absensi]
    simpan_ke_file()
    print("Absensi berhasil dihapus!")

while True:
    print("\n=== Sistem Absensi ===")
    print("1. Tambah Absensi")
    print("2. Lihat Absensi")
    print("3. Update Absensi")
    print("4. Hapus Absensi")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
        status = input("Masukkan status (Hadir/Tidak Hadir): ")
        tambah_absensi(nama, tanggal, status)
    elif pilihan == "2":
        lihat_absensi()
    elif pilihan == "3":
        id_absensi = int(input("Masukkan ID absensi yang akan diperbarui: "))
        nama = input("Masukkan nama baru: ")
        tanggal = input("Masukkan tanggal baru (YYYY-MM-DD): ")
        status = input("Masukkan status baru (Hadir/Tidak Hadir): ")
        update_absensi(id_absensi, nama, tanggal, status)
    elif pilihan == "4":
        id_absensi = int(input("Masukkan ID absensi yang akan dihapus: "))
        hapus_absensi(id_absensi)
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid!")
