# The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. 
# You have to write a program to find out the population at the end of each of the last 10 years. 
# For eg current population is 10000 so the output should be like this:
# 10th year - 10000
# 9th year - 9000
# 8th year - 8100 and so on

current_population=int(input("enter population:"))
count=0
print(current_population)


while True:
    population_increase=current_population-((current_population*10)/100)
    current_population=population_increase
    print(int(population_increase))
    count+=1
    if count==9:
        break






