inputNilai = int(input("Input Nilai : "))

def countGrade(inputNilai):
    status = []
    grade = []
    if inputNilai >= 90 and inputNilai <= 100:
        grade.append("A")
        status.append("Lulus")
    elif inputNilai >= 80 and inputNilai <= 89:
        grade.append("B")
        status.append("Lulus")
    elif inputNilai >= 75 and inputNilai <= 79:
        grade.append("C")
        status.append("Lulus")
    elif inputNilai <= 75:
        grade.append("D")
        status.append("Tidak Lulus")
    #convertGrade = ' '.join(map(str, grade))
    convertGrade = ', '.join(grade)
    convertStatus = ' '.join(map(str, status))
    return f"Status : {convertStatus} \nGrade : {convertGrade}"

hitungNilai = countGrade(inputNilai)
print(hitungNilai)

#READ.ME#
#Goals : 
#Implementation Conditional
#Implementation comparison operator and logic operator
#Convert Type data (List to Str)
#Persiapan Variabel
#-Variabel nilai = untuk menampung nilai 
#-Menggunakan logic and untuk mengcompare nilai berdasarkan rentang nilai yang ada
#status : Lulus or tidak lulus
#Grade : A/B/C/D