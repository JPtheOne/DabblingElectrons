import itertools #Library for the combination method
def calculate_combinations(electrons): #Function that calculates the different combinations based on the electrons

    possible_combinations = []#List to store the possible combinations that were calculated

    d_orbital = ["2⁺","2⁻", "1⁺","1⁻","0⁺","0⁻","-1⁺","-1⁻","-2⁺","-2⁻"] #String with the d_orbital. It could be modified later...|

    comb_tuples = itertools.combinations(d_orbital,electrons) #Itertools method to calculate combinations based on the orbital and the electron

    #Loop to print all the tuples obtained by the methods and add them to a list 
    for element in comb_tuples:
        comb_list = list(element)
        possible_combinations.append(comb_list)
    return possible_combinations #Returning the combinations stored on a list

def combination_sums (comb,count):
    values_sum = 0 #variable to store the sum of the numbers 
    half_sum = 0   #Variable to store the half values

    output = ",".join(comb)
    print("Combination #", count,":(",output,")") #Formatting the print of the combination
  
    for i in comb: #Switching the half values
        if i[-1] == "⁺":
            half_sum += 0.5
        else:
            half_sum += -0.5
             
        only_num = int(i[:-1:]) 
        values_sum += only_num

    print("Half sum: ",half_sum)
    print("Sum of numbers: ", values_sum)

#------------------------------------------MAIN--------------------------------------------
electrons = int(input("Precise the number of electrons to be accomodated in orbital d: "))
possible_combinations = calculate_combinations(electrons)

count = 1
for comb in possible_combinations:
    combination_sums(comb, count)
    count += 1
print(" \nSums completed for a total of", count-1, "combinations for d-orbital \n")




 
    
