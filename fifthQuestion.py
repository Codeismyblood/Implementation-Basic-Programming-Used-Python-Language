employee = [
    {"name": "Budi", "sallary":5000000, "status":"fix"},
    {"name": "Andi", "sallary":3000000, "status":"contract"},
    {"name": "Siti", "sallary":7000000, "status":"fix"}
]

def countBonus (employee):

    for index in employee:
        if index["status"] == "fix":
            print(f"Nama : {index["name"]}, Status : {index["status"]}, sallary : {index["sallary"]}")
            rewardBonusFix = index["sallary"] * 20 / 100
            FinalresultBonusandSallaryFix = index["sallary"] + rewardBonusFix
            print(f"Total gaji + bonus : {FinalresultBonusandSallaryFix}")
        if index["status"] == "contract":
            print(f"Nama : {index["name"]}, Status : {index["status"]}, sallary : {index["sallary"]}")
            rewardBonusContract = index["sallary"] * 10/ 100
            FinalresultBonusandSallaryContract = index["sallary"] + rewardBonusContract
            print(f"Total gaji + Bonus : {FinalresultBonusandSallaryContract}")

countBonus(employee)

#README.MD#
#Goals : 
#Looping → untuk iterasi data
#Conditional → untuk cek status
#Operator:
#Aritmatika (+, *, /)
#Perbandingan
#Logika (opsional)
#Function