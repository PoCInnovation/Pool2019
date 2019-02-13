---
layout: page
title: Une journée de sécurité web (01)
permalink: web-01-student
---

Durant votre [première journée](web-00-student.html) de
sécurité web, vous avez eu l'occasion de travailler sur des vulnérabilités
archi classiques. Cette journée sera exclusivement dédiée aux injections SQL.

La grande majorité des applications WEB utilisent un ou plusieurs systèmes de
gestion de base de données (SGBD), pour du stockage plus ou moins persistant.
Lorsque des entrées utilisateur sont utilisées dans les requêtes passées au
SGBD, les choses se compliquent.

Nous avons choisi de travailler sur SQL car il s'agit de la syntaxe la plus
répandue à l'heure actuelle. Une fois la logique d'injection assimilée,
il est facile de transposer les connaissances sur différents SGBD et
d'autres syntaxes.

Si vous n'avez jamais fait de SQL, vous pourrez apprendre sur le tas. Vous
allez juste galérer un peu.

Si vous êtes à l'aise avec SQL, vous irez surement assez vite une fois le
principe compris. Vous pourrez en profiter pour revenir sur la journée
précédente ou bien commencer la journée de demain.


## Exercice 00

L'objectif de ce premier exercice est de comprendre la logique d'une injection
et surtout de visualiser ce qui se passe.

Si ce n'est pas déjà fait, commencez par installer [Docker](https://www.docker.com/)
ainsi que [Docker Compose](https://docs.docker.com/compose/).

*Note : Si vous ne connaissez pas Docker... Il s'agit, pour faire très simple,
d'un outil vous permettant d'exécuter sur votre machine des applications
demandant des dépendances et configurations complexes sans avoir à toucher
à votre système. La, ou les, applications(s) tournent alors dans des
containers, plus ou moins isolés de votre système hôte.*

Lancez Docker.

Récupérez ensuite [le code](https://github.com/Geospace/sqli-platform) de
l'application vulnérable et placez-vous dans le dépot.

Lancez l'application :

```
docker-compose up
```

Attendez que tout démarre. Vous avez devant vous les journaux de l'application
et de sa base de données.

Rendez vous ensuite sur [le front](http://localhost:8080/) et soyez attentif
lors de la démonstration.

Vous devez obtenir les mots de passe stockés dans la base de données à l'aide
d'une injection SQL.


## Exercice 01

Vous devez maintenant comprendre la logique d'une injection SQL. Les exercices
suivants ne sont que des situations plus complexes.

Vous allez affronter [cette épreuve](https://www.root-me.org/fr/Challenges/Web-Serveur/SQL-injection-authentification).

Pour vous aider, quelques petites questions :

* quel champ est vulnérable ?
* imaginez la requête, comment la rendre valide tout en injectant ?
* combien de colonnes pour que la requête reste valide ?
* comment *augmenter* la requête afin de joindre aux résultats ce qu'on
  recherche ?


## Exercice 02

Vous allez affronter [cette épreuve](https://www.root-me.org/fr/Challenges/Web-Serveur/SQL-injection-string).

Quelques questions pour vous guider :

* vous savez qu'il existe d'autres champs que ceux de connexion, n'est ce pas ?
* combien de colonnes dans cette requête ?
* on va chercher le schéma de table ou on le devine ?


## Exercice 03

Vous allez affronter [cette épreuve](https://www.root-me.org/fr/Challenges/Web-Serveur/SQL-injection-numerique).

Vous êtes des grands maintenant, débrouillez vous ! ;)


## Exercice 04

Vous allez affronter [cette épreuve](https://www.root-me.org/fr/Challenges/Web-Serveur/SQL-injection-en-aveugle).

Pour cette épreuve, vous devez produire un script. Le choix du langage vous
revient. Si vous n'avez pas d'idées, utilisez Python, vous trouverez de l'aide
plus facilement.

Quelques questions :

* quel est le problème ? Qu'est ce qui rend cette épreuve différentes des
  précédentes ?
* pouvez-vous connaitre la longueur de ce que vous recherchez ? Ce serait
  quand même plus facile...
* sur quelle *range* de caractère pouvez-vous raisonnablement itérer ?


## Exercice 05

Vous allez affronter [cette épreuve](https://www.root-me.org/fr/Challenges/Web-Serveur/LDAP-injection-authentification).

Je sais bien que c'est pas du SQL. Et alors ? On est là pour s'amuser, non ?


## Exercice 06

Vous devez affronter l'épreuve numéro 21 de [WebSec](https://websec.fr/).

Cette épreuve est plus difficile que les autres. Donc, pas d'indice.


## Exercice 07

Merci de nous faire part de vos questions, remarques, suggestions ou quoi que
ce soit à l'adresse <lucas.santoni@epitech.eu>.

Merci aux créateurs d'épreuves sur Root-Me et WebSec pour leur merveilleux
travail.
