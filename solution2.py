# Write a function that prints the natural numbers from 1 to n

def natural_numbers(x,i=1):
    if  i > x:
        return
    else:
        print(i)
        natural_numbers(x, i+1)
        
natural_numbers(3)
