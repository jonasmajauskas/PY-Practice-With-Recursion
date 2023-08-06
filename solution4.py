# Write a function that calculates the value of 'a' to the power of 'b'.
# This power function calculates a to the power of b, based on the integer values it is fed.
def power(a,b):
    if b < 1:
        print("invalid input")
    # If something is x^0, it will result in zero, so it's an invalid input.
    elif b == 1:
        return a
    # If something is x^1, it will return the values that is being powered.
    else:
        return a * power(a,b-1)
    # This is the formula that must be followed where power(a,b) = a * power(a,b-1)
        return 2 * power (2,3)
        return 2 * (2 * power (2,2))
        return 2 * 2 * (2 * power (2,1))
        return 2 * 2 * 2 * 2

print("2^4:", power(2,4))

power(2,4) = 2 * power(2,3)
power(2,3) = 2 * power(2,2)
power(2,2) = 2 * power(2,1)
power(2,1) = 2

power(2,2) = 2 * 2
power(2,3) = 2 * 2 * 2
power(2,4) = 2 * 2 * 2 * 2