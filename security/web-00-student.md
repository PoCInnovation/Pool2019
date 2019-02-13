---
layout: page
title: Une journée de sécurité web (00)
permalink: web-00-student
---

Cette journée est une introduction à la sécurité web. Cette expression
regroupe généralement toutes les attaques que l'on peut infliger aux
sites web et autres applications que l'on consomme à travers un navigateur.

Il s'agit certainement de la branche la plus populaire de la sécurité
informatique. Les média grand public en parlent régulièrement, les entreprises
y mettent des sommes folles... Et ce n'est pas près de s'arrêter ! De plus en
plus de choses se passent sur le web. De nouveaux frameworks, de nouveaux
langages et de nouvelles technologies émergent tous les ans, chacun avec son
lot de vulnérabilités. N'hésitez pas à parcourir
[le site de l'OWASP](https://www.owasp.org/index.php/Main_Page) pour des
statistiques ou même des détails techniques. C'est vraiment une super
ressource.

Les compétences requises en sécurité web sont, entre autres :

* compréhension du protocole HTTP
* connaissance des langages/frameworks de programmation web...
* ...et des vulnérabilités qu'ils apportent
* utiliser Burp, scripting

Côté client, le langage roi est JavaScript. Nous verrons quelques
vulnérabilités *client-side* au cours de cette journée.

Côté serveur, on a une pluralité beaucoup plus imporante : PHP, JavaScript,
Python, Go, C++... On retrouve également des langages de base de données.

D'une manière générale, comprendre le langage dans lequel est écrit
l'application aidera grandement quand il s'agit de lui faire du mal.

Pour les besoins de cette piscine, nous avons dû choisir un langage cible
pour les épreuves serveur. Nous cherchions un langage très utilisé en
production mais présentant, par design, de nombreuses vulnérabilités. Un
langage très permissif qui vous permettrait de laisser libre cours à votre
créativité. Un langage regroupant toute la faune et la flore des problèmes de
sécurité dans les applications web. Nous parlons bien sur de PHP.


## Exercice 00

Pour ce premier exercice, vous allez devoir produire un schéma. L'objectif est
de visualiser ce qui se passe dans la situation suivante : un utilisateur
appuie sur le bouton "Se Connecter" d'un site web. L'utilisateur constate que
la page se recharge. Une fois le chargement terminé, il est connecté, et sur
sa page de profil.

Vous devez faire apparaitre les légendes suivantes :

* début de la requête vers le serveur web
* début de la requête vers la base de données
* utilisateur/navigateur
* fin de la requête vers le serveur WEB
* traitement de PHP
* fin de la requête vers la base de données
* côté serveur
* l'utilisateur voit qu'il est connecté
* côté client
* redirection vers la page du profil

Ne cherchez pas à faire quelque chose de joli. Un gribouillage sur un bout
de papier fera amplement l'affaire.


## Exercice 01

Continuons nos recherches sur le HTTP...

Répondez aux questions suivantes :

* quels sont les caractéristiques des
  requêtes `GET`, `POST`, `PUT` et `DELETE` ?
* prenons une requête `POST`, qu'est ce que le `Content-Type` ?
* par quel(s) moyen(s) standards peut on communiquer de la donnée au serveur
  dans le cas d'une requête `GET` ?
* déchiffrez `3%20%2B%202%20%3D%205%20est%20une%20%C3%A9galit%C3%A9%20vraie`,
  quelle est l'utilité de cette représentation ?

Vous allez maintenant assister à une démonstration du logiciel Burp. Soyez
attentif. Nous vous conseillons de tout de suite prendre l'habitude
de l'utiliser.


## Exercice 02

Vous devez affronter [cette épreuve](https://www.root-me.org/fr/Challenges/Web-Client/Javascript-Authentification-2).

Pour vous aider, répondez aux questions suivantes :

* cette application implémente-elle sa sécurité côté client ou côté serveur ?
* dans quel fichier cette sécurité est-elle implémentée ?
* comment sont stockés le nom d'utilisateur et le mot de passe ?

Enfin, expliquez pourquoi on ne fait **jamais** de sécurité côté client.


## Exercice 03

Vous devez affronter [cette épreuve](https://www.root-me.org/fr/Challenges/Web-Client/XSS-Stored-1).

Voici des questions pour vous aider :

* dans quels champs pouvez-vous injecter de la donnée sur cette page ?
* l'un de ces champs est-il vulnérable ? Que pouvez-vous injecter ?
* quel utilisateur consulte la page dans laquelle sera chargée votre injection ?
* que pouvez-vous voler à cette personne ?
* vous connaissez [RequestBin](https://requestbin.fullcontact.com/) ?
* comment pouvez-vous vous envoyer ce que vous souhaitez recevoir ?

Expliquez le principe d'une XSS. Expliquez la différence entre une XSS
**réfléchie** et une XSS **stockée**. Y'a-t-il des interactions avec le serveur
dans le cadre d'une XSS ?


## Exercice 04

Vous devez affronter [cette épreuve](https://www.root-me.org/fr/Challenges/Web-Client/CSRF-0-protection).

Nous allons réaliser un schéma afin de bien visualiser les étapes
de l'attaque. Vous devez faire apparaître les éléments suivants :

* l'attaquant élabore une charge utile à partir du formulaire permettant de
  passer admin
* l'administrateur consulte son back office et exécute la charge utile
  sans même s'en rendre compte
* l'attaquant est administrateur
* l'attaquant contacte l'administrateur, et joint sa charge utile au message
* l'attaquant n'est pas administrateur
* l'attaquant repère un formulaire permettant de passer admin

Expliquez le principe d'une CSRF. Donnez un exemple de mécanisme permettant
de s'en protéger.


## Exercie 05

Assez de sécurité côté client... Vous avez compris le principe : qui dit
point d'entrée mal filtré, dit vulnérabilité. Il ne faut jamais faire
confiance à l'utilisateur et surtout ne jamais lui permettre d'exécuter du
JavaScript là où bon lui semble.

Passons côté serveur...

Vous devez affronte l'épreuve numéro 17 de [WebSec](https://websec.fr/).

Un indice : les adeptes de PHP sont souvent de très bon jongleurs...


## Exercice 06

Vous devez affronter l'épreuve numéro 08 de [WebSec](https://websec.fr/).

Un indice : PHP est le genre de gars qui adore les emballages mais qui se
soucie assez peu du cadeau en lui même...

Un autre indice : au final, ça veut dire quoi "valide" ?


## Exercice 07

Vous devez affronter l'épreuve numéro 28 de [WebSec](https://websec.fr/).

Un indice : il va falloir aller vite...

Un autre indice : l'exercice 05 !


## Exercice 08

Merci de nous faire part de vos questions, remarques, suggestions ou quoi que
ce soit à l'adresse <lucas.santoni@epitech.eu>.

Merci aux créateurs d'épreuves sur Root-Me et WebSec pour leur merveilleux
travail.
