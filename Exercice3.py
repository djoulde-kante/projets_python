import numpy as np
from scipy import stats

def test_correlation(X, Y, rho0):
    # Étape 1: Calcul du coefficient de corrélation
    r = np.corrcoef(X, Y)[0,1]
    
    # Étape 2: Transformation Z de Fisher
    n = len(X)
    z = 0.5 * np.log((1 + r)/(1 - r))
    z0 = 0.5 * np.log((1 + rho0)/(1 - rho0))
    
    # Étape 3: Calcul de la statistique de test
    z_stat = (z - z0) * np.sqrt(n - 3)
    
    # Étape 4: Calcul de la p-value
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    
    return r, p_value

def main():
    np.random.seed(42)  # Pour la reproductibilité
    X = np.random.normal(0, 1, 100)
    Y = 0.7 * X + np.random.normal(0, 0.5, 100)  # Corrélation positive

    # Test avec rho0 = 0
    r, p_value = test_correlation(X, Y, 0)
    print(f"Test avec rho0 = 0:")
    print(f"Coefficient de corrélation: {r:.4f}")
    print(f"P-value: {p_value:.4f}")

    # Test avec rho0 = 0.6
    r, p_value = test_correlation(X, Y, 0.6)
    print(f"\nTest avec rho0 = 0.6:")
    print(f"Coefficient de corrélation: {r:.4f}")
    print(f"P-value: {p_value:.4f}")

if __name__ == "__main__":
    main()
