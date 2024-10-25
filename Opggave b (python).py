# Definerer en klasse for studenter med navn og gruppenummer
class Student:
    def __init__(self, navn, gruppenr):
        self.navn = navn
        self.gruppenr = gruppenr

# Oppretter noen studenter med deres gruppenummer
David = Student("David", 1)
Per = Student("Per", 1)
Chris = Student("Chris", 2)
Jonas = Student("Jonas", 2)
Peder = Student("Peder", 3)
Arne = Student("Arne", 3)

# Definerer en klasse for grupper med gruppenavn og gruppenummer
class gruppe:
    def __init__(self, navn, gruppenr):
        self.navn = navn
        self.gruppenr = gruppenr

# Oppretter gruppene med navn og deres gruppenummer
gruppe1 = gruppe("gruppe 1", 1)
gruppe2 = gruppe("gruppe 2", 2)
gruppe3 = gruppe("gruppe 3", 3)

# Funksjon som finner gruppen til en student basert på gruppenummer
def finngruppe(student):
    if student.gruppenr == 1:
        return gruppe1.navn
    elif student.gruppenr == 2:
        return gruppe2.navn
    elif student.gruppenr == 3:
        return gruppe3.navn

# Eksempel på bruk
print(finngruppe(David))  # "Skrive ut gruppe 1"

assert finngruppe(David) == "gruppe 1"
assert finngruppe(Chris) == "gruppe 2"
assert finngruppe(Peder) == "gruppe 3"
print("alle testene er bestått")





