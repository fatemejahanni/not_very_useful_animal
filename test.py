from not_very_useful_animal import Animal, AnimalType, Gender, Lion

a = Lion("a", Gender.FEMALE, 3, "blue", AnimalType.DOMESTIC)
b = Lion("a", Gender.MALE, 3, "red", AnimalType.WILD)
c = a+b
c.eating(4)
c.moving(4)
