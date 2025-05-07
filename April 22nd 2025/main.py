'''
Name: Ritesh Sivanathan
Date: April 25 2025
Description: Read and Write to files
'''

total_sum = 0

with open("num.txt", "w") as num_txt:
    for i in range (1, 11):
        num_txt.write(str(i)+("" if i==10 else "\n"))

with open("num.txt", "r") as num_txt:
    for line in num_txt:
        number = int(line.strip())
        total_sum += number

print(total_sum)