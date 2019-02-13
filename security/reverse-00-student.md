---
layout: page
title: Une journée de rétro-ingénierie (00)
permalink: reverse-00-student
---

Cette journée est une introduction au *reverse*, ou **rétro-ingénierie**
(voire même ingénierie à reculon si vous êtes ce genre de personne) en
français. J'utiliserai le terme anglais reverse tout au long de ce document,
on va pas se prendre la tête.

Définition Wikipédia :

> La rétro-ingénierie, ou ingénierie inverse ou inversée, est l'activité qui
> consiste à étudier un objet pour en déterminer le fonctionnement interne ou
> la méthode de fabrication. On parle également de rétroconception et dans le
> domaine du vivant de biomimétisme. Le terme équivalent en anglais est reverse
> engineering.

Le terme dépasse donc largement le contexte de l'informatique... Mais pour des
raisons évidentes de logistique et de cohérence, nous allons rester dans le
domaine du reverse de logiciels.

L'idée est simple : vous récupérez un binaire, sans son code source, parfois
même sans symboles (on en parle ensuite) et vous devez comprendre comment le
bazar fonctionne. Les objectifs sont divers :

* faire une simple description exhaustive du comportement du binaire, utile
quand on a affaire à un logiciel malveillant inconnu
* comprendre un mécanisme de protection du logiciel, c'est souvent comme ça
que les cracks de jeu et autres sont faits
* accroître sa compréhension du développement logiciel, ça aide de savoir
ce que ça donne une fois compilé
* simplement se faire plaisir, c'est cool le reverse, ça fait travailler le
cerveau et ça élimine les gueules de bois

Il n'y a pas vraiment de langage de programmation à connaitre... Le Python
peut aider pour du scripting et le C rend service quand on veut faire des
tests un peu plus bas niveau mais ça peut toujours se remplacer. D'une manière
générale, connaitre le langage de programmation qui a servi à produire le
binaire que l'on veut reverse est une très bonne chose.

Quand on fait du reverse, on se retrouve face à un listing assembleur. On peut
donc se dire que c'est une bonne idée de connaitre ce langage. J'aime pas
vraiment considérer l'assembleur du reverse comme un langage de programmation.
Le listing que l'on voit est simplement une représentation plus humaine du
programme compilé. Il n'y a aucune différence entre la suite d'octets que l'on
peut observer dans un éditeur hexadécimal et les lignes d'assembleur que GDB
ou autre nous crache. L'assembleur du reverse peut totalement s'apprendre
sur le tas. Beaucoup d'instructions tombent sous le sens, se ressemblent et
les plus compliquées sont très bien expliquées sur internet.

Les débutants en reverse sont souvent effrayés par les listings assembleur.
Une fois le code désassemblé, ils ne savent pas par où commencer et quoi
faire. Afin d'éviter ce problème :

* Prenez le temps de traduire le code assembleur en C. C'est très long
et très fastidieux mais ça permet d'avancer au début et au bout de quelques
fois, on peut tout faire de tête.
* Mémorisez et recherchez les "patterns" de
[control flow](https://en.wikipedia.org/wiki/Control_flow) : conditions,
boucles, sauts, appels de fonction... Ce sont à ces endroits là qu'il y a de
l'action !

**Attention : Nous attendons des réponses complêtes et exhaustives de votre
part. Que vous trouviez le mot de passe d'un exercice ne nous intéresse
en réalité pas vraiment... Ce sont les questions qui attireront votre attention
sur les notions importantes et qui vous permettront de progresser.**


## Exercice 00

En parlant de GDB ! Il s'agit du débogueur/désassembleur que vous allez
utiliser pendant cette journée.

Installez GDB puis installez [PEDA](https://github.com/longld/peda).

Au passage, un peu de vocabulaire :

* un débogueur est un logiciel qui vient se mettre au dessus d'un autre binaire
afin de monitorer son exécution et permettre de mettre le programme en pause,
placer des points d'arrêts, inspecter le contenu des registres ou de la
mémoire... (exemple: GDB)
* un désassembleur est un logiciel qui, à partir d'un binaire compilé, vient
nous générer un listing assembleur (exemple: `objdump -D`)
* un décompilateur est un logiciel qui, à partir d'une binaire compilé, vient
nous générer un pseudo-code, souvent proche du C (exemple: Hex-Rays Decompiler,
parfois surnommé *F5 dans IDA*)

GDB a beaucoup de commandes, gardez
[une cheatsheet](https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf) sous le
coude. Un assistant va ensuite vous faire une démo, soyez attentif !


## Exercice 01

Téléchargez le fichier [bin01](assets/reverse-00/ex01/bin01).

Désassemblez le binaire et étudiez son fonctionnement.

Vous devez écrire un code C identique à celui utilisé pour générer ce binaire.

**Note : Le simple fait de lancer le programme ne suffit pas pour pouvoir
reproduire son code source. Vous devez absolument le désassembler.**


## Exercice 02

Téléchargez le fichier [bin02](assets/reverse-00/ex02/bin02).

Ce binaire demande un mot de passe... On appelle ça un *crackme* ou un
*reverseme*. C'est un logiciel qui a été développé dans le seul but de produire
un exercice de reverse.

Quel est le mot de passe demandé ? Avez vous vraiment besoin de GDB pour le
trouver ?

Indice : I wanna be tracer !


## Exercice 03

Téléchargez le fichier [bin03](assets/reverse-00/ex03/bin03).

Désassemblez le binaire et étudiez son fonctionnement. Répondez ensuite
aux questions suivantes :

* observez le prologue de la fonction `main`, combien d'octets sont alloués
pour les variables locales de la fonction ?
* repérez la boucle de la fonction `main`, identifiez les variables locales
utilisées
* que fait cette boucle ?
* à quelle adresse se trouve le flag demandé ?
* donnez un numéro de ligne où ce pointeur est déréférencé
* quel est le mot de passe demandé ?


## Exercice 04

Téléchargez le fichier [bin04](assets/reverse-00/ex04/bin04).

Désassemblez le binaire et étudiez son fonctionnement. Répondez ensuite
aux questions suivantes :

* observez les lignes +132 à +137 du listing du main, que se passe-t-il ?
* même question pour les lignes +152 à +158
* que fait la fonction `soap` ?
* comment ses arguments lui sont passés ?
* comment la valeur de retour de la fonction est elle récupérée ?
* l'adresse `ds:0x80498f8`, utilisée en +228, est préfixée par ce `ds`, pourquoi ?
* avec X l'opération XOR, nous avons A X B = C : comment retrouver A en
connaissant B et C ?
* quel est le mot de passe attendu ?


## Exercice 05

Téléchargez le fichier [bin05](assets/reverse-00/ex05/bin05).

Ce binaire a été strippé, il ne contient donc pas de symboles. Parmi les
symboles, nous avons par exemple :

* des noms de fonction
* des noms de variables
* des bouts du code source original

Sans les symboles, le débogage est plus compliqué. Surtout, le "démarage" est
plus compliqué car on ne peut pas lâcher un `disas main` et commencer à se
repérer à partir de là.

Utilisez `readelf` ou GDB pour récupérer le point d'entrée du programme.
Existe-t-il un lien entre le point d'entrée du programme et l'adresse de la
fonction main ?

Répondez ensuite aux questions suivante :

* donnez l'adresse de la fonction `main`
* trouvez l'adresse à laquelle est stockée le flag
* trouvez le mot de passe demandé


## Exercice 06

Téléchargez le fichier [bin06](assets/reverse-00/ex06/bin06).

Ce binaire a l'air différent... Peut être que la commande `file` pourrait nous
donner plus d'informations ?

Trouvez le mot de passe demandé.

Un conseil : des fois, prendre le temps de trouver l'outil adapté est une
très bonne chose !


## Exercice 07

*Cet exercice est une création de **Oursin**, merci à lui !*.

Téléchargez le fichier [bin07](assets/reverse-00/ex07/bin07).

Encore un binaire qui a une tête bizarre... Il a pourtant l'air d'être de la
famille...

Répondez aux questions suivantes :

* quel langage a été utilisé pour écrire ce programme ?
* comment placer un point d'arrêt au début du programme dans GDB ?
* repérez la routine de vérification, quel est le mot de passe demandé ?
* BONUS : pourquoi le binaire est-il obèse ?


## Exercice 08

*Cet exercice est une création de **caillou**, merci à lui !*

Téléchargez le fichier [bin08](assets/reverse-00/ex08/siglol).

Trouvez le mot de passe demandé.

Cet exercice est plus dur que les autres. Vous n'aurez surement pas le temps de
le faire pendant la journée. N'hésitez pas à y revenir plus tard et poser des
questions à <sylvain.lefevre@epitech.eu> !


## Exercice 09

Pour finir, faites le point sur la journée, dites-nous ce que vous avez aimé,
pas aimé, tous vos retours, ce que vous voulez... Et envoyez un petit
mail à <lucas.santoni@epitech.eu>.
