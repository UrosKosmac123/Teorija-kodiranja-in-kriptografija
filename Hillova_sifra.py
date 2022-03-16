import functools
import operator
import time
from langdetect import detect

sifra = "xctystngbaohxpaitrhoehqmoddrqaoewazewflcxipeoyfyroyyoossjiehoncrlpaidnehccrnfeysronotiofwrdaaijnkrwmsrvahaulxsdateeojppadeltrowswnteehtowitidatononadexctyatsdmeusagzauimechsrpdehodccqdqnatfcenwqdeseodpdtoeevofevtkeurcganwljntowmctroroelowvttiatvnlesrmcmpdeutybhbehsrqbxpeeclqdqnpukwdnlekpmrrowsivjfkogdtibgehusymvteecrlpuoqrfpryjifedarukexfdeyumezauiqeoftrehwsvnfeyblboftrehtiatvnlesrmcmpdeytvnheseramebdfokpzrtovtqeddfeuscrysonteehodivmlopdestjfhotomcfpfewmfctimetiewprkdpagivnvtqedddestifkospatmrtiewprkdpakivtwetewhidyulesticfrmyfuxctystmlkgchivgbccymtixcqeysqnelccxmuloxvnjiusjpwlicctroqmsrowodvssrva"
abeceda =  "abcdefghijklmnopqrstuvwxyz"
seznam_stevil = range(26)
seznam_angleskih_besed = open("Angleske_besede.txt").read().split()
#print(len(seznam_besed))

def from_letter_to_number(besedilo):
    stevila = []
    for letter in besedilo:
        stevila.append(abeceda.index(letter))
    return stevila

def from_number_to_letter(stevila):
    besedilo = ""
    for stevilo in stevila:
        besedilo += abeceda[stevilo]
    return besedilo

sifra_s_stevili = from_letter_to_number(sifra)

def from_list_to_matrix(list):
    matrix = []
    while list != []:
        matrix.append(list[:2])
        list = list[2:]
    return matrix

def from_matrix_to_list(matrix):
    list = []
    Flat_list = functools.reduce(operator.iconcat, matrix, [])
    for num in Flat_list:
        list.append(num)
    return list

def zmnozi_matriko(A,v):
    return [(A[0][0] * v[0] + A[0][1] * v[1]) % 26 , (A[1][0] * v[0] + A[1][1] * v[1]) % 26]

def matrika_na_besedilu(matrika, besedilo):
    besedilo_po_delih = from_list_to_matrix(from_letter_to_number(besedilo))
    pretvorba = [zmnozi_matriko(matrika, vektor) for vektor in besedilo_po_delih]
    return from_number_to_letter(from_matrix_to_list(pretvorba))

def vse_obrljive_2x2_matrike(n):
    matrike = []
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if a*d == b*c:
                        pass
                    else:
                        matrike.append([[a,b], [c, d]])
    return matrike

število_obrljivih_2x2_matrik = len(vse_obrljive_2x2_matrike(26))
#print(število_obrljivih_2x2_matrik)

def matrix_to_string(matrix):
    string = ""
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            string += str(matrix[i][j])
    return string

#print(matrix_to_string([[1,2,3], [4,5,6]]))

#def dekodiraj(besedilo):
#    vrednosti_besedil = {}
#    for matrika in vse_obrljive_2x2_matrike(26):
#        dekodirano_besedilo = matrika_na_besedilu(matrika, besedilo)
#        for beseda in seznam_angleskih_besed:
#            vrednosti_besedil[matrix_to_string(matrika)] = 0
#            if beseda in dekodirano_besedilo:
#                vrednosti_besedil[matrix_to_string(matrika)] += 1
#            else:
#                pass 
#    return vrednosti_besedil

with open("dekodirana_besedial.txt", "w") as file:
    start_time = time.time()

    def dekodiraj(besedilo):
        vsa_mozna_dekodiranja = []
        for matrika in vse_obrljive_2x2_matrike(26):
            dekodirano_besedilo = matrika_na_besedilu(matrika, besedilo)
            vsa_mozna_dekodiranja.append(dekodirano_besedilo)
        return vsa_mozna_dekodiranja

    writer = file.writelines("\n".join(dekodiraj(sifra)))

    dekodiraj(sifra)

    def poisci_pravo_dekodiranje(sifra):
        for besedilo in dekodiraj(sifra):
            if detect(besedilo) == "en":
                print(besedilo)
            else:
                pass

    #poisci_pravo_dekodiranje(sifra)

    #def poisci_pravo_dekodiranje(sez):
    #    vrednosti = []
    #    for besedilo in sez:
    #        stevec = 0
    #        for beseda in seznam_angleskih_besed:
    #            if beseda in besedilo:
    #                stevec += 1
    #            else:
    #                pass
    #        vrednosti.append(stevec)
    #    vrednosti
            
    #print(poisci_pravo_dekodiranje(dekodiraj(sifra_s_stevili)))
    #print(dekodiraj(sifra))
    print(time.time() - start_time, "seconds")