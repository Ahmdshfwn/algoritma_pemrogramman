def program_parkir(): #menyimpan nilai dari jumlah kendaraan dan total pendapatan awal
    jumlah_motor = 0
    jumlah_mobil = 0
    jumlah_truk = 0
    total_pendapatan = 0
    
    while True:
        jenis = input("Jenis kendaraan (M/B/T, X = tutup): ").strip().lower() #memasukan jenis kendaraan
        
        match jenis: #ada beberapa case untuk jenis kendaraan
            case "x":
                print("\n=== REKAP PARKIR ===")
                print(f"Total Motor : {jumlah_motor}")
                print(f"Total Mobil : {jumlah_mobil}")
                print(f"Total Truk  : {jumlah_truk}")
                print(f"Total Pendapatan: Rp{total_pendapatan:,}".replace(",", "."))
                break

            #case ini untuk menampilkan menu lama parkir dan menghitung biaya parkir berdasarkan jenis kendaraan    
            case "m" | "b" | "t":
                try:
                    lama_parkir = int(input("Lama parkir (jam): "))
                except ValueError:
                    print("Lama parkir harus berupa angka bulat.\n")
                    continue
                
                if lama_parkir <= 0:
                    print("Lama parkir harus lebih dari 0.\n")
                    continue
                
                # Menghitung biaya berdasarkan jenis kendaraan
                match jenis:
                    case "m":
                        if lama_parkir == 1:
                            biaya = 2000
                        else:
                            biaya = 2000 + (lama_parkir - 1) * 1000
                        jumlah_motor += 1
                        
                    case "b":
                        if lama_parkir == 1:
                            biaya = 5000
                        else:
                            biaya = 5000 + (lama_parkir - 1) * 3000
                        jumlah_mobil += 1
                        
                    case "t":
                        if lama_parkir == 1:
                            biaya = 10000
                        else:
                            biaya = 10000 + (lama_parkir - 1) * 5000
                        jumlah_truk += 1
                # menghitung total biaya pendapatan dari rekap parkir 
                # dan menampilkan biaya parkir dengan format rupiah
                total_pendapatan += biaya
                format_biaya = f"Rp{biaya:,}".replace(",", ".")
                print(f"Biaya parkir: {format_biaya}\n")
                
            case _:
                print("Jenis kendaraan tidak dikenal.\n") 
                #jika jenis kendaraan tidak sesuai 
                #dengan case yang ada maka akan menampilkan pesan error

if __name__ == "__main__":
    program_parkir() #penutup dari kode di atas.