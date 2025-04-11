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

# Fonction pour évaluer la spline à un point donné
def evaluate_spline(x_vals, x, coefficients):
    n = len(x) - 1
    y_vals = []

    for x_val in x_vals:
        # Trouver le bon intervalle
        for i in range(n):
            if x[i] <= x_val <= x[i + 1]:
                a, b, c, d = coefficients[i]
                dx = x_val - x[i]
                y_vals.append(a + b * dx + c * dx**2 + d * dx**3)
                break

    return np.array(y_vals)

# Exemple d'utilisation
x = np.array([7.70000e-05,4.71000e-04,1.52700e-03,2.84400e-03,4.34000e-03,6.02500e-03
,7.92300e-03,1.00400e-02,1.23870e-02,1.49810e-02,1.78250e-02,2.09310e-02
,2.43130e-02,2.79870e-02,3.19660e-02,3.62650e-02,4.09020e-02,4.58960e-02
,5.12600e-02,5.70090e-02,6.31590e-02,6.97260e-02,7.67270e-02,8.41770e-02
,9.20920e-02,1.00487e-01,1.09377e-01,1.18778e-01,1.28704e-01,1.39169e-01
,1.50184e-01,1.61763e-01,1.73919e-01,1.86664e-01,2.00007e-01,2.13958e-01
,2.28525e-01,2.43715e-01,2.59532e-01,2.75981e-01,2.93062e-01,3.10776e-01
,3.29120e-01,3.48087e-01,3.67669e-01,3.87856e-01,4.08632e-01,4.29979e-01
,4.51876e-01,4.74296e-01,4.97207e-01,5.20573e-01,5.44351e-01,5.68493e-01
,5.92942e-01,6.17641e-01,6.42522e-01,6.67505e-01,6.92501e-01,7.42170e-01
,7.90661e-01,8.58986e-01,8.99952e-01,9.35728e-01,9.64902e-01,9.85886e-01
,1.00000e+00])
print(x.shape[0])
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
