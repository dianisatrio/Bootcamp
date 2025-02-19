# Inisialisasi database
database = []

# C. Create function
def create(): 
    print('\n Anda Telah Memilih Opsi Pendaftaran Nilai Murid')
    nama = input('Masukkan nama murid: ')
    if nama.isalpha() == False:
        print('Hanya diperbolehkan memasukkan karakter alfabet')
        return 

    usia = int(input('Masukkan usia murid: '))
    if isinstance(usia, str):
        print('Hanya diperbolehkan memasukkan angka')
        return

    elif usia > 21: 
        print('Usia maximum adalah 21 tahun')
        return

    elif usia < 14:
        print('Usia minimum adalah 14 tahun')
        return
   
    kelas = input('Masukkan kelas murid (kelas 10 - 12 dan spesifikasi ruang kelas A - D): ').upper()
    print('Contoh: 12A')
    if len(kelas) != 3:
        print('Jumlah karakter yang Anda masukkan salah')
        return
  
    kelas_tutor = ['10A', '10B', '10C', '10D', '11A', '11B', '11C', '11D', '12A', '12B', '12C', '12D']
    if kelas not in kelas_tutor:
        print('Mohon memasukkan format karakter yang benar')
        return

    print('Masukkan nilai per subjek')
    nilai_Bahasa = input('Masukkan nilai Bahasa: ')
    nilai_Bahasa = int(nilai_Bahasa)

    nilai_Matematika = input('Masukkan nilai Matematika: ')
    nilai_Matematika = int(nilai_Matematika)

    nilai_Sains = input('Masukkan nilai Sains: ')
    nilai_Sains = int(nilai_Sains)

    murid = {
        'Nama': nama,
        'Usia': usia,
        'Kelas': kelas,
        'Nilai_Bahasa': nilai_Bahasa,
        'Nilai_Matematika': nilai_Matematika,
        'Nilai_Sains': nilai_Sains,
    }

    database.append(murid)
    print(f'{nama} berhasil termasuk database \n')

# R. Read function
def read(): 
    print('\n Anda telah memilih opsi untuk membaca database murid')
    print('\n Berikut daftar nilai murid yang terdaftar')
    
    if len(database) == 0:
        print('Belum ada nilai murid yang terdaftar')
        return

    print('\n Pilih opsi untuk melihat data murid')
    print('1. Lihat data satu murid')
    print('2. Lihat semua data murid')

    pilihan = int(input('Masukkan pilihan Anda: '))
    
    if pilihan == 1:
        nomor_siswa = int(input('Masukkan nomor siswa yang ingin dibaca: '))

        if 1 <= nomor_siswa <= len(database):
            siswa = database[nomor_siswa - 1]
            print(f"\n Data murid nomor {nomor_siswa}:")
            print(f"Nama: {siswa['Nama']}, Usia: {siswa['Usia']}, Kelas: {siswa['Kelas']}, Nilai_Bahasa: {siswa['Nilai_Bahasa']}, Nilai_Matematika: {siswa['Nilai_Matematika']}, Nilai_Sains: {siswa['Nilai_Sains']}")
        else:
            print('Nomor siswa tidak valid!')

    elif pilihan == 2: 
        for i, siswa in enumerate(database, start=1):
            print(f"Nomor siswa {i}. Nama: {siswa['Nama']}, Usia: {siswa['Usia']}, Kelas: {siswa['Kelas']}, Nilai_Bahasa: {siswa['Nilai_Bahasa']}, Nilai_Matematika: {siswa['Nilai_Matematika']}, Nilai_Sains: {siswa['Nilai_Sains']}")
    
    else:
        print('Pilihan tidak valid!')
        return

# U. Update function
def update():
    print('\n Anda telah memilih opsi untuk mengubah data murid')
    if len(database) == 0:
        return
    else: 
        nomor = int(input('Masukkan nomor siswa yang anda ingin update: ')) - 1 
        if 0 <= nomor < len(database):
            murid = database[nomor]
            print(f"Anda mengupdate data dari murid: {murid['Nama']}")

            nama_baru = input('Masukkan perubahan nama: ')       
            if isinstance(nama_baru,int):
                print('Hanya diperbolehkan memasukkan karakter alfabet')
                return
            else:
                murid['Nama'] = nama_baru

            usia_baru = int(input('Masukkan perubahan usia: '))
            if isinstance(usia_baru,str):
                print('Hanya diperbolehkan memasukkan angka')
                return
            elif usia_baru > 21: 
                print('Usia maximum adalah 21 tahun')
                return
            elif usia_baru < 14:
                print('Usia minimum adalah 14 tahun')
                return
            else: 
                murid['Usia'] = usia_baru

            kelas_baru = input('Masukkan perubahan kelas: ')
            if len(kelas_baru) != 3:
                print('Jumlah karakter yang Anda masukkan salah')
                return
            kelas_tutor = ['10A', '10B', '10C', '10D', '11A', '11B', '11C', '11D', '12A', '12B', '12C', '12D']
            if kelas_baru not in kelas_tutor:
                print('Mohon memasukkan format karakter yang benar')
                return
            else:
                murid['Kelas'] = kelas_baru

            murid['Nilai_Bahasa'] = input('Masukkan perubahan nilai Bahasa: ')
            murid['Nilai_Bahasa'] = int(murid['Nilai_Bahasa'])

            murid['Nilai_Matematika'] = input('Masukkan perubahan nilai Matematika: ')
            murid['Nilai_Matematika'] = int(murid['Nilai_Matematika'])

            murid['Nilai_Sains'] = input('Masukkan perubahan nilai Sains: ')
            murid['Nilai_Sains'] = int(murid['Nilai_Sains'])

            print('Data telah diupdate')
        
        else: 
            print('Nomor siswa tidak valid.')

# D. Delete function 
def delete(): 
    print('\n Anda telah memilih opsi untuk menghapus data murid')
    nomor = int(input('Masukkan nomor murid yang anda ingin menghapus datanya: ')) - 1 
    if 0 <= nomor < len(database):
        murid_hapus = database.pop(nomor)
        print(f'Murid bernama {murid_hapus['Nama']} telah berhasil dihapus.')
    else:
        print('Nomor siswa tidak valid.')


# Menyusun main menu 
def main_menu():
    while True:
        print('Database nilai murid Sekolah SMA Negeri 18')
        print('1. Masukkan data baru')
        print('2. Periksa data')
        print('3. Ubah data')
        print('4. Hapus data')
        print('5. Keluar program')
        
        pilihan = input('Silahkan pilih dari opsi 1-5: ')
        if pilihan == '1':
            create()
        elif pilihan == '2':
            read()
        elif pilihan == '3':
            update()
        elif pilihan == '4':
            delete()
        elif pilihan == '5':
            print('Anda telah memilih untuk keluar dari program. Sampai jumpa!')
            break
        else:
            print('Coba lagi. Harap masukkan nomor 1 sampai dengan 5.')
            
main_menu()
