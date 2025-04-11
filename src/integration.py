import math as math
# Question 1
# Intégrale: left and right rectangle,trapezoid

def integration_n_left_rec( f, a, b, N ):
    """
    Calcule l'intégrale de f sur [a,b] en utilisant la méthode des rectangles à gauche
    Paramètres: 
    - f: fonction à intégrer
    - a: borne inférieure de l'intervalle
    - b: borne supérieure de l'intervalle
    - N: nombre de sous-intervalles
    Retourne:
    - l'intégrale de f sur [a,b]
    """
    #calcul de la largeur des sous intervalles
    I=0
    h = (b-a)/N
    for i in range(N):
        I+= f(a + i*h)
    return h * I

def integration_n_right_rec( f, a, b, N ):
    """
    Calcule l'intégrale de f sur [a,b] en utilisant la méthode des rectangles à gauche
    Paramètres: 
    - f: fonction à intégrer
    - a: borne inférieure de l'intervalle
    - b: borne supérieure de l'intervalle
    - N: nombre de sous-intervalles
    Retourne:
    - l'intégrale de f sur [a,b]
    """
    I=0
    h = (b-a)/N
    for i in range(1, N+1):
        I+= f(a + i*h)
    return h * I

def integration_n_trapezoid( f, a, b, N ):
    """
    Calcule l'intégrale de f sur [a,b] en utilisant la méthode des trapèzes
    Paramètres: 
    - f: fonction à intégrer
    - a: borne inférieure de l'intervalle
    - b: borne supérieure de l'intervalle
    - N: nombre de sous-intervalles
    Retourne:
    - l'intégrale de f sur [a,b]
    """
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

#Question 2:
def integretion_epsilon( f, a, b, eps, meth ):
    """
    Calcule l'intégrale de f sur [a,b] avec une précision eps
    en utilisant la méthode meth.
    Paramètres:
    - f: fonction à intégrer
    - a: borne inférieure de l'intervalle
    - b: borne supérieure de l'intervalle
    - eps: précision souhaitée
    - meth: méthode d'intégration (une fonction)
    Retourne:
    - l'intégrale de f sur [a,b] avec une précision eps
    """

    N = 10000 # nombre d'itérations maximal
    i = 1
    while (i < N):
        In = meth(f, a, b, i)
        In_p1 = meth(f, a, b, i*2)
        if math.abs(In - In_p1) < eps:
            return In_p1
        i *= 2
    return In




























#Question 3
#test_de_meth_sur_un_polynôme_de_degré_n
def test_poly(meth
