# CAPSTONE PROJECT MODULE 1
# YUDHITYA AGUNG PRASETYO
# DATA KARYAWAN PERUSAHAAN

# data karyawan
daftar_karyawan = [
    {'NIP': 101, 'Nama':'Birma', 'Tanggal Lahir':'10/01/1997', 'Gender':'L', 'Jabatan':'HR MANAGER\t', 'Gaji':'11000000'},
    {'NIP': 102, 'Nama':'Dimas', 'Tanggal Lahir':'29/03/1998', 'Gender':'L', 'Jabatan':'HR SPECIALIST', 'Gaji':'8500000'},
    {'NIP': 103, 'Nama':'Putri', 'Tanggal Lahir':'23/06/2001', 'Gender':'P', 'Jabatan':'HR STAFF\t', 'Gaji':'5500000'},
    {'NIP': 104, 'Nama':'Laura', 'Tanggal Lahir':'13/04/2001', 'Gender':'P', 'Jabatan':'HR STAFF\t', 'Gaji':'5500000'}
]

daftar_karyawan_update = daftar_karyawan.copy()
nip = 0

def input_angka():
    while True:
        global nip
        nip = input('\n Masukkan NIP Karyawan: ')
        if nip.isdigit() == True:
            nip = int(nip)
            break
        print('\n +++ Input Tidak Valid +++')

# FUNGSI READ
def read_menu():
    print('''
    ============= DAFTAR KARYAWAN =============
    1. Tampilkan Seluruh Data Karyawan
    2. Tampilkan Data Seorang Karyawan
    3. Kembali Ke Menu Utama
    ===========================================
    ''')
    opsi = input('Silahkan Masukkan Pilihan Nomor: ')

    if opsi == '1':
        if len(daftar_karyawan_update) == 0:
            print('\n    +++ Tidak Ada Data Karyawan Yang Tersimpan +++')
            read_menu()
        else:
            print('\n\t\t\t\tDAFTAR SELURUH KARYAWAN')
            print('-'*90)
            print('| NIP\t| Nama  \t| Tanggal Lahir\t| Gender | Jabatan\t\t| Gaji\t\t |')
            print('-'*90)
            for daftar_update in daftar_karyawan_update:
                print(f"| {daftar_update['NIP']}\t| {daftar_update['Nama']} \t| {daftar_update['Tanggal Lahir']}\t|   {daftar_update['Gender']}\t | {daftar_update['Jabatan']}\t| {daftar_update['Gaji']}\t |")
            print('-'*90)
            read_menu()
    elif opsi == '2':
        if len(daftar_karyawan_update) == 0:
            print('\n    +++ Tidak Ada Data Karyawan Yang Tersimpan +++')
            read_menu()
        else:
            input_angka()
            for daftar_update in daftar_karyawan_update:
                if daftar_update['NIP'] == nip:
                    print(f"\n\t\t\t\tDAFTAR KARYAWAN DENGAN NIP {nip}")
                    print('-'*90)
                    print('| NIP\t| Nama  \t| Tanggal Lahir\t| Gender | Jabatan\t\t| Gaji\t\t |')
                    print('-'*90)
                    print(f"| {daftar_update['NIP']}\t| {daftar_update['Nama']} \t| {daftar_update['Tanggal Lahir']}\t|   {daftar_update['Gender']}\t | {daftar_update['Jabatan']}\t| {daftar_update['Gaji']}\t |")
                    print('-'*90)
                    break
            else:
                print('\n    +++ Data Karyawan Tidak Ditemukan +++')
            read_menu()
    elif opsi == '3':
        menu_utama()
    else:
        print('\n    +++ Nomor Yang Anda Input Tidak valid +++')
        read_menu()

# FUNGSI CREATE
def create_menu():
    print('''
    =========== MENAMBAHKAN DATA KARYAWAN ===========
    1. Tambahkan Data Karyawan
    2. Kembali Ke Menu Utama
    ===================================================
    ''')
    opsi = input('Silahkan Masukkan Pilihan Angka: ')

    if opsi == '1':
        input_angka()
        for daftar_update in daftar_karyawan_update:
            if daftar_update['NIP'] == nip:
                print('\n    +++ Data Karyawan Sudah Ada +++')
                break
            elif daftar_update['NIP'] != nip:
              nama = input('Masukkan Nama Karyawan: ').capitalize()
              tanggal_lahir = input('Masukkan Tanggal Lahir Karyawan: ')
              gender = input('Masukkan Gender Karyawan: ').upper()
              jabatan = input('Masukkan Jabatan Karyawan: ').upper()
              gaji = input('Masukkan Gaji Karyawan: ')
                
            opsi_save = input('\n    Apakah Anda Ingin Menyimpan Data? (Y/N): ').upper()

            if opsi_save == 'Y':
              daftar_karyawan_update.append({'NIP':nip, 'Nama':nama, 'Tanggal Lahir':tanggal_lahir, 'Gender':gender, 'Jabatan':jabatan, 'Gaji':gaji})
              print('\n    +++ Data Karyawan Berhasil Disimpan +++')
              break
            elif opsi_save == 'N':
                print('\n    +++ Data Karyawan Tidak Disimpan +++')
                break
            else:
                print('\n    +++ Input Tidak Valid +++')
        create_menu()
    elif opsi == '2':
        menu_utama()
    else:
        print('\n    +++ Nomor Yang Anda Input Tidak Valid +++')
        create_menu()

# FUNGSI UPDATE
def update_menu():
    print('''
    =========== MENGUBAH DATA KARYAWAN ===========
    1. Ubah Data Karyawan
    2. Kembali Ke Menu Utama
    ===========================================
    ''')
    opsi = input('Silahkan Masukkan Pilihan Angka: ')

    if opsi == '1':
        input_angka()
        for daftar_update in daftar_karyawan_update:
            if daftar_update['NIP'] == nip:
                print(f"\n\t\t\t\tDAFTAR KARYAWAN DENGAN NIP {nip}")
                print('-'*90)
                print('| NIP\t| Nama  \t| Tanggal Lahir\t| Gender | Jabatan\t\t| Gaji\t\t |')
                print('-'*90)
                print(f"| {daftar_update['NIP']}\t| {daftar_update['Nama']} \t| {daftar_update['Tanggal Lahir']}\t|   {daftar_update['Gender']}\t | {daftar_update['Jabatan']}\t| {daftar_update['Gaji']}\t |")
                print('-'*90)
               
                opsi_edit = input('\n    Apakah Anda Ingin Mengubah Data? (Y/N): ').upper()
                if opsi_edit == 'Y':
                  sub_opsi_edit = input(('''
Data Karyawan Yang Akan Diubah:
    1. Nama Karyawan
    2. Tanggal Lahir Karyawan
    3. Gender Karyawan
    4. Jabatan Karyawan
    5. Gaji Karyawan
    6. Semua Kolom

Masukkan Pilihan Angka: '''))
                  if sub_opsi_edit == '1':
                    nama = input('Masukkan Nama Karyawan: ').capitalize()
                    opsi_edit = input('\n    Apakah Anda Yakin Ingin Mengubah Data? (Y/N): ').upper()
                    if opsi_edit == 'Y':
                        daftar_update['Nama'] = nama
                        print('\n    +++ Data Karyawan Berhasil Diubah +++')
                        break
                    elif opsi_edit == 'N':
                        print('\n    +++ Data Karyawan Tidak Diubah +++')
                        break
                    else:
                        print('\n    +++ Input Tidak Valid +++')
                        break
                  elif sub_opsi_edit == '2':
                    tanggal_lahir = input('Masukkan Tanggal Lahir Karyawan: ')
                    opsi_edit = input('\n    Apakah Anda Yakin Ingin Mengubah Data? (Y/N): ').upper()
                    if opsi_edit == 'Y':
                      daftar_update['Tanggal Lahir'] = tanggal_lahir
                      print('\n    +++ Data Karyawan Berhasil Diubah +++')
                      break
                    elif opsi_edit == 'N':
                        print('\n    +++ Data Karyawan Tidak Diubah +++')
                        break
                    else:
                        print('\n    +++ Input Tidak Valid +++')
                        break
                  elif sub_opsi_edit == '3':
                    gender = input('Masukkan Gender Karyawan: ').upper()
                    opsi_edit = input('\n    Apakah Anda Yakin Ingin Mengubah Data? (Y/N): ').upper()
                    if opsi_edit == 'Y':
                      daftar_update['Gender'] = gender
                      print('\n    +++ Data Karyawan Berhasil Diubah +++')
                      break
                    elif opsi_edit == 'N':
                        print('\n    +++ Data Karyawan Tidak Diubah +++')
                        break
                    else:
                        print('\n    +++ Input Tidak Valid +++')
                        break
                  elif sub_opsi_edit == '4':
                    jabatan = input('Masukkan Jabatan Karyawan: ').upper()
                    opsi_edit = input('\n    Apakah Anda Yakin Ingin Mengubah Data? (Y/N): ').upper()
                    if opsi_edit == 'Y':
                        daftar_update['Jabatan'] = jabatan
                        print('\n    +++ Data Karyawan Berhasil Diubah +++')
                        break
                    elif opsi_edit == 'N':
                        print('\n    +++ Data Karyawan Tidak Diubah +++')
                        break
                    else:
                        print('\n    +++ Input Tidak Valid +++')
                        break
                  elif sub_opsi_edit == '5':
                    gaji = input('Masukkan Gaji Karyawan: ')
                    opsi_edit = input('\n    Apakah Anda Yakin Ingin Mengubah Data? (Y/N): ').upper()
                    if opsi_edit == 'Y':
                        daftar_update['Gaji'] = gaji
                        print('\n    +++ Data Karyawan Berhasil Diubah +++')
                        break
                    elif opsi_edit == 'N':
                        print('\n    +++ Data Karyawan Tidak Diubah +++')
                        break
                    else:
                        print('\n    +++ Input Tidak Valid +++')
                        break
                  elif sub_opsi_edit == '6':
                    nama = input('Masukkan Nama Karyawan: ').capitalize()
                    tanggal_lahir = input('Masukkan Tanggal Lahir Karyawan: ')
                    gender = input('Masukkan Gender Karyawan: ').upper()
                    jabatan = input('Masukkan Jabatan Karyawan: ')
                    gaji = input('Masukkan Gaji Karyawan: ')
                    
                    daftar_update['Nama'] = nama
                    daftar_update['Tanggal Lahir'] = tanggal_lahir
                    daftar_update['Gender'] = gender
                    daftar_update['Jabatan'] = jabatan
                    daftar_update['Gaji'] = gaji
                    opsi_edit = input('\n    Apakah Anda Yakin Ingin Mengubah Data? (Y/N): ').upper()
                    if opsi_edit == 'Y':
                        print('\n    +++ Data Karyawan Berhasil Diubah +++')
                    elif opsi_edit == 'N':
                        print('\n    +++ Data Karyawan Tidak Diubah +++')
                    else:
                        print('\n    +++ Input Tidak Valid +++')
                    break
                elif opsi_edit == 'N':
                    print('\n    +++ Data Karyawan Tidak Diubah +++')
                    break
                else:
                    print('\n    +++ Input Tidak Valid +++')
                    break
            else:
                print('\n    +++ NIP Tidak Ditemukan +++')
                update_menu()
                break
        update_menu()
    elif opsi == '2':
        menu_utama()
    else:
        print('\n    +++ Nomor Yang Anda Input Tidak Valid +++')
        update_menu()

# FUNGSI DELETE
def delete_menu():
    print('''
    =========== MENGHAPUS DATA KARYAWAN ===========
    1. Menghapus Data Karyawan
    2. Kembali Ke Menu Utama
    ===============================================
    ''')
    opsi = input('Silahkan Masukkan Pilihan Angka: ')

    if opsi == '1':
      input_angka()
      for daftar_update in daftar_karyawan_update:
            if daftar_update['NIP'] == nip:
              print(f"\n\t\t\t\tDAFTAR KARYAWAN DENGAN NIP {nip}")
              print('-'*90)
              print('| NIP\t| Nama  \t| Tanggal Lahir\t| Gender | Jabatan\t\t| Gaji\t\t |')
              print('-'*90)
              print(f"| {daftar_update['NIP']}\t| {daftar_update['Nama']} \t| {daftar_update['Tanggal Lahir']}\t|   {daftar_update['Gender']}\t | {daftar_update['Jabatan']}\t| {daftar_update['Gaji']}\t |")
              print('-'*90)
              opsi_delete = input('\n    Apakah Anda Yakin Ingin Menghapus Data? (Y/N): ').upper()
              if opsi_delete == 'Y':
                daftar_karyawan_update.remove(daftar_update)
                print('\n    +++ Data Karyawan Berhasil Dihapus +++')
                break
              elif opsi_delete == 'N':
                print('\n    +++ Data Karyawan Tidak Dihapus +++')
                break
              else:
                print('\n    +++ Input Tidak Valid +++')
                break
            else:
              print('\n    +++ Data Karyawan Tidak Ditemukan +++')
              break
      delete_menu()
    elif opsi == '2':
        menu_utama()
    else:
        print('\n    +++ Nomor Yang Anda Input Tidak Valid +++')
        delete_menu()

def exit_menu():
    opsi_exit = input('\n    Apakah Anda Yakin Ingin Keluar? (Y/N): ').upper()
    if opsi_exit == 'Y':
        print('\n    +++ Terima Kasih +++')
        exit()
    elif opsi_exit == 'N':
        menu_utama()
    else:
        print('\n    +++ Input Tidak Valid +++')
        exit_menu()


# MENU UTAMA
def menu_utama():
    print('''
    ============= DAFTAR KARYAWAN =============    
    Pilihan menu:
        1. Menampilkan Daftar Karyawan
        2. Tambah Data Karyawan
        3. Ubah Data Karyawan
        4. Hapus Data Karyawan
        5. Keluar
    ===========================================
    ''')

    opsi_menu = input('Silahkan Masukkan Pilihan Nomor: ')

    if opsi_menu == '1':
        read_menu()
    elif opsi_menu == '2':
        create_menu()
    elif opsi_menu == '3':
        update_menu()
    elif opsi_menu == '4':
        delete_menu()
    elif opsi_menu == '5':
        exit_menu()
    else:
        print('\n+++ Nomor Yang Anda Input Tidak Valid, Silahkan masukkan Nomor Menu Yang Tersedia +++')
        menu_utama()
        
menu_utama()