def print_asterisk_pattern(n):
    # Your code here
    for i in range(1,n+1):
#        for j in range(i):
        print("*" *i,end="" )
        print("\n")    

# Example usage:
print_asterisk_pattern(int(input("enter the number")))
