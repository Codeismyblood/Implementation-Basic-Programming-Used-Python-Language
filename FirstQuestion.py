name = input("Input Name : ")
age = int(input("Input Age (Now) : "))
height = int(input("Input Height (cm) : "))

def calculate_height(name, age, height):
    hitungUmur = age + 5
    hitungTinggi = height / 100
    return f"Name : {name} \nAge Now : {age} \nAge for 5 years : {hitungUmur} \nHeight (Meter) : {hitungTinggi}" 

hitungUsia = calculate_height(name,age,height)
print(hitungUsia)


##README.MD##
#Goals :
#Variabel implementation
#Data Types
#Input
#Function, Parameter, and Return Value
#Implementation Global & Local Scope
#Implementation multipleline

# *Persiapan Variabel 
# - Variabel nama = (menampung nama)
# - Variabel umur = (menampung umur)
# - Variabel tinggi badan = (menampung nilai sebelum perhitungan berlanjut)

# *Perhitungan
# - Menghitung umur 5 tahun yang akan datang
# - menghitung tinggi badan dalam centimeter ke dalam satuan meter

# membuat fungsi dengan parameter : Name,Age,Height 


