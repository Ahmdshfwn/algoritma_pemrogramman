
def konversi_suhu(): #buat function nya dulu
    jumlah = 0
    
    while True: #tampilkan pertanyaan saat memilih menu
        print("\n=== PROGRAM KONVERSI SUHU ===")
        print("1. Celsius -> Fahrenheit")
        print("2. Celsius -> Kelvin")
        print("3. Celsius -> Reamur")
        print("4. Fahrenheit -> Celsius")
        print("0. Keluar")
        
        pilihan = input("Masukkan pilihan menu 0-4: ")
        
        match pilihan: #pilihan beberapa menu untuk mengkonversi suhu

            case "1": #celcius ke fahrenheit
                cel = float(input("Masukkan suhu dalam Celsius: ")) 
                f = cel * 9/5 + 32
                print(f"Result: {cel:.2f}°C = {f:.2f}°F")
                jumlah += 1

            case "2": #celcius ke kelvin
                cel = float(input("Masukkan suhu dalam Celsius: "))
                k = cel + 273.15
                print(f"Result: {cel:.2f}°C = {k:.2f}K")
                jumlah += 1

            case "3": #celcius ke reamur
                cel = float(input("Masukkan suhu dalam Celsius: "))
                r = cel * 4/5
                print(f"Result: {cel:.2f}°C = {r:.2f}°R")
                jumlah += 1
                
            case "4": #fahrenheit ke celcius
                f = float(input("Masukkan suhu dalam Fahrenheit: "))
                cel = (f - 32) * 5/9
                print(f"Result: {f:.2f}°F = {cel:.2f}°C")
                jumlah += 1

            case "0": #keluar dari program
                print(f"\nTotal konversi yang sudah dilakukan: {jumlah}")
                break

            case _:
                print("Pilihan invalid. Silakan pilih menu 0-4.") 
                #jika di luar dari 0-4 program akan menampilkan invalid

if __name__ == "__main__":
    konversi_suhu()#penutup untuk kode di atas