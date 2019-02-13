---
layout: page
title: Une journée de forensique
permalink: forensics-00-student
---

Cette journée est une introduction au *forensic* ou
**investigation numérique légale** en français. Le terme anglais sera
utilisé comme si c'était un terme français tout au long
de ce document : forensique.

Définition Wikipédia :

> On désigne par informatique légale, investigation numérique légale ou
> informatique judiciaire l'application de techniques et de protocoles
> d'investigation numériques respectant les procédures légales et destinée à
> apporter des preuves numériques à la demande d'une institution de type
> judiciaire par réquisition, ordonnance ou jugement. On peut donc également la
> définir comme l'ensemble des connaissances et méthodes qui permettent de
> collecter, conserver et analyser des preuves issues de supports numériques en
> vue de les produire dans le cadre d'une action en justice.
>
> Ce concept, construit sur le modèle plus ancien de médecine légale,
> correspond à l'anglais computer forensics.

Pour faire simple... On vous donne tel ou tel fichier, vous ne connaissez
pas forcément son origine, sa nature ou son utilisation mais vous devez vous
en servir pour prouver telle ou telle chose.

En forensique, on :

* Analyse des formats de fichiers inconnus
* Ecrit des scripts et programme pour automatiser l'analyse
* Analyse des dumps de mémoire vive
* Met en relation des évènements pour élaborer un scénario (d'attaque par exemple)
* Surement d'autres trucs

Le forensique n'a pas vraiment été touché par le 'tout en Python' ou le 'tout
en Javascript'. C'est un domaine où on manipule des offsets et où on aime bien
être très bas niveau ce qui fait du C un bon choix. Mais j'avoue, on retrouve
quand même pas mal le Python.

Un outil de forensique très populaire
est [Volatility](https://www.volatilityfoundation.org/). C'est un framework
Python pour l'analyse de dump RAM. Il marche super bien mais on galère à
retenir les commandes donc je vous donne tout de suite une cheatsheet avec
tout ce qui faut : [cliquez ici](https://downloads.volatilityfoundation.org/releases/2.4/CheatSheet_v2.4.pdf).

La plupart des épreuves de forensique que vous trouvez sur internet sont bien
entendu simulées. Il est assez rare de tomber sur le dernier format de fichier
inconnu et secret de Google ou un disque dur ayant servi de preuve dans une
affaire criminelle.


## Exercice 00

Faison un peu d'analyse mémoire. C'est amusant, ça ne demande pas beaucoup
d'effort, et ça revient souvent en CTF ! Pour tous les exercices suivants, vous
allez travailler sur [le fichier `dump_ram` fourni](https://cdn.geographer.fr/forensics_00_dump_ram.zip).

Ce fichier est un dump de la mémoire vive d'une machine virtuelle
qui sert de poste de travail à un certain Rick. Nous savons que ce Rick
a été infecté par un logiciel malveillant (le boulet...). Nous allons
mener l'enquête et essayer de comprendre ce qui se passe dans cette VM !

**IMPORTANT ! Ce fichier est tiré du OtterCTF et il est la propriété
de Asaf Eitani ! Mais je le trouvais cool alors je l'ai emprunté...**

Installez Volatility puis trouvez le profil adapté pour ce dump.


## Exercice 01

Les profils sont un peu comme une `struct` en C que l'on applique sur une
suite brute d'octets afin de leur donner un sens. Bien souvent, Volatility
trouve tout de suite le bon profil. Des fois, le bon profil n'existe pas
encore et il faut le construire (mais trop compliqué pour cette introduction).

Commençons par faire un peu de reconnaissance. Trouvez le nom de
l'ordinateur ainsi que le mot de passe de Rick.


## Exercice 02

Nous en savons désormais un peu plus. Un collègue souhaiterai jeter un oeil
au traffic réseau de cette machine virtuelle au moment de l'incident...

Quelle est l'adresse IP de la machine sur le réseau local ?


## Exercice 03

Ce n'est pas certain, mais on peut supposer que le malware qui a
infecté la machine communique avec un serveur distant.

Si tel est le cas, quel est l'IP de ce serveur distant ?


## Exercice 04

Jetons plutôt un oeil à la liste des processus en cours d'exécution.

Un de ces processus devrait attirer votre attention, lequel ? Un indice :
soyez attentif aux liens de parenté des processus. Il est rare que
`chrome.exe` soit légitimement le père de `svchost.exe`. ;)

Une fois le processus identifié, dumpez l'exécutable correspondant
ainsi que la mémoire au moment de l'exécution. Il est super intéressant de
pouvoir récupérer la mémoire correspondant à un processus en cours
d'exécution. En effet, en RAM, le contenu chiffré est souvent en clair... :p


## Exercice 05

Commencez par obtenir des informations sur le logiciel malveillant. A quel
famille appartient-il ? Est-il déjà répertorié ?


## Exercice 06

Retrouvez ensuite l'adresse de paiement. Un indice : bien que pas obligatoire
du tout, une machine virtuelle Windows n'est pas de trop pour faire de la
rétro-ingénierie sur ce genre de binaire...

Indice : vous ne savez pas quel logiciel utiliser ? On a besoin d'un
espion !


## Exercice 07

Nous aimerions comprendre comment ce malware est arrivé là... Je me souviens
avoir vu du client Bittorent dans le liste des processus en cours. Le collègue
qui a regardé les logs réseau confirme ceci (merci à lui !). Rick devait encore
être en train de récupérer des séries pour glander au bureau... Essayez d'en
savoir plus !

**Note : Pour cet exercice, deux flags (un par étape) sont présents dans le
dump. Vous n'êtes pas obligé de remonter les flags si vous pouvez expliquer
clairement comment l'ordinateur a été infecté, quels fichiers sont malveillants
et comment ils sont arrivés sur le disque.**


## Exercice 08

Bon... Rick a fait des bêtises, il se fera remonter les bretelles par la
direction. En attendant, il faut qu'on lui déchiffre ses fichiers à
ce boulet...

Retrouvez la clé de chiffrement utilisée pour prendre les fichiers de Rick
en otage. Un indice : il me semble que `.NET` fait des choses étranges
avec les chaines de caractères.


## Exercice 09

Enfin, déchiffrez les fichiers de Rick !

**Note : Pour cet exercice, un flag est attendu.**


## Exercice 10

Je suis toujours étonné de tout ce qu'on faire avec un dump RAM. Sans même
toucher à la machine virtuelle, nous avons pu reconstruire tout le scénario
de l'infection, obtenir la preuve que Rick est un boulet et trouver un moyen
de déchiffrer ses fichiers.

Pour finir, faites le point sur la journée, dites nous ce que vous avez aimé,
pas aimé, tous vos retours, ce que vous voulez... Et envoyez un petit
mail à <lucas.santoni@epitech.eu>.
