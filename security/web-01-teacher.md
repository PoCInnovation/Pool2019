---
layout: page
title: Une journée de sécurité web (01)
permalink: web-01-teacher
---

Les objectifs de la journée sont les suivants :

* faire comprendre le principe d'une injection SQL
* donner des automatismes dans l'exploitation de cette vulnérabilité
* présenter les cas classiques

Les étudiants qui ne connaissent pas la syntaxe SQL, particulièrement ceux
qui n'ont jamais utilisé un SGBD, risquent d'avoir du mal. La syntaxe peut
tout à fait s'apprendre sur le tas mais certains ont du mal à assimiler
plusieurs notions en même temps. On peut imaginer donner quelques exercices
de SQL avant, pour roder un peu.


## Exercice 00

Ce premier exercice permet à l'étudiant de visualiser ce qu'il fait. On cherche
à avoir ce "déclic".

Ceux qui n'ont jamais utilisé Docker vont peut être galêrer à mettre en place
l'application. Je sais qu'il n'y a littéralement qu'**une** commande à tapper
mais quand on connait pas Docker, ça peut perturber... On peut accepter de
taper les commandes à leur place, quitte à faire un petit cours Docker pour
les intéressés à la fin de la séance. On évite de perdre du temps avec le
déploiement.

Une fois l'application déployée... On a un champ, vulnérable. La requête
exécutée côté serveur est toujours renvoyée au client si elle est valide.
Les étudiants doivent **bien** observer leurs requêtes.

On commence par vérifier que le champ est bien injectable :

```sql
whatever"
```

On récupère une erreur, c'est tout bon. On pose l'`UNION` et on augmente le
nombre de colonnes jusqu'à ce que la requête soit valide :

```sql
" UNION SELECT 1, 2, 3 #
```

L'`UNION` est l'outil qui nous permet "d'augmenter" notre requête pour
ajouter ce qui nous intéresse dans les résultats. Or, pour que notre requête
soit valide, nous devons avoir le même nombre de colonnes deux des côtés de
l'`UNION`.

Cette méthode nous permet aussi de voir quels sont les champs qui sont
affichés sur la page. Ici, ce sont tous les champs (on peut voir un `1`, un `2`
et un `3` dans le rendu).

Nous connaissons le nom de la base de données mais il aurait pu être deviné
facilement. Il ne nous restes plus qu'à insérer les noms des colonnes et on
a notre payload finale :

```sql
" UNION SELECT pass, nickname, email FROM users #
```

Et c'est gagné !


## Exercice 01

Epreuve Root-Me donc pas de correction publique.

C'est une SQLi classique, on peut appliquer la même méthodologie que
pour l'exercice d'introduction. Il faut seulement s'imaginer la requête.


## Exercice 02

Epreuve Root-Me donc pas de correction publique.

Même méthodologie. Pour les étudiants qui vont trop vite, on peut leur
demander de faire fuiter le schéma de la table au lieu de deviner les noms
de colonne.


## Exercice 03

Epreuve Root-Me donc pas de correction publique. Mais vraiment, rien de
particulier, c'est juste de la pratique à ce stade... ;)


## Exercice 04

Epreuve Root-Me donc pas de correction publique.

Cette épreuve est différente car l'injection SQL doit se faire à l'aveugle.
La technique que nous avons utilisé précédemment ne fonctionnera pas
en raison d'un filtre.

L'approche du temps (*time based attack*) pourrait résoudre le problème. Mais,
encore plus simple... On utilise un `OR` pour valider une expression. Si
l'exression est vraie, on est connecté. Autrement, la connection échoue.

Nous allons tester la valeur recherchée caractère par caractère. On peut
utiliser la dichotomie pour gagner du temps.

La longueur peut être trouvée à l'avance avec la fonction SQL `LENGTH`.

On peut itérer sur la range ASCII, moins les caractères qui ne sont pas
imprimables.


## Exercice 05

Epreuve Root-Me donc pas de correction publique.

C'est du LDAP. Rien de particulier, il suffit de se lire
[un petit document](https://www.blackhat.com/presentations/bh-europe-08/Alonso-Parada/Whitepaper/bh-eu-08-alonso-parada-WP.pdf)
pour prendre la syntaxe.


## Exercice 06

Epreuve Root-Me donc pas de correction publique.


## Exercice 07

S'il vous plait, un retour !
