# ReservationApp

Le but de ce projet est de créer une application de réservation de salle. Cette application comporte une interface graphique permettant à l’utilisateur d’interagir pour réserver des salles selon des horaires, ainsi que pour l’administrateur de pouvoir gérer les salles (en ajouter).

## Fonctionnalités

- **Réservation à la minute près** : possibilité de réserver une salle libre sur des horaires précis.
- **Affichage des salles disponibles** : visualisation des salles libres sur une plage horaire donnée.
- **Affichage des créneaux** : visualisation des créneaux libres ou occupés d’une salle.
- **Gestion des clients** : ajout, affichage, validation d’email.
- **Gestion des salles** : ajout, affichage, typage (Standard, Conférence, Informatique), capacité.
- **Réservations** : création, affichage, vérification de disponibilité, gestion des conflits.
- **Interface graphique** : navigation intuitive via Tkinter.
- **Sauvegarde/chargement** : sauvegarde automatique des données dans un fichier JSON.
- **Architecture claire** : séparation Model / View / Controller, managers dédiés pour chaque type de données.

## Utilisation

- **Accueil** : accès rapide aux principales fonctionnalités.
- **Ajouter** :
  - Ajouter un client (nom, prénom, email valide)
  - Ajouter une salle (nom, type, capacité)
- **Afficher** :
  - Liste des clients
  - Liste des salles
  - Salles disponibles pour un créneau donné
  - Réservations d’un client
- **Réserver** :
  - Choisir un client, un créneau, un type de salle, puis réserver une salle disponible.

## Sauvegarde et chargement

Les données sont automatiquement sauvegardées dans `data/data.json` à chaque modification (ajout client, salle, réservation).  
Au lancement, l’application recharge les données existantes.

## Architecture (Résumé technique)

- **Model** :
  - `ClientManager`, `RoomsManager`, `ReservationsManager` gèrent respectivement clients, salles, réservations.
  - Les entités (`Client`, `Room`, `Reservation`, `TimeInterval`) sont sérialisables en JSON.
- **View** :
  - Interface Tkinter, navigation par menus, affichage dynamique des listes et formulaires.
- **Controller** :
  - Fait le lien entre la vue et les managers, gère la logique et les erreurs.

## Tests

Des tests unitaires sont présents dans le dossier `tests`.  
Pour les lancer :

```bash
pytest

```
Auteurs :
- Lou Lemarechal lou.lemarechal@uha.fr
- Mael Le-goff mael.legoff@uha.fr