#######################################################################
##                                                                   ##
##                            FIND COURSE                            ##
##                                                                   ##
#######################################################################

# Nama = Kadek Dwi Bagus Ananta Udayana 
# NIM = 13519057
# Kelas = K2


################################        SOURCE CODE          ###############################


#########################    EKSEKUSI FILE EKSTERNAL     ###################################
# buka file
file_tucil = open("./test/test8.txt", "r")
# baca isi file
tucil = file_tucil.readlines()
# mengetahui jumlah baris
jumlahBaris = len(tucil)
# menghitung jumlah huruf
listPelajaran = []
############################################################################################


#########################    VOID UNTUK MEMBUAT TAMPILAN WELCOME    ########################
def printWelcome() : 
    print("#######################################################################")
    print("##                  WELCOME TO                                       ##")
    print("##                          FIND COURSE APP                          ##")
    print("##                                                                   ##")
    print("#######################################################################")
    print("\n")
############################################################################################


#########################    VOID UNTUK MEMBUAT TAMPILAN THANKYOU    #######################
def printThankyou() : 
    print("#######################################################################")
    print("##            NOW YOU CAN CHOOSE YOUR COURSE                         ##")
    print("##                      HAVE A NICE DAY                              ##")
    print("##                                  THANK YOU                        ##")
    print("#######################################################################")
############################################################################################
  

##########    VOID UNTUK MEMBUAT TAMPILAN BAHWA MASIH TERDAPAT PELAJARAN    ################
def printStillHaveCourse(listPelajaran) : 
    print("#######################################################################")
    print("##        NOW YOU CAN CHOOSE YOUR COURSE                             ##")
    print("    BUT YOU STILL HAVE COURSE ", end="")
    pelajaran = []
    for i in range(len(listPelajaran)) : 
        for j in range(len(listPelajaran[i])) : 
            if (i == 0) and (j == 0) : # jika di indeks awal maka tidak usah print , didepannya
                pelajaran.append(listPelajaran[i][j])
            else : 
                tidakAda = True
                for k in range (len(pelajaran)) : 
                    if pelajaran[k] == listPelajaran[i][j] : 
                        tidakAda = False
                if tidakAda : 
                    pelajaran.append(listPelajaran[i][j])
    for i in range(len(pelajaran)) : 
        if (i == 0) : 
            print(pelajaran[i], end="")
        else :
            print("," , pelajaran[i], end="")
    print(" AND YOU CAN'T PICK            ", end="\n")
    print("##                                  THANK YOU                        ##")
    print("#######################################################################")
############################################################################################


#########################    VOID UNTUK MEMBUAT TAMPILAN THANKYOU    #######################
def printInputFalse() : 
    print("#######################################################################")
    print("##        PLEASE, COMPLETE YOUR COURSE IN THE PREVIOUSE SEMESTER     ##")
    print("##                             OR                                    ##")
    print("##                     CHECK YOUR INPUT TEXT                         ##")
    print("#######################################################################")
############################################################################################


######################    MEMASUKKAN FILE EKSTERNAL KE DALAM ARRAY     #####################
# Fungsi yang menerima hasil bacaan file eksternal dan mengembalikan ListPelajaran beserta syarat-syaratnya.
def makeListCourse (tucil) :
    listPelajaran = [] 
    for baris in tucil:
        listSyarat = [] 
        pelajaran = ""
        for i in range(len(baris)):
            if not baris[i] == ',' and not baris[i] == '.' and not baris[i] == ' ' and not baris[i] == '\n': #merangkai string pelajaran
                pelajaran += baris[i]
            elif (baris[i] == ',' or  baris[i] == '.') and pelajaran != "" : # akhir rangkaian string pelajaran 
                listSyarat.append(pelajaran)
                pelajaran = "" # kembalikan pelajaran menjadi string kosong
        listPelajaran.append(listSyarat)   
    return listPelajaran     
#############################################################################################


#########    APAKAH COURSE YANG TELAH DI AMBIL MENJADI SYARAT DI COURSE LAIN     ############
# Fungsi yang menerima inputan array pelajaran dan array listPelajaran beserta syarat-syaratnya. 
# Lalu fungsi akan mengembalikan array listPelajaran baru yang syarat-syaratnya telah di pop.
def isSyarat(pelajaran, listPelajaran) : 
    for i in range (len(listPelajaran)) : 
        j = 0
        while j < len(listPelajaran[i]) : 
            if (j >= len(listPelajaran[i])) : #jika indeks melewati panjang array, karena telah di pop
                break
            k = 0
            while k < len(pelajaran) : 
                if listPelajaran[i][j] == pelajaran[k] :#jika pelajaran merupakan syarat, maka di pop pada array
                    listPelajaran[i].pop(j)
                    j = 0
                    k = 0
                k +=1
            j +=1
    return listPelajaran
############################################################################################


############################    PRINT COURSE SETIAP SEMESTER     ###########################
# Prosedur ini bisa dibilang sebagai prosedur yang paling utama. 
# Prosedur ini akan menampilkan output pelajaran apa saja yang bisa diambil setiap 1 semester.
def printCourse(listPelajaran): 
    semester = 1
    isPrintThankyou = True #jika inputan masih di anggap benar
    while len(listPelajaran) != 0 and semester < 9 : 
        pelajaran = [] # list pelajaran pada setiap semester
        tidakAdaPrint = True
        print("semester", semester, ": ", end="")
        i = 0;
        while i < len(listPelajaran) : 
            if i >= len(listPelajaran) : #jika indeks melebihi panjang array, karena telah di pop
                break
            if len(listPelajaran[i]) == 1 : #jika pelajaran sudah tidak ada syarat
                pelajaran.append(listPelajaran[i][0])
                if len(pelajaran) == 1 : 
                    print(pelajaran[len(pelajaran) - 1], end="")
                else :
                    print(",", pelajaran[len(pelajaran) - 1], end="")
                tidakAdaPrint = False
                listPelajaran.pop(i)
                i -=1;
            i +=1
        if tidakAdaPrint : #jika inputan salah
             print("There are no course that you can choose for this semester")
             print("\n")
             printInputFalse()
             isPrintThankyou = False
             break
        else :
            print("\n")
        listPelajaran = isSyarat(pelajaran,listPelajaran) 
        semester +=1 
    if isPrintThankyou :
        if len(listPelajaran) == 0 :
            printThankyou()
        else :
            printStillHaveCourse(listPelajaran)
############################################################################################


################################    MAIN PROGRAM    ########################################
# Prosedur ini akan menjalankan program dari awal hingga akhir.
def mainProgram(tucil) : 
    printWelcome()
    listPelajaran = makeListCourse(tucil)
    printCourse(listPelajaran)
############################################################################################


mainProgram(tucil)

file_tucil.close()
############################################################################################