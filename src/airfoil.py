import numpy as np
import matplotlib.pyplot as plt

def cubic_spline(x, y):
    n = len(x) - 1  # Nombre de segments
    h = np.diff(x)  # Pas entre les points
    alpha = np.zeros(n)

    # Calcul de alpha pour l'équation tridiagonale
    for i in range(1, n):
        alpha[i] = (3 / h[i]) * (y[i + 1] - y[i]) - (3 / h[i - 1]) * (y[i] - y[i - 1])

    # Construction du système tridiagonal
    l = np.ones(n + 1)
    mu = np.zeros(n)
    z = np.zeros(n + 1)

    for i in range(1, n):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    # Résolution du système pour c_i
    c = np.zeros(n + 1)
    b = np.zeros(n)
    d = np.zeros(n)

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # Stockage des coefficients
    coefficients = [(y[i], b[i], c[i], d[i]) for i in range(n)]
    return coefficients

# Fonction pour évaluer la spline à un point donné # On va evaluer les ordonnees des points de x_vals
def evaluate_spline(x_vals, x, coefficients):
    n = len(x) - 1
    y_vals = []
    for x_val in x_vals:
        # Trouver le bon intervalle
        for i in range(n):
            if x[i] <= x_val <= x[i + 1]: # la liste x contient les intervalles par selon lesquels la spline est definie
                a, b, c, d = coefficients[i]
                dx = x_val - x[i]
                count += 1
                y_vals.append(a + b * dx + c * dx**2 + d * dx**3)
                break
    return np.array(y_vals)

x = np.array([1, 2, 2.5, 3.5, 5])
y = np.array([2, 3, 5, 4, 6])

# Calcul des coefficients de la spline cubique
coefficients = cubic_spline(x, y)

# Évaluation de la spline sur un domaine plus dense
x_dense = np.linspace(1, 5, 100)
y_dense = evaluate_spline(x_dense, x, coefficients)

# Affichage du résultat
plt.scatter(x, y, color='red', label="Points donnés")
plt.plot(x_dense, y_dense, label="Spline cubique", color='blue')
plt.legend()
plt.show()
