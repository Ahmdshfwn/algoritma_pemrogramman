def perpustakaan_mini():
    daftar_buku = [] #untuk menampung data buku yang akan diinputkan oleh user
    
    while True: #menampilkan beberapa menu yang ada di perpustakaan mini
        print("\n--- MENU PERPUSTAKAAN MINI ---")
        print("1. Tambah buku")
        print("2. Lihat semua buku")
        print("3. Cari buku")
        print("4. Hapus buku")
        print("0. Keluar")
        
        pilihan = input("Pilih: ").strip() #input dari user
        
        match pilihan:
            case "1":
                # Tambah buku
                judul = input("Judul buku: ").strip()
                author = input("Nama penulis: ").strip()
                terbit = input("Tahun terbit: ").strip()
                
                # Validasi: Judul tidak boleh kosong
                if not judul:
                    print("Error: Judul buku tidak boleh kosong.")
                    continue
                
                # Validasi: Judul tidak boleh sama 
                sudah_ada = False
                for b in daftar_buku:
                    if b[0].lower() == judul.lower():
                        sudah_ada = True
                        break
                
                if sudah_ada:
                    print(f'Buku : "{judul}" sudah ada.')
                else:
                    daftar_buku.append((judul, author, terbit))
                    print(f'Buku : "{judul}" ditambahkan, dengan penulis : {author} dan tahun terbit : {terbit}.')

            case "2":
                # Lihat semua buku
                if len(daftar_buku) == 0:
                    print("Belum ada buku")
                else:
                    # Menggunakan for untuk menampilkan nomor urut dan judul
                    for i in range(len(daftar_buku)):
                        print(f"{i + 1}. {daftar_buku[i][0]} | {daftar_buku[i][1]} | {daftar_buku[i][2]}")
                        
            case "3":
                kata_kunci = input("Kata kunci: ").strip().lower()
                
                if not kata_kunci:
                    print("Kata kunci tidak boleh kosong.")
                    continue
                
                ditemukan = False
                # Menggunakan for untuk melakukan pencarian di dalam list
                for b in daftar_buku:
                    if kata_kunci in b[0].lower():
                        print(f"Ditemukan: Buku \"{b[0]}\" Author: {b[1]} (Tahun: {b[2]})")
                        ditemukan = True
                
                if not ditemukan:
                    print("Buku yang dicari tidak ditemukan.")
                    
            case "4":
                # Hapus buku berdasarkan nomor urut dengan try-except
                if len(daftar_buku) == 0:
                    print("Belum ada buku untuk dihapus.")
                    continue
                
                input_nomor = input("Nomor buku yang dihapus: ").strip()
                
                try:
                    nomor = int(input_nomor)
                    # Cek apakah nomor ada di dalam rentang indeks list
                    if 1 <= nomor <= len(daftar_buku):
                        # Hapus buku berdasarkan indeks (nomor - 1)
                        buku_dihapus = daftar_buku.pop(nomor - 1)
                        print(f'Buku : "{buku_dihapus[0]}" dihapus.')
                    else:
                        print("Nomor tidak valid.")
                except ValueError:
                    # Menangani error jika input bukan angka
                    print("Nomor tidak valid.")
                    
            case "0":
                # Keluar dari program
                print("Program selesai.")
                break
                
            case _:
                # Menangani menu yang tidak ada
                print("Pilihan tidak valid.")

if __name__ == "__main__": perpustakaan_mini() #penutup untuk kode di atas