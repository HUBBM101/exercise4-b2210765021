number=int(input("Please enter a number:"))
sum_odd=0
sum_even=0
evens=[]
for i in range(1,number+1):
    if i%2!=0:
        sum_odd+=i
    else:
        sum_even+=i
        evens+=str(i)
print("Sum of off odds:",sum_odd)
print("Average of evens:",sum_even/len(evens))
    
