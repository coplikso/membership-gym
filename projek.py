

# 1. declare variable daftar tamu dan jumlah
daftar_tamu = []

while True:
    try:
        jumlah_input = input("Berapa jumlah member yang ingin didaftarkan: ")
        if not jumlah_input.isnumeric():
            raise ValueError("input angka ya! bukan huruf.")
        jumlah = int(jumlah_input)
        break  # kalau valid, keluar dari loop
    except ValueError as e:
        print(f"Error: {e}")


# 2. Buat fungsi undangan
def undangan_app():
    # 3. Membuat Looping jumlah tamu
    for _ in range(jumlah):
        
        # 4. Input nama, alamat, gender dari user
        nama = input('Masukan Nama member : ').title()
        alamat = input("alamat: ").title()
        gender = input("gender: ").title()
        tipe_paket = input("tipe_paket:vip/reguler/silver ?  ").title()

        # 5. condition, jika tamu sudah diundang, tampil pesan
        # jika tidak, masukkan ke daftar tamu
        
        
        if ([nama, alamat, gender, tipe_paket]) in daftar_tamu:
            print(f"{nama} sudah didaftarkan")
        else:
            daftar_tamu.append([nama, alamat, gender, tipe_paket])

        # 8. Membuat Tampilan Judul table
        print("=" * 55)
        print("=== Daftar member yang didaftarkan:")
        print("=" * 55)

        # 9. Header kolom — FIX: tambah kolom tipe_paket
        print("{:<8} {:<16} {:<12} {:<10} {:<10}".format("No", "Nama", "Alamat", "Gender", "Tipe Paket"))
        print("=" * 55)

        # FIX: no = 0 dipindah ke sini, sebelum loop for tamu
        no = 0

        # 10. Membuat Looping untuk daftar_tamu
        for tamu in daftar_tamu:

            # 11. melakukan perulangan menambah 1
            no += 1

            # 12. Membuat format kode
            no_format = f"MBR-{no:03}"

            # 13. Menampilkan nilai/data dari daftar tamu
            print("{:<8} {:<16} {:<12} {:<10} {:<10}".format(no_format, tamu[0], tamu[1], tamu[2], tamu[3]))

        print("=" * 55)
        # 13. Menampilkan jumlah Undangan
        print("Jumlah member yang didaftarkan =", len(daftar_tamu))

# 14. memanggil fungsi undangan
undangan_app()