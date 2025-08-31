# Simulateur Machine Enigma 🔐

Un simulateur Python de la célèbre machine de chiffrement Enigma utilisée pendant la Seconde Guerre mondiale. Ce projet implémente le mécanisme de double rotation des rotors pour le chiffrement et déchiffrement de messages.

## 🎯 Description

La machine Enigma était un dispositif de chiffrement électromécanique utilisé pour sécuriser les communications militaires et diplomatiques. Ce simulateur reproduit le principe de fonctionnement avec :

- **Deux rotors** de substitution configurables
- **Mécanisme de rotation** automatique des rotors
- **Chiffrement/déchiffrement** bidirectionnel
- **Gestion des espaces** dans les messages

## ✨ Fonctionnalités

### 🔒 Chiffrement/Déchiffrement
- **Chiffrement simple** avec rotors statiques
- **Chiffrement Enigma** avec rotation automatique des rotors
- **Déchiffrement** pour retrouver le message original
- **Préservation des espaces** dans le texte

### ⚙️ Mécanisme des Rotors
- **Double rotation** : rotation du premier rotor à chaque caractère
- **Rotation cascade** : rotation du second rotor après un tour complet du premier
- **Configuration personnalisable** des rotors
- **Génération aléatoire** de nouveaux rotors

## 🔧 Comment ça marche

### Principe de Chiffrement Enigma

1. **Étape 1** : Trouver l'index de la lettre dans l'alphabet
2. **Étape 2** : Substitution par le premier rotor
3. **Étape 3** : Trouver l'index de la lettre substituée
4. **Étape 4** : Substitution par le second rotor
5. **Étape 5** : Rotation des rotors pour le caractère suivant

### Principe de Déchiffrement

1. **Étape 1** : Trouver la lettre dans le second rotor
2. **Étape 2** : Récupérer la position dans l'alphabet
3. **Étape 3** : Trouver cette lettre dans le premier rotor
4. **Étape 4** : Récupérer la lettre originale dans l'alphabet

### Mécanisme de Rotation

```
Rotor 1 : Rotation à chaque caractère
Rotor 2 : Rotation après 26 rotations du Rotor 1
```

## 📖 Utilisation

### Import du Module
```python
from enigma_simulator import *
```

### Fonctions Principales

#### 1. Générer des Rotors Aléatoires
```python
rotor1 = shuffle_alphabet()
rotor2 = shuffle_alphabet()
```

#### 2. Chiffrement Simple (Rotors Statiques)
```python
code(rotor1, rotor2, "votre message")
```

#### 3. Déchiffrement
```python
decode(rotor1, rotor2, "message chiffré")
```

#### 4. Chiffrement Enigma (Avec Rotation)
```python
message_chiffre = code_enigma(rotor1, rotor2, "votre message")
```

#### 5. Rotation Manuelle des Rotors
```python
nouveau_rotor = rotation(rotor_actuel)
```

## 💡 Exemples

### Exemple Basique
```python
# Rotors de démonstration
rotor1 = ['f', 'g', 'r', 'o', 'w', 'd', 'c', 'i', 'y', 't', 'p', 'z', 'u', 'a', 'h', 'm', 'l', 'q', 's', 'j', 'b', 'x', 'k', 'n', 'v', 'e']
rotor2 = ['u', 'i', 'f', 'e', 'w', 'x', 'z', 't', 'n', 'j', 'q', 'a', 'm', 's', 'h', 'c', 'l', 'o', 'v', 'd', 'b', 'y', 'g', 'k', 'p', 'r']

# Chiffrement
print("Message original : je suis en classe de nsi")
code(rotor1, rotor2, "je suis en classe de nsi")
# Sortie : "dg vipv gu orxvvg hg uvp"

# Déchiffrement
print("Message chiffré : dg vipv gu orxvvg hg uvp")
decode(rotor1, rotor2, "dg vipv gu orxvvg hg uvp")
# Sortie : "je suis en classe de nsi"
```

## 🔍 Détails Techniques

### Gestion des Caractères
- **Lettres minuscules** : a-z supportées
- **Espaces** : préservés dans le message
- **Autres caractères** : non supportés dans cette version

### Mécanisme de Rotation
- **Rotation simple** : décalage d'une position vers la droite
- **Rotation cascade** : le second rotor tourne après 26 rotations du premier
- **État des rotors** : modifié pendant le chiffrement Enigma

### Performance
- **Complexité temporelle** : O(n×m) où n = longueur du message, m = taille de l'alphabet
- **Complexité spatiale** : O(m) pour les rotors

## ⚠️ Limitations

### Caractères Supportés
- Uniquement les lettres minuscules (a-z)
- Les accents et caractères spéciaux ne sont pas gérés
- La casse n'est pas préservée

### Sécurité
- Les rotors sont générés avec `random()` (non cryptographiquement sûr)
- Pas de validation des entrées utilisateur
- Configuration des rotors visible en clair

### Fonctionnalités Manquantes
- Pas de plugboard (tableau de connexions)
- Un seul réflecteur implicite
- Pas de configuration de position initiale des rotors

## 🤝 Contribuer

1. **Fork** le projet
2. **Créer une branche** feature (`git checkout -b feature/amelioration`)
3. **Commit** les changements (`git commit -m 'Ajout fonctionnalité'`)
4. **Push** sur la branche (`git push origin feature/amelioration`)
5. **Ouvrir une Pull Request**

### Domaines de Contribution
- Amélioration de l'interface utilisateur
- Optimisation des performances
- Ajout de tests unitaires
- Documentation et exemples
- Support de nouveaux caractères
- Fonctionnalités historiquement exactes

## 📝 Licence

Ce projet est développé à des fins éducatives pour comprendre les principes de cryptographie historique.

## 👨‍💻 Auteur

Projet développé pour l'apprentissage de la cryptographie et de l'informatique historique.

---

**Note Pédagogique** : Ce simulateur est une simplification de la machine Enigma historique, conçu pour illustrer les concepts de base du chiffrement par substitution avec rotation mécanique.
