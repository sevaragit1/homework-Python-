#Temperature

#1
#def convert_cel_to_far(C):
    #return C*9/5+32
#C = float(input("Please enter the temperature in Celsius: "))
#F = convert_cel_to_far(C)
#print(f"The temperature in Fahrenheit is: {F}")

#2
#def convert_far_to_cel(F):
    #return (F-32)*5/9
#F = float(input("Please enter the temperature in Farenheit: "))
#C = convert_far_to_cel(F)
#print(f"The temperature in Celsius is: {C}")

#Invest

#1
#def invest(amount, rate, years):
    #for year in range(1, years + 1):
        #amount += amount * rate
        #print(f"year {year}: ${amount:.2f}")

#try:
    #principal = float(input("Please enter the initial amount: "))
    #annual_rate = float(input("Please enter the annual rate of return (e.g., 0.05 for 5%): "))
    #years = int(input("Please enter the number of years: "))

    #invest(principal, annual_rate, years)
#except ValueError:
    #print("Please enter only numeric values for the amount, rate, and years.")


#Factors


#number = int(input("Please enter a positive integer: "))
#for a in range(1, number + 1):
    #if number % a == 0: 
        #print(f"{a} is a factor of {number}")


