#1 van for 11 people
#1 car for 4 people
#input people
#calculate amount of van and car (เลือกใช้รถตู้ให้เต็มคันก่อนเสมอ)

def validate_number(number):
    if number == 0 :
                return "input amount of people"
    elif type(number) != int :
        if type(number) == str:
            return "input integer"
        elif number < 0 :
            return "input integer"
        else:
            return "input integer"
    else:
        return "input integer"

def amount_of_vehicle(number):
    if number%11 > 0:
        amount_of_van = int(number/11)
        number = number-(11*amount_of_van)
        if number%4 == 0:
            amount_of_car = int(number/4)
        elif number%4 != 0:
            amount_of_car = int(number/4)
            amount_of_car = amount_of_car+1
    elif number%11 == 0:
        amount_of_van = int(number/11)
        amount_of_car = 0
    elif number%11 < 0:
        if number%4 == 0:
            amount_of_car = int(number/4)
            amount_of_van = 0
        elif number%4 != 0:
            amount_of_car = int(number/4)
            amount_of_car = amount_of_car + 1
            amount_of_van = 0
    return (str(amount_of_van)," van",str(amount_of_car)," car")


            
