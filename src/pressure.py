from integration import *
from airfoil import *

#Function performing the computation of a pressure map around the wing
def compute_pressure_map(f, h_min, h_max, nx=100, ny=100, P_static=101325):
    """
    Compute a pressure map around an airfoil.
    
    Parameters:
    - f: Function representing the airfoil upper surface
    - h_min: Minimal height of the airfoil
    - h_max: Maximal height of the airfoil
    - nx & ny defining grid resolution
    
    Returns:
    - pressure_map: 2D array of pressure values
    """  
       
    pressure_map = np.zeros(nx * ny)
    
    for i in range(nx):
        for j in range(ny):
            
            if is_in_airfoil(i, j, f):
                continue
            
            #chercher lambda
            compute_lambda(i, j, f, h_max)
            
            #calculer la vitesse nécessaire pour dét la pression
            v = compute_v()
            
            pressure_map[j, i] = compute_pressure(P_static, v, rho=1.225)
    
    return pressure_map


def is_in_airfoil(x, y, f):
    """Vérifie si un point est intérieur à l'aile"""
    pass

def compute_lambda(x, y, f, h_max):
    """Find the λ parameter for the streamline passing through (x,y)"""
    return (y - f(x)) / (3*h_max - f(x)) 

def compute_v():
    """Calcule la vitesse nécessaire pour dét la pression"""
    
    pass

def compute_pressure(P_static, V, rho=1.225):
    """Calcule la pression à partir de la vitesse"""
    return P_static + 0.5 * rho * V**2

#fonction de visualisation


