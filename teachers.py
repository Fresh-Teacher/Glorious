import json

def generate_email(name):
    return name.split()[0].lower() + name.split()[1].lower() + '@glorious.com'

def generate_teacher_details(teacher_data):
    teachers = []
    for data in teacher_data:
        name_parts = data[0].split()
        teacher = {
            "name": " ".join(name_parts),
            "photo": "",
            "sex": "",
            "nationality": "",
            "maritalStatus": "",
            "religion": "",
            "subjectsTaught": [],
            "classesTaught": [],
            "email": generate_email(data[0]),
            "birthdate": "",
            "contactNumber": data[1].split(' / ') if ' / ' in data[1] else [data[1]]
        }
        teachers.append(teacher)
    return teachers

teacher_data = [
    ("KAMEREMBO GENEROUS KAHOMBATE", "0781422393"),
    ("NAKITTO IMELDAH", "0700696792"),
    ("NAMULINDWA SYLVIA", "0701936463"),
    ("NAMPUNGU ZAHARAH MARIAM", "0755382095"),
    ("NAMWANJE NOELYN", "0701305309"),
    ("NAKANJAKO TEDDY", "0755317325"),
    ("AKUKU NELVIN ANGELLA", "0705026079"),
    ("ACHIENG GRACE", "0776108763"),
    ("NAMULI MARTHA", "0708166226"),
    ("NAJJEMBA ROSEMARY", "0778249398"),
    ("NAMBOGO TEDDY", "0788732716"),
    ("TAREMWA FLAVIA", "0787393767"),
    ("NAMUKASA JUSTINE", "0786585083"),
    ("NAKABONGE SAMALIE", "0741406048"),
    ("NYAMATE AMPEREZA JUDITH", "0759192951"),
    ("KARUNGI OLIVIA", "0787393767"),
    ("ZEMEI MIRIAM", "0704235682"),
    ("NAMUGERWA STELLAH", "0776278101"),
    ("NANSUBUGA GLORIA", "0706482420"),
    ("NAKAWUKA MARIA MARGARET RITAH", "0760773937"),
    ("AKELLO SARAH ENUME", "0784161222"),
    ("NAMUJJUMBI PROSSY", "0703544871"),
    ("NITUMWIKIRIZA EDINAH", "0783586824"),
    ("KUSAASIRA BARBRA", "0705547386"),
    ("NAZZIWA SHARON", "0759230048"),
    ("NAMUSAAZI BENITAH", "0759523884"),
    ("KYOZIRA MARGRET", "0784834170"),
    ("NAKAGGWA RUTH", "0771470205"),
    ("NAMUGENYI LEIRAH A.", "0702988381"),
    ("AJUNA MATHIAS", "0757266687"),
    ("MIRIMU MANSUR", "0740737275"),
    ("NKWASIBWE LABON", "0753618333"),
    ("NSIIMIRE DENIS", "0743722149"),
    ("ODAGA ALEX", "0755190443"),
    ("KALIISA JOSEPH KATO", "0773546465"),
    ("TURYOMURUGYENDO MOSES", "0700718840"),
    ("NDAWULA SAM", "0704341303 / 0762648863"),
    ("WAISWA ISSA", "0759494094"),
    ("MUKASA WALTER OJIAMBO", "0763104834"),
    ("OKURUT CHARLES", "0778740333"),
    ("SABAIDU ROBERT SMITH", "0754513111"),
    ("TURINAWE JUSTUS", "0775562642"),
    ("WATHUM HABERT", "0703697049"),
    ("NIYOKINDI BENOIT", "0761065888"),
    ("EPODOI GERALD BENJAMIN", "0393242808"),
    ("TUHAIRWE JOSEPH", "0756052623"),
    ("MUTUMBA JESSE PAUL", "0750687790 / 0786812837"),
    ("KIWANUKA EDWARD", "0752546211"),
    ("BONGOMIN GABRIEL", "0705715959"),
    ("ATWIINE EDMOND", "0782284273"),
    ("KAYONGO SANTOS JOSEPH", "0759805467")
]

teacher_details = generate_teacher_details(teacher_data)

with open('teacher_details.json', 'w') as f:
    json.dump(teacher_details, f, indent=4)

print("JSON file 'teacher_details.json' has been created with teacher details.")