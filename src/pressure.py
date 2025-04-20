from integration import integration_n_trapezoid
from airfoil import evaluate_spline, cubic_spline, extrados_x, extrados_y, intrados_x, intrados_y
import numpy as np
import matplotlib.pyplot as plt

# Calculer les coefficients de la spline cubique pour les surfaces supérieure et inférieure
coeff_intra = cubic_spline(intrados_x, intrados_y)
coeff_extra = cubic_spline(extrados_x, extrados_y)

def compute_pressure_map(h_max, h_min, nx=200, ny=200, P=101325):
    """
   Calcule une carte de pression autour de l'aile.
   
   Paramètres:
   - h_min: Hauteur minimale du profil d'aile
   - h_max: Hauteur maximale du profil d'aile
   - nx & ny définissant la résolution de la grille
    - P: Pression statique (en Pa)
   
   Retourne:
   - pressure_map: Tableau 2D des valeurs de pression
   """ 
    pressure_map = np.full((ny, nx), np.nan)

    for i in range(nx):
        for j in range(ny):
            # Calculer les coordonnées x et y
            x = i * (max(extrados_x) - min(extrados_x)) / (nx - 1) + min(extrados_x)
            y = (j - ny//2) * (3*h_max + abs(3*h_min)) / (ny - 1)
            
            if is_in_airfoil(x, y, extrados_x, intrados_x, coeff_extra, coeff_intra):
                pressure_map[j, i] = np.nan
                continue
            
            # Déterminer si on est au-dessus ou en-dessous de l'aile
            if y >= 0: 
                lambda_val = compute_lambda_upper(x, y, extrados_x, coeff_extra, h_max)
                if lambda_val is None or not (0 <= lambda_val <= 1):
                    continue
                
                streamline_length = compute_streamline_length(lambda_val, extrados_x, coeff_extra, 
                                                              h_max, is_upper=True)
            else: 
                lambda_val = compute_lambda_lower(x, y, intrados_x, coeff_intra, h_min)
                if lambda_val is None or not (0 <= lambda_val <= 1):
                    continue
                
                streamline_length = compute_streamline_length(lambda_val, intrados_x, coeff_intra, 
                                                              h_min, is_upper=False)
            
            v = compute_v(streamline_length)
            pressure_map[j, i] = compute_pressure(P, v, rho=1.204)
    
    return pressure_map

def is_in_airfoil(x, y, extrados_x, intrados_x, coeff_extra, coeff_intra):
    """
    Détermine si un point (x,y) est à l'intérieur du profil d'aile
    en utilisant la fonction evaluate_spline.
    
    Paramètres:
    - x, y: Coordonnées du point
    - extrados_x, extrados_y: Points définissant la surface supérieure
    - intrados_x, intrados_y: Points définissant la surface inférieure
    
    Retourne:
    - True si le point est à l'intérieur du profil, False sinon
    """
    # Vérifier si x est dans le domaine du profil de l'aile
    if x < min(extrados_x) or x > max(extrados_x) or x < min(intrados_x) or x > max(intrados_x):
        return False
    
    y_upper = evaluate_spline([x], extrados_x, coeff_extra)[0]
    y_lower = evaluate_spline([x], intrados_x, coeff_intra)[0]
    return y_lower <= y <= y_upper



def compute_lambda_upper(x, y, extrados_x, coeff_extra, h_max):
    """Lambda pour les points au-dessus de l'aile"""
    if x < min(extrados_x) or x > max(extrados_x):
            return None
    fx = evaluate_spline([x], extrados_x, coeff_extra)[0]
    denom = 3*h_max - fx
    if abs(denom) < 1e-10:
        return None
    
    return (y - fx) / denom

def compute_lambda_lower(x, y, intrados_x, coeff_intra, h_min):
    """Lambda pour les points sous l'aile"""
    if x < min(intrados_x) or x > max(intrados_x):
            return None
    fx = evaluate_spline([x], intrados_x, coeff_intra)[0]
    denom = 3*h_min - fx
    if abs(denom) < 1e-10:
        return None
    
    return (y - fx) / denom

def compute_streamline_length(lambda_val, x_points, coefficients, h_limit, 
                              is_upper=True, integration_method=integration_n_trapezoid, 
                              N=100):
    """
    Calcule la longueur d'une ligne de courant avec paramètre lambda.
    
    Paramètres:
    - lambda_val: Paramètre lambda définissant la ligne de courant
    - x_points: Points définissant la surface (extrados ou intrados)
    - coefficients: Coefficients de la spline pour la surface (extrados ou intrados)
    - h_limit: Hauteur limite (h_max pour au-dessus, h_min pour en-dessous)
    - is_upper: True si au-dessus de l'aile, False si en-dessous
    - integration_method: Méthode d'intégration numérique à utiliser
    - N: Nombre de points pour l'intégration numérique
    
    Retourne:
    - Longueur de la ligne de courant
    """
    # Bornes d'intégration
    a = min(x_points)
    b = max(x_points)
    
    # Définir la fonction qui calcule l'élément différentiel de longueur
    def length_element(x):
        h = 1e-6  

        if x < min(x_points) or x > max(x_points) - h:
            return 0.0
            
        # Évaluer la spline à ce point
        y_surface = evaluate_spline([x], x_points, coefficients)[0]
        
        if is_upper:
            y_streamline = (1 - lambda_val) * y_surface + lambda_val * 3 * h_limit
        else:
            y_streamline = (1 - lambda_val) * y_surface + lambda_val * 3 * h_limit
        
        # Calculer la dérivée numérique en ce point
        y_surface_next = evaluate_spline([x + h], x_points, coefficients)[0]
        
        if is_upper:
            y_streamline_next = (1 - lambda_val) * y_surface_next + lambda_val * 3 * h_limit
        else:
            y_streamline_next = (1 - lambda_val) * y_surface_next + lambda_val * 3 * h_limit
        
        # Calculer la pente
        dy_dx = (y_streamline_next - y_streamline) / h
        
        return np.sqrt(1 + dy_dx**2)
    
    # Utiliser la méthode d'intégration fournie pour calculer la longueur
    return integration_method(length_element, a, b, N)

def compute_v(streamline_length):
    """Calcule la vitesse de l'air en fonction de la longueur de la ligne de courant."""

    return 1/streamline_length
    

def compute_pressure(P, V, rho=1.204):
    """Calcule la pression à partir de la vitesse"""
    return P + 0.5 * rho * V**2

#fonction de visualisation

def plot_pressure_map(pressure_map, extrados_x, extrados_y, intrados_x, intrados_y, h_max, h_min):
    plt.figure(figsize=(10, 8))
    
    extent = [0, 1, -3*abs(h_min), 3*h_max]
    plt.imshow(pressure_map, cmap='jet', interpolation='nearest', 
               extent=extent)
    
    plt.colorbar(label='Pression (Pa)')
    
    # Normaliser les x pour le contour
    x_norm_extra = [(x - min(extrados_x)) / (max(extrados_x) - min(extrados_x)) for x in extrados_x]
    x_norm_intra = [(x - min(intrados_x)) / (max(intrados_x) - min(intrados_x)) for x in intrados_x]
    
    # Tracer le contour de l'aile
    plt.plot(x_norm_extra, extrados_y, 'k-', linewidth=2)
    plt.plot(x_norm_intra, intrados_y, 'k-', linewidth=2)
    
    plt.title('Carte de Pression')
    plt.xlabel('Position x normalisée')
    plt.ylabel('Position y (m)')
    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    h_max = 0.1  # Hauteur maximale du profil
    h_min = -0.1  # Hauteur minimale du profil
    nx = 200  # Nombre de points en x
    ny = 200  # Nombre de points en y
    P_static = 101325  # Pression statique (Pa)
    
    pressure_map = compute_pressure_map(h_max,h_min, nx, ny, P_static)
    
    # Plot results
    plot_pressure_map(pressure_map, extrados_x, extrados_y, intrados_x, intrados_y, h_max, h_min)
    

