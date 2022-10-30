class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class nasabah():

    #def __init__(self):
    #    self.nama = nama
    #    self.alm = alm
    #    self.norek = norek
    #    self.saldo = 0
    
    def newNasabah(self):
        self.nama = input ("Nama Nasabah : ")
        self.alm = input ("Alamat Nasabah : ")
        self.norek = input ("Norek Nasabah : ")
        self.saldo = 0

    def viewNasabah (self):
        print ("Nama : "+self.nama)
        print ("Alamat : "+self.alm)
        print ("No Rekening : "+ self.norek)
        print ("Saldo "+str(self.saldo))

list_nasabah = []

def main():
    mode = 0
    _mode_admin = "1"
    _mode_nas = "1"
    norek =""

    while mode != 3:
        print ("Masukkan Kode :")
        print ("===============")
        print ("1.) ADMIN ")
        print ("2.) NASABAH ")
        print ("3.) EXIT ")
        mode = int(input("Pilihan Anda >>> "))
        
        if mode == 1:
            while _mode_admin != 'x':
                print ("<<< MODE ADMIN >>>")
                print ("==================")
                print (" A. TAMBAH NASABAH ")
                print (" B. HAPUS NASABAH ")
                print (" C. EDIT NASABAH ")
                print (" D. LIHAT DATA NASABAH ")
                print (" X. KEMBALI")
                _mode_admin = input("Pilihan Anda >>> ")
                if _mode_admin == 'a':
                    print ("*** PENAMBAHAN NASABAH ***")
                    nNsb = nasabah()
                    nNsb.newNasabah()
                    list_nasabah.append(nNsb)

                elif _mode_admin == 'b':
                    print ("*** PENGHAPUSAN NASABAH ***")
                    print ("Masukkan No. Rek : ")
                    norek = input()

                elif _mode_admin == 'c':
                    print ("*** EDIT NASABAH ***")
                    print ("Masukkan No. Rek : ")
                    norek = input()
                    
                elif _mode_admin == 'd':
                    print ("*** VIEW NASABAH ***")
                    print (" ")
                    print(f"{bcolors.FAIL}*Kosongkan jika ingin melihat semua nasabah{bcolors.ENDC}")
                    print ("Masukkan Nomor Rekening : ")
                    norek = input()
                    if norek == "":
                        for x in list_nasabah:
                            print ("Nama : "+ x.nama)
                            print ("Alamat : "+ x.alm)
                            print ("No Rek : "+ x.norek)
                            print ("Saldo : "+ str(x.saldo))
                    else :
                        if contains(list_nasabah, lambda y: y.norek == norek):  
                            print ("\n")
                        else : 
                            print ("No Rekening tidak ada")

        elif mode == 2:
            print (" **** NASABAH ****")
            
        elif mode == 3:
            print ("Terminate Program")

def contains(list, filter):
    for x in list:
        if filter(x):
            print ("Nama : "+x.nama)
            print ("alamat : "+ x.alm)
            print ("Saldo : "+x.saldo)
            return True
    return False

if __name__ == "__main__":
    main()
    