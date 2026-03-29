data_nilai = {
    "nama": "Andi",
    "nilai": [10,20,30]
}

def hitung_nilai_rata_rata(data_nilai):
    value = []
    counter = 0
    jumlah_element = 0
    name = data_nilai["nama"]
    value = data_nilai["nilai"]
    status = ''
    # result = len(value)
    for i in value:
        counter = counter + i

    for x in value:
        jumlah_element = jumlah_element + 1

    averageValue = counter / jumlah_element

    for j in value:
        if j >= 75:
            status = 'Lulus'
        else:
            status = 'Tidak Lulus'

    # print(result)
    # print(jumlah_element)
    # print(counter)
    print(f"name : {name}")
    print(f"Nilai rata - rata : {averageValue}")
    print(f"Status : {status}")
    # print(f"value : {value}")
    return f"name : {name}\nRata - rata nilai : {averageValue}"

hitung_nilai_rata_rata(data_nilai)

#README.MD#
#Goals : 
#Function
#Parameter
#Return value
#Dictionary
