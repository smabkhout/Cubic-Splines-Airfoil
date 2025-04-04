# Question 1
# Intégrale: left and right rectangle,trapezoid

def integration_n_left_rec( f, a, b, N ):
    I=0
    h = (b-a)/N
    for i in range(N):
        I+= f(a + i*h)
    return h * I

def integration_n_right_rec( f, a, b, N ):
    I=0
    h = (b-a)/N
    for i in range(1, N+1):
        I+= f(a + i*h)
    return h * I

def integration_n_trapezoid( f, a, b, N ):
    I=0
    h = (b-a)/N
    for i in range(1, N):
        I+= f(a + i*h)   
    I += (f(a) + f(b))/2 
    return h * I

#Intégrale: middle point, Simpson