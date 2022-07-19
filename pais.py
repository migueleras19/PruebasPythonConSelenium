from countryinfo import CountryInfo

count = input("Ingrese el País: ")

country = CountryInfo(count)


print("Capital de: ", country.capital(), country.provinces())
print("Idioma de: ", country.languages())
print("Regionm que pertenece el País: ", country.region())
print("Especificaciones del País: ", country.alt_spellings())
print("AreaS de: ", country.area())
print("Nombre nativo de: ", country.population())








