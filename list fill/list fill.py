import random
import time
import matplotlib.pyplot as plt

#Define constants for max length, max runs, and amount to increment the list length
MAX_LENGTH = 5000
MAX_RUNS = 5
INCREMENT = 100

#Define starting length and initialize counter
target_length = 100
counter = 0

#Create empty lists for finished size and time data
size_data = []
time_data = []

#Seed RNG
random.seed()

#Main loop. Will run until target_length > MAX_LENGTH. Target length increments by INCREMENT value for each loop
while target_length <= MAX_LENGTH:

    #Defines and resets average time variable between sets
    time_average = 0

    #Perform each filling of the list MAX_RUNS times and times each run, which will be averaged and added to final time list
    for i in range(0, MAX_RUNS):
        numbers = []
        start = time.time()

        #Runs while numbers list is shorter in length than the target length. Will stop running when every number from 1 to target length is in list
        while len(numbers) < target_length:

            #Gen a number
            potential_new_entry = random.randint(1, target_length)
            
            #If that number is in the list skip it
            if potential_new_entry in numbers:
                continue
            
            #Otherwise add it to the list
            else:
                numbers.append(potential_new_entry)

        end = time.time()

        #Calculate time it took to perform the run
        time_result = end - start

        #Add that time to the average variable
        time_average = time_average + time_result

        #Tallies how far in the process we are. 
        print("Completed run " + str(i + 1) + " of " + str(MAX_RUNS) +  " in set " + str(counter + 1) + " of " + str(int(MAX_LENGTH / INCREMENT)) +
            ", which is filling a list with " + str(target_length) + " integers.")

    #Counter tracks list size
    counter = counter + 1

    #Appends averaged time to the final time data list
    time_data.append(time_average / MAX_RUNS)

    #Appends length to final size data list. Each run will have its data stored in the same index position of each list
    size_data.append(target_length)

    #Increments target length by 100. Final size is defined in MAX_LENGTH constant
    target_length = target_length + INCREMENT

#Everything below plots the data
x = size_data
y = time_data

plt.plot(x, y)
plt.xlabel('Size of list')
plt.ylabel('Time (Seconds)')
plt.title('Time to fill a list with every integer from 1 to X without duplicates')
plt.show()