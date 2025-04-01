#%%
x = float(input("Input a number: "))

def function(x):
    if 0 <= x <= 1:
        def error(c,b):
            y = (c**((2*b)+1))/((2*b)+1)
            return y
        
        n = 0
        while error(x,n) > 0.0001:
            n += 1
            
        a = 0
        for i in range(n):
            current = (((-1)**i)*(x**((2*i)+1)))/(3)
            a += current
          
    else: 
        return("Error! Please input a number between 0 and 1.")
    
    return (a,n,error(x,n))
    
print(function(x))
