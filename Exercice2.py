def analyse_precipitations():
    BOS = [2.67, 1.00, 1.21, 3.09, 3.43, 4.71, 3.88, 3.08, 4.10, 2.62, 1.01, 5.93]
    MER = [6.83, 3.63, 7.20, 2.68, 2.05, 2.96, 1.04, 0.00, 0.03, 6.71, 8.28, 6.85]
    mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 
            'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    
    # a) Calcul des totaux et moyennes
    total_bos = sum(BOS)
    total_mer = sum(MER)
    moy_bos = total_bos / 12
    moy_mer = total_mer / 12
    
    # b) Mois supérieurs à la moyenne
    sup_moy_bos = sum(1 for x in BOS if x > moy_bos)
    sup_moy_mer = sum(1 for x in MER if x > moy_mer)
    
    # c) Mois où Boston < Seattle
    mois_inf = [(mois[i], BOS[i], MER[i]) for i in range(12) if BOS[i] < MER[i]]
    
    return {
        'totaux': (total_bos, total_mer),
        'moyennes': (moy_bos, moy_mer),
        'sup_moyenne': (sup_moy_bos, sup_moy_mer),
        'boston_inf_seattle': mois_inf
    }

def main():
    resultats = analyse_precipitations()

    print(f"a) Précipitations totales et moyennes:")
    print(f"Boston - Total: {resultats['totaux'][0]:.2f} pouces, Moyenne: {resultats['moyennes'][0]:.2f} pouces/mois")
    print(f"Seattle - Total: {resultats['totaux'][1]:.2f} pouces, Moyenne: {resultats['moyennes'][1]:.2f} pouces/mois")

    print(f"\nb) Nombre de mois au-dessus de la moyenne:")
    print(f"Boston: {resultats['sup_moyenne'][0]} mois")
    print(f"Seattle: {resultats['sup_moyenne'][1]} mois")

    print(f"\nc) Mois où Boston < Seattle:")
    for mois, bos, mer in resultats['boston_inf_seattle']:
        print(f"{mois}: Boston ({bos:.2f}) < Seattle ({mer:.2f})")

if __name__ == "__main__":
    main()
