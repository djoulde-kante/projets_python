import numpy as np
import matplotlib.pyplot as plt

def nicholson_bailey_model(generations=30, r=2, a=0.05, beta=1, H0=20, P0=2):
    H = np.zeros(generations)  # Population hôte
    P = np.zeros(generations)  # Population parasitoïde
    t = np.arange(generations)
    
    # Initialisation
    H[0] = H0
    P[0] = P0
    
    # Simulation
    for i in range(generations-1):
        H[i+1] = r * H[i] * np.exp(-a * P[i])
        P[i+1] = beta * H[i] * (1 - np.exp(-a * P[i]))
    
    # Création du graphique
    plt.figure(figsize=(10, 6))
    plt.plot(t, H, 'b-', label='Hôtes')
    plt.plot(t, P, 'r-', label='Parasitoïdes')
    plt.xlabel('Générations')
    plt.ylabel('Taille de la population')
    plt.title('Modèle de Nicholson-Bailey')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return np.column_stack((t, H, P))

def main():
    resultats = nicholson_bailey_model()
    print("Aperçu des résultats (5 premières générations):")
    print("Génération | Hôtes    | Parasitoïdes")
    print("-" * 35)
    for i in range(5):
        print(f"{int(resultats[i,0]):10d} | {resultats[i,1]:8.2f} | {resultats[i,2]:8.2f}")

if __name__ == "__main__":
    main()
