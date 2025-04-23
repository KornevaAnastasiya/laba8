countries={"South Korea":"Seoul",
         "Russia":"Moscow",
         "USA":"Waschington D.C",
         "France":"Paris",
         "China":"Peking"
}
print('\nCountry and capital')
for country, capital in countries.items():
    print(f"{country}: {capital}")

country_name = input("\nEnter the name of a country: ").strip().title()#стрип удаляет лишние пробелы,сопостовление с ключами словаря
if country_name in countries:
    print(f"\nThe capital of {country_name} is: {countries[country_name]}")
else:
    print("\nThis country is not on the list.")
sorted_countries = sorted(countries.keys())

print("\nSorted List of Countries and Capitals:")
for nation in sorted_countries:
    print(f"{nation}: {countries[nation]}")