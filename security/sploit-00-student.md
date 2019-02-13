---
layout: page
title: Une journée d'exploitation (00)
permalink: sploit-00-student
---

L'objectif de cette journée est de vous faire découvrir le monde de
l'exploitation de binaire. On utilise en fait plus souvent l'expression
anglo-saxonne *binary exploitation*, souvent abrégée *exploit* ou même
*sploit*.

Le principe est simple... Vous savez que lorsqu'on écrit du code, on introduit
bien souvent des bugs. Ces bugs ont des causes tout à fait différentes mais
le résultat est presque toujours le même : une opération indésirable en
mémoire. Ecrire quelques octets de trop, lire un pointeur nul... Voilà de
quoi faire terminer prématurément le programme !

Ces erreurs de programmation sont très fréquentes quand on programme dans
un langage bas niveau comme le C où le programmeur est seul responsable
de la gestion de la mémoire. Nous sommes humains, nous faisons beaucoup
d'erreurs !

Des langages plus récents tentent de résoudre ce problème en déléguant la
gestion de la mémoire à des outils très complexes : ramasse-miettes (C#,
Go...), *ownership* (Rust, par l'intermédiaire du compilateur)... Avec plus
ou moins de succès !

Le plus important est que chacun de ces bugs est une vulnérabilité
potentielle. Admettons une écriture de 50 octets dans un tampon prévu pour en
accueillir... 20 ? Admettons aussi que les 50 octets écrits proviennent d'une
entrée utilisateur. Nous laissons donc l'utilisateur écrire 30 octets
arbitraires en mémoire. Les érudits appellent ça une primitive d'écriture et
c'est bien souvent suffisant pour faire crasher un shell à un programme
développé dans le seul but d'afficher des photos. Vous comprendrez mieux
après la démo.


## Exercice -01

Vous allez assister à une démonstration sur les points suivants :

* l'exploitation de binaire : pourquoi ?
* GDB pour l'exploitation de binaire
* étude d'un crash
* introduction au format *remote virtual machine*

Vous serez ensuite en mesure de répondre à la question suivante... Quand on
écrit "trop loin" en mémoire, parfois, le programme plante, pourquoi ?


## Exercice 00

Cet exercice ainsi que tous les suivants se passent sur une machine distante.
Pous vous connecter :

```
ssh ex00@louane.geographer.fr
```

Mot de passe : `ex00`.

*Pourquoi `louane.geographer.fr` ? Pour pouvoir [taper dans](https://www.youtube.com/watch?v=KHueIzyiCMA&feature=youtu.be&t=153) Louane, pardi !*

Chaque épreuve vous donne le mot de passe pour accéder au suivant. Vous
devez venir à bout de cette machine virtuelle ! Bon courage ! ;)

Pour vous aider, vous pouvez répondre aux questions suivantes :

* quelle est la taille du tampon alloué pour l'entrée utilisateur ?
* combien d'octets sont en fait écrits à l'adresse de ce tampon ?
* qu'est ce qui se trouve sur les quatre octets suivants la fin de l'espace
  alloué pour le tampon ?


## Exercice 00b

Attention au boutisme ! 😉


## Exercice 01

Essayons d'écrire quelque chose qui a du sens !


## Exercice 02

C'est à vous d'apporter vos affaires...


## Exercice 03

Une fois on a demandé à Sylvain d'expliquer `stdarg`. Il a répondu :

> Ben... Tu prends c'qui a sur le haut de la pile là, hop, hop, hop !

Et si vous tiriez profit de ça ?


## Exercice 04

I wanna be Tracer !


## Exercice 05

Pour ce challenge, la *stack* n'est pas exécutable. Il va falloir trouver
autre chose !


## Exercice 06

Hein ?


## Exercice 07

Pour finir, faites le point sur la journée, dites-nous ce que vous avez aimé,
pas aimé, tous vos retours, ce que vous voulez... Et envoyez un petit
mail à <lucas.santoni@epitech.eu>.
