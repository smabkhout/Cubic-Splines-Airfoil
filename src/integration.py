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
def integration_n_middle_point(f,a,b,n):
    #calcul de largeur des sous intervalles
    h=(b-a)/n
    #construction d'une liste des images  des noeuds de quadrature
    l=[f(a+(2*k+1)*h/2) for k in range(n)]
    s=0
    for i in range(n):
       s+=l[i]
    return s*h   

def integration_n_simpson(f,a,b,n):
     #calcul de largeur des sous intervalles
    h=(b-a)/(n+1)
    #construction d'une liste  des noeuds de quadrature
    l=[a+k*h for k in range(1,n+1)]
    s=0
    d=0
    for i in range(n+1):
       s+=f(l[i]+h/2)
    for i in range(1,n+1):
       d+=f(l[i])
    return (h/6)*(f(a)+f(b))+(2*h/3)*s+(h/3)*d































#Question 3
#test_de_meth_sur_un_polynôme_de_degré_n
def test_poly(meth
