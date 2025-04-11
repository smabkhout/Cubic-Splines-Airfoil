import math as math
import numpy as np
import matplotlib.pyplot as plt

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
    for i in range(n):
       s+=f(l[i]+h/2)
    for i in range(1,n):
       d+=f(l[i])
    return (h/6)*(f(a)+f(b))+(2*h/3)*s+(h/3)*d

#Question 2:
def integration_epsilon( f, a, b, eps, meth ):
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
        if abs(In - In_p1) < eps:
            return In_p1
        i *= 2
    return In



#Question 3
#tests_sur_un_polynôme_de_degré_4
def poly_4(x):
    return x**4+3*x**2+9*x-3
def test_poly(a,b,eps):
    print("tests sur le polynôme x⁴+3x²+9x-3 entre",a,"et",b)
    print("la valeur donnée par la méthode de left triangle est",integration_epsilon(poly_4,a,b,eps,integration_n_left_rec))
    print("la valeur donnée par la méthode de right triangle est",integration_epsilon(poly_4,a,b,eps,integration_n_right_rec))
    print("la valeur donnée par la méthode de trapèzes est",integration_epsilon(poly_4,a,b,eps,integration_n_trapezoid))
    print("la valeur donnée par la méthode de middle point",integration_epsilon(poly_4,a,b,eps,integration_n_middle_point))
    print("la valeur donnée par la méthode de Simpson",integration_epsilon(poly_4,a,b,eps,integration_n_simpson))

#tests_sur_la_fonction_cos
def cos(x):
    return np.cos(x)
def test_cos(a,b,eps):
    print("tests sur la fonction cos entre",a,"et",b)
    print("la valeur donnée par la méthode de left triangle est",integration_epsilon(cos,a,b,eps,integration_n_left_rec))
    print("la valeur donnée par la méthode de right triangle est",integration_epsilon(cos,a,b,eps,integration_n_right_rec))
    print("la valeur donnée par la méthode de trapèzes est",integration_epsilon(cos,a,b,eps,integration_n_trapezoid))
    print("la valeur donnée par la méthode de middle point",integration_epsilon(cos,a,b,eps,integration_n_middle_point))
    print("la valeur donnée par la méthode de Simpson",integration_epsilon(cos,a,b,eps,integration_n_simpson))

    #tests_sur_la_fonction_sin
def sin(x):
    return np.sin(x)
def test_sin(a,b,eps):
    print("tests sur la fonction sin entre",a,"et",b)
    print("la valeur donnée par la méthode de left triangle est",integration_epsilon(sin,a,b,eps,integration_n_left_rec))
    print("la valeur donnée par la méthode de right triangle est",integration_epsilon(sin,a,b,eps,integration_n_right_rec))
    print("la valeur donnée par la méthode de trapèzes est",integration_epsilon(sin,a,b,eps,integration_n_trapezoid))
    print("la valeur donnée par la méthode de middle point",integration_epsilon(sin,a,b,eps,integration_n_middle_point))
    print("la valeur donnée par la méthode de Simpson",integration_epsilon(sin,a,b,eps,integration_n_simpson))

    #tests_sur_la_fonction_tan
def tan(x):
    return np.tan(x)
def test_tan(a,b,eps):
    print("tests sur la fonction tan entre",a,"et",b)
    print("la valeur donnée par la méthode de left triangle est",integration_epsilon(tan,a,b,eps,integration_n_left_rec))
    print("la valeur donnée par la méthode de right triangle est",integration_epsilon(tan,a,b,eps,integration_n_right_rec))
    print("la valeur donnée par la méthode de trapèzes est",integration_epsilon(tan,a,b,eps,integration_n_trapezoid))
    print("la valeur donnée par la méthode de middle point",integration_epsilon(tan,a,b,eps,integration_n_middle_point))
    print("la valeur donnée par la méthode de Simpson",integration_epsilon(tan,a,b,eps,integration_n_simpson))



a=3
b=19
eps=10**(-3)
test_poly(3,19,10**(-3))
test_cos(3,19,10**(-3))
test_sin(3,19,10**(-3))
test_tan(3,19,10**(-3))

#Question4
#retirer les valeurs des méthodes à chaque fois
def integration_epsilon_valeurs( f, a, b, eps, meth ):
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
    l=[]
    while (i < N):
        In = meth(f, a, b, i)
        In_p1 = meth(f, a, b, i*2)
        if abs(In - In_p1) < eps:
            l+=[In_p1]
            return l
        i *= 2
        l+=[In]
    return l
#Cas left rectangle
# Calculer les valeurs d'intégration pour chaque fonction
valeurs_f1 = integration_epsilon_valeurs(cos, a, b, eps, integration_n_left_rec)
valeurs_f2 = integration_epsilon_valeurs(tan, a, b, eps, integration_n_left_rec)
valeurs_f3 = integration_epsilon_valeurs(poly_4, a, b, eps, integration_n_left_rec)

# Tracer les résultats
plt.figure(figsize=(10, 6))

plt.plot(valeurs_f1, label=r"$\cos(x)$", color='blue', marker='o')
plt.plot(valeurs_f2, label=r"$\tan(x)$", color='red', marker='x')
plt.plot(valeurs_f3, label=r"$poly_4(x)$", color='green', marker='s')

plt.xlabel("Nombre d'itérations")
plt.ylabel("Valeur de l'intégrale")
plt.title("Convergence des intégrales pour différentes fonctions")
plt.legend()
plt.grid(True)

plt.show()

#Cas right rectangle
# Calculer les valeurs d'intégration pour chaque fonction
valeurs_f1 = integration_epsilon_valeurs(cos, a, b, eps, integration_n_right_rec)
valeurs_f2 = integration_epsilon_valeurs(tan, a, b, eps, integration_n_right_rec)
valeurs_f3 = integration_epsilon_valeurs(poly_4, a, b, eps, integration_n_right_rec)

# Tracer les résultats
plt.figure(figsize=(10, 6))

plt.plot(valeurs_f1, label=r"$\cos(x)$", color='blue', marker='o')
plt.plot(valeurs_f2, label=r"$\tan(x)$", color='red', marker='x')
plt.plot(valeurs_f3, label=r"$poly_4(x)$", color='green', marker='s')

plt.xlabel("Nombre d'itérations")
plt.ylabel("Valeur de l'intégrale")
plt.title("Convergence des intégrales pour différentes fonctions")
plt.legend()
plt.grid(True)

plt.show()

#Cas trapezoid
# Calculer les valeurs d'intégration pour chaque fonction
valeurs_f1 = integration_epsilon_valeurs(cos, a, b, eps, integration_n_trapezoid)
valeurs_f2 = integration_epsilon_valeurs(tan, a, b, eps, integration_n_trapezoid)
valeurs_f3 = integration_epsilon_valeurs(poly_4, a, b, eps, integration_n_trapezoid)

# Tracer les résultats
plt.figure(figsize=(10, 6))

plt.plot(valeurs_f1, label=r"$\cos(x)$", color='blue', marker='o')
plt.plot(valeurs_f2, label=r"$\tan(x)$", color='red', marker='x')
plt.plot(valeurs_f3, label=r"$poly_4(x)$", color='green', marker='s')

plt.xlabel("Nombre d'itérations")
plt.ylabel("Valeur de l'intégrale")
plt.title("Convergence des intégrales pour différentes fonctions")
plt.legend()
plt.grid(True)

#plt.show()

#Cas middle point
# Calculer les valeurs d'intégration pour chaque fonction
valeurs_f1 = integration_epsilon_valeurs(cos, a, b, eps, integration_n_middle_point)
valeurs_f2 = integration_epsilon_valeurs(tan, a, b, eps, integration_n_middle_point)
valeurs_f3 = integration_epsilon_valeurs(poly_4, a, b, eps, integration_n_middle_point)

# Tracer les résultats
plt.figure(figsize=(10, 6))

plt.plot(valeurs_f1, label=r"$\cos(x)$", color='blue', marker='o')
plt.plot(valeurs_f2, label=r"$\tan(x)$", color='red', marker='x')
plt.plot(valeurs_f3, label=r"$poly_4(x)$", color='green', marker='s')

plt.xlabel("Nombre d'itérations")
plt.ylabel("Valeur de l'intégrale")
plt.title("Convergence des intégrales pour différentes fonctions")
plt.legend()
plt.grid(True)

#plt.show()

#Cas simpson
# Calculer les valeurs d'intégration pour chaque fonction
valeurs_f1 = integration_epsilon_valeurs(cos, a, b, eps, integration_n_simpson)
valeurs_f2 = integration_epsilon_valeurs(tan, a, b, eps, integration_n_simpson)
valeurs_f3 = integration_epsilon_valeurs(poly_4, a, b, eps, integration_n_simpson)

# Tracer les résultats
plt.figure(figsize=(10, 6))

plt.plot(valeurs_f1, label=r"$\cos(x)$", color='blue', marker='o')
plt.plot(valeurs_f2, label=r"$\tan(x)$", color='red', marker='x')
plt.plot(valeurs_f3, label=r"$poly_4(x)$", color='green', marker='s')

plt.xlabel("Nombre d'itérations")
plt.ylabel("Valeur de l'intégrale")
plt.title("Convergence des intégrales pour différentes fonctions")
plt.legend()
plt.grid(True)

#plt.show()
