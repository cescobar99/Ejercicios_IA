convertion_to_roman = {
	1000: "M",
	900: "CM",
	500: "D",
	400: "CD",
	100: "C",
	90: "XC",
	50: "L",
	40: "XL",
	10: "X",
	9: "IX",
	5: "V",
	4: "IV",
	1: "I"
}
def roman(number):
    roman = []
    for size in sorted(convertion_to_roman,reverse=True):
        c = int(number / size)
        number = number % size
        roman.append(convertion_to_roman[size] * c)
        
    return "".join(roman)
    
