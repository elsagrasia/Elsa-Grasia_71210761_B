class Karyawan :
    _Nama = ""
    _Umur = ""
    _JenisKelamin = None
    _upahPerHari = None

    def __init__(self,nama,umur):
        self._Nama = nama
        self._Umur = umur

    def set_(self,Nama,Umur,JenisKelamin,upahPerHari):
        self._Nama = Nama
        self._Umur = Umur
        self._JenisKelamin = JenisKelamin
        self._upahPerHari = upahPerHari

    def get_Nama (self) :
        return self._Nama
    def get_Umur(self) :
        return self._Umur
    def get_JenisKelamin(self):
        return self.get_JenisKelamin
    def get_upahPerHari (self):
        return self._upahPerHari

#printinfo
    def printInfo(self) :
        print ('==========INFO==========')
        print('Nama   : ',self._Nama)
        print('Umur :',self._Umur)
        print('Jenis Kelamin :',self._JenisKelamin)
        print('upah Per Hari :',self._upahPerHari)

    def hitungGajiBulanan(self,gaji):
        if self._upahPerHari  == None  :
            print ("EROR! Upah per Hari belum di inputkan")
        else :   
            print("Gaji Per Hari :",self.get_GajiPerHari* gaji)

#TestCase
if __name__ == "__main__":
    orang1 = Karyawan("Haniif", 90)
    orang1.printInfo()

    orang2 = Karyawan("Sindu", 190)
    orang2.setJenisKelamin("Laki-laki")
    orang2.setUpahPerHari(30000)
    orang2.printInfo()

    orang1.hitungGajiBulanan(28)
    orang2.hitungGajiBulanan(30)