def my_max(lst):
    if len(lst) == 0:
        return None  # returnerer none hvis listen er tom
    max_value = lst[0]
    for num in lst: # går gjennom hvert element i listen, # og sjekker om hvert element er større enn max_value
        if num > max_value:
            max_value = num
    return max_value # returner tallet som har høyeste verdi

def finn_storste(lst):
    max_value = my_max(lst)
    if max_value is None:
        return "listen er tom."
    else:
        return f"Det største tallet i listen er {max_value}."
resultat = finn_storste([1, 2, 3, 4, 5, 6,])
print(resultat)

# definerer my_str_len funksjonen
def my_str_len(s):
    count = 0 # det holder styr på hvor mange variabler som er telt i strengen
    for char in s:
        count += 1 # for hvert tegn vil øke count med 1
    return count

# Definer en ny funksjon som bruker my_str_len
def finn_streng_lengde(s):
    lengde = my_str_len(s) # Her kaller vi my_str_len(s) for å beregne lengden på strengen s.
    #resultat blir lagret i variabelen lengde.
    return f"Strengen '{s}' har {lengde} tegn."

resultat = finn_streng_lengde("hei verden")
print(resultat)
 
