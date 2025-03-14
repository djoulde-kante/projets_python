import random

class Personne:
    def __init__(self, nom, proba_infection):
        self.nom = nom
        self.sante = "saine"
        self.proba_infection = proba_infection
    
    def infection(self):
        self.sante = "infectee"
    
    def immuniser(self):
        self.sante = "immunisee"
    
    def __str__(self):
        return f"Personne {self.nom} - État: {self.sante}"

class Population:
    def __init__(self, taille_population, proba_infection):
        self.individus = [
            Personne(f"P{i}", proba_infection) 
            for i in range(taille_population)
        ]
    
    def introduire_infection(self, nombre_infectes):
        personnes_saines = [p for p in self.individus if p.sante == "saine"]
        if len(personnes_saines) >= nombre_infectes:
            for personne in random.sample(personnes_saines, nombre_infectes):
                personne.infection()
    
    def simuler_jour(self, proba_guerison):
        infectes = [p for p in self.individus if p.sante == "infectee"]
        
        for personne in self.individus:
            if personne.sante == "saine":
                for _ in infectes:
                    if random.random() < personne.proba_infection:
                        personne.infection()
                        break
        
        for personne in infectes:
            if random.random() < proba_guerison:
                personne.immuniser()
    
    def __str__(self):
        sains = sum(1 for p in self.individus if p.sante == "saine")
        infectes = sum(1 for p in self.individus if p.sante == "infectee")
        immunises = sum(1 for p in self.individus if p.sante == "immunisee")
        return f"Population: {len(self.individus)} personnes\n" \
               f"- Saines: {sains}\n" \
               f"- Infectées: {infectes}\n" \
               f"- Immunisées: {immunises}"

def executer_simulation():
    pop = Population(1000, 0.1)
    
    pop.introduire_infection(10)
    
    for jour in range(30):
        print(f"\nJour {jour + 1}:")
        pop.simuler_jour(0.05)
        print(pop)

if __name__ == "__main__":
    executer_simulation()