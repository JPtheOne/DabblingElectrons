import itertools

def calculate_combinations(orbital, electrons):
    possible_combinations = []
    comb_tuples = itertools.combinations(orbital, electrons)
    
    for element in comb_tuples:
        comb_list = list(element)
        possible_combinations.append(comb_list)      
    return possible_combinations

def combination_sums(combinations_list):
    counter = 1
    half_sum_set = set()  # set to store the half sums for each combination
    value_sum_set = set()  # set to store the value sums for each combination
    sums_dict = {}  # dictionary to store the sums for each combination
    
    #Repeat the loop for EVERY combination given by the combination list
    for comb in combinations_list:
        values_sum = 0
        half_sum = 0
        
        #Check every character of the combination
        for i in comb:
            #Half Sum calculation
            if i[-1] == "⁺":
                half_sum += 0.5
            elif i[-1] == "⁻":
                half_sum += -0.5
            #Value sum Calculation    
            only_num = int(i[:-1:]) 
            values_sum += only_num
            
        #Store the sums for this combination in the dictionary
        str_comb = ",".join(comb)
        str_output = ("C:" + str(counter) + ": " + str_comb)
        sums_dict[str_output] = (half_sum, values_sum)
        
        # add the sums to the respective sets
        half_sum_set.add(half_sum)
        value_sum_set.add(values_sum)
        counter+=1  

    # return the dictionary and the tuple with the highest and lowest sums for each set
    vs_boundary = (min(value_sum_set), max(value_sum_set))
    hs_boundary = (min(half_sum_set), max(half_sum_set))
       
    #print("\nCalculating sums for " + str(counter-1) + " calculations")
    return sums_dict, vs_boundary, hs_boundary, counter


#--------------------------MAIN-------------------------------
d_orbital = ["2⁺","2⁻", "1⁺","1⁻","0⁺","0⁻","-1⁺","-1⁻","-2⁺","-2⁻"]
electrons = int(input("Precise the number of electrons to be accomodated in orbital d: "))

possible_combinations = calculate_combinations(d_orbital, electrons)

sums_dict, vs_boundary, hs_boundary, counter = combination_sums(possible_combinations)

print("Dictionary of Sums for each combination:")
for combination, sums in sums_dict.items():
    print(combination, ":", "Half-sum =", sums[0], ", Value-sum =", sums[1])

print("\nBoundary Values:")
print("Value-sum: ", vs_boundary)
print("Half-sum: ", (hs_boundary))

print("\nSums stored in dictionary for ",len(sums_dict)," total combinations")

print("The dictionary to tabulate is: ",sums_dict)