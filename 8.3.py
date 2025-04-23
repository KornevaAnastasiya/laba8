students=[{"name":"Ivan","languages":["английский","китайский","испанский"]},
          {"name":"Maria","languages":["японский", "корейский", "тайский"]},
          {"name":"Karina","languages":["польский","китайский"]},
          {"name":"Lada","languages":["китайский","японский","хинди"]}
]
all_languages=set(lang for student in students for lang in student["languages"])
sort_langu=sorted(all_languages)

china_stud=[student["name"]for student in students if "китайский"in student["languages"]]
print("different lang",sort_langu)
print("students who know китайский",china_stud)