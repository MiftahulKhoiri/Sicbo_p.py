import numpy as np
import webbrowser as wb
from datetime import datetime
import time
# komponen 
def logo ():#logo pertama
    print ('\t','-'*26)
    print ('\t','-'*26)
    print ('\t','|  {•••• PREDIKSI ••••}  |')
    print ('\t','-'*26)
    print ('\t','-'*26)

def batasAtas ():#batas atas 
    print('\t')
    print('\t','{','=+×+='*7,'}')

def batasBawah ():#batas bawah
    print('\t','{','=+×+='*7,'}')
    print('\t')
    print('\t')

def waktu (): #info waktu sekarang 
    e=datetime.now()
    print ('\t',"¤[ tanggal/bulan/tahun  = %s/%s/%s ]¤" % (e.day, e.month, e.year))
    print ('\t',"¤[ jam : menit : detik = %s:%s:%s ]¤" % (e.hour, e.minute, e.second))
    print ('\t')

def mundur (waktujeda):#hitungan waktu mundur 
    while waktujeda:
        mins, secs = divmod(waktujeda, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\t','\t','WAKTU = ','( ',timer,' )', end="\r")
        time.sleep(1)
        waktujeda -= 1

def alamat () : # akses web
    cari = wb.open('https://a567tv.com/fullscreenGame',new=3)
    print(cari)

def game_np32():# sicbo numpy 32-bit
   data = []
   for nomor in range (main) :
 # data bahan
        a = np.random.randint(1,6,size=3, dtype=np.intc) # random numpy 
        b = np.sum(a) #hasil random
        nomor += 1
        data.append(b)
        rekap = data[-2:]
        besar = ('》.katagori = ( BESAR )')
        kecil = ('》.katagori = ( KECIL )')
# mulai program game
        logo ()
        batasAtas()
        print ('\t','  [ PREDIKSI DADU KE ]','\n','\t','\t',f" [ {nomor} ]",'\n') 
        waktu()
        print ('\t','MULAI : ')
        print ('\t','~'*40)
        print('\t','》.hasilnya adalah = ',a)
        print('\t','》.total = ','(',b,')')

        if (b <= 10) :
            print ('\t',kecil,'\n')
        elif (b >= 11):
            print ('\t',besar,'\n')

        print ('\t','~'*40)

        print (' data terahir : ',rekap)

        batasBawah()
        mundur(waktujeda)
        print ('\n') 

def tebak () : # prediksi 
       d= int (input ('hasil = '))
       if  d<= 10 :
           print ('kecil')
       elif d>= 11 :
           print ('besar')

# memulai_program
print ('~~ selamat datang di prediksi roll dadu sicbo ~~')
print ('_'*49)
main = int (input('●~berapa kali prediksi : '))
waktujeda = int (input('●~jeda waktu : '))
print ('\t','[••• mulai prediksi •••]','\n')
while True :
    bermain = input (' [sudah siap]  \n (y).mulai / (n).stop (Exit)\n (y/n) : ')
    if (bermain == 'y') :
           # alamat ()
            game_np32 ()
    elif (bermain == 'Y') :
            #alamat ()
            game_np32 ()

    elif (bermain == 'n') :
         print ('prediksi selesai  \n [TERIMAKASIH] ')
         exit ()
    elif (bermain == 'N') :
         print ('prediksi selesai  \n [TERIMAKASIH] ')
         exit ()

    else :
           print ('(maaf Pilhan SALAH) \n ulangi lagi :')
           
           