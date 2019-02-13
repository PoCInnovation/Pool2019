---
layout: page
title: Une journée de sécurité web (00)
permalink: web-00-teacher
---

Les étudiants ont généralement déjà une idée de ce qu'est la sécurité web.

On peut leur conseiller d'utiliser Firefox et de dédier ce navigateur à
la sécurité web :

* laisser le proxy configuré sur Burp
* le navigateur Chrome embarque des protections contre les XSS/CSRF qui sont
  pénibles quand on veut justement en exploiter une

On peut aussi troller un peu sur PHP, ça fait jamais de mal. Ca vaut le coup
de parler [de la fin de PHP5](https://www.youtube.com/watch?v=yx2ks03d4mE).
On en profite pour faire de la pub pour
[Snuffleupagus](https://github.com/nbs-system/snuffleupagus), c'est gagné.


## Exercice 00

Dans l'ordre :

* côté client
* utilisateur/navigateur
* début de la requête vers le serveur web
* côté serveur
* traitement de PHP
* début de la requête vers la base de données
* fin de la requête vers la base de données
* redirection vers la page du profil
* fin de la requête vers le serveur WEB
* l'utilisateur voit qu'il est connecté

On part du principe que la redirection se fait côté serveur.


## Exercice 01

`GET`, `POST`, `PUT` et `DELETE` sont les quatre verbes HTTP que l'on
retrouve traditionnellment dans le `REST` :

* `GET` pour récupérer une ressource auprès du serveur
* `POST` pour mettre à jour une ressource, parfois créer
* `PUT` pour créer une ressource à l'emplacement spécifié par l'URI, parfois
  mettre à jour
* `DELETE` pour supprimer une ressource

Nous avons pris l'exemple d'une requête `POST` mais le `Content-Type` peut
en fait s'utiliser avec n'importe quel verbe HTTP, tant que la requête admet
un corps qu'il faut décrire. Le `Content-Type` décrit la nature (type *MIME*)
de la ressource. Quand on envoie de la donnée au serveur (un payload en JSON
par exemple), il faut faire attention à ce champ.

Dans le cas d'une requête `GET`, on peut communiquer de la donnée au serveur
via des paramètres URL
(`http://domain.com/page.html?param1_name=param1_value&param2_name=param2_value`)
ou bien par le corps de la requête. Les étudiants pensent souvent que seul
`POST` peut avoir un *body*...

Après déchiffrement, on obtient `3 + 2 = 5 est une égalité vraie`. La
représentation *percent encoded* ou *UR(I/L) encoded*, par abus de langage,
est là pour respecter d'obscures RFC. Dans les faits, nous devons respecter
cet encodage dans nos payloads et ça peut également être un moyen d'éviter
des filtres.

Pour la démonstration de Burp, on peut faire un rapide tour des fonctionnalités.
Il faut absolument présenter :

* la mise en place du proxy, avec Firefox
* l'interface proxy
* le *Send to...*
* le repeater
* le decoder (on en remet une couche sur l'*URL encoding*)

Pourquoi pas l'intruder mais le cas d'usage classique est une injection SQL,
ce qui est hors du scope de la journée, donc bof.


## Exercice 02

Epreuve Root-Me donc pas de correction publique.

Il ne faut jamais faire de sécurité côté client car on expose le mécanisme de
sécurité. Aussi fort qu'il soit, ce n'est qu'une question de temps avant
qu'il soit cassé. Le morceau de JavaScript le plus obfusqué du monde finira
toujours pas être nettoyé et compris.


## Exercice 03

Epreuve Root-Me donc pas de correction publique.

Nous avons une XSS à partir du moment où nous sommes en mesure d'injecter
dans la page du contenu interprétable par le navigateur. Dans le cas d'école,
on peut injecter du JavaScript dans la page afin de voler les *cookies* de
la victime.

Une XSS est **stockée** si le code injecté se retrouve dans un système de
stockage côté serveur. La charge utile est alors injectée automatiquement
dès qu'un utilisateur demande la (ou parfois les) page(s) vulnérable(s).

Une XSS est **réfléchie** quand elle n'est pas stored. La charge utile est alors
couplée à la requête en utilisant par exemple un paramètre `GET`. Le tout
est ensuite envoyé à l'utilisateur en espérant qu'il clique dessus.


## Exercice 04

Epreuve Root-Me donc pas de correction publique.

Dans l'ordre :

* l'attaquant n'est pas administrateur
* l'attaquant repère un formulaire permettant de passer admin
* l'attaquant élabore une charge utile à partir du formulaire permettant de
  passer admin
* l'attaquant contacte l'administrateur, et joint sa charge utile au message
* l'administrateur consulte son back office et exécute la charge utile
  sans même s'en rendre compte
* l'attaquant est administrateur

Le principe de la CSRF est de forcer un utilisateur plus privilégié à effectuer
une action à son insu.

Imaginons un lien permettant de supprimer un article sur un blog :
`https://blog.com/post/12/delete`. Si un utilisateur lambda clique sur ce
lien, une vérification côté serveur empêchera l'action de résoudre.

En revanche, si ce lien est transmis à un administrateur et que celui-ci le
visite dans le contexte de son navigateur, alors la vérification côté serveur
validera l'action étant donné que c'est la session de l'utilisateur
privilégié qui sera utilisée.

Quelques moyens permettant de profiter d'une CSRF :

* envoyer une balise `a` par mail et prier pour que la victime ne vérifie
  pas le lien avant de cliquer dessus
* envoyer un formulaire, caché (`hidden` en CSS) et automatiquement exécuté
  via JavaScript
* coupler la CSRF à une XSS et utiliser le JavaScript injecté par XSS
  pour faire la requête CSRF


## Exercice 05

Epreuve WebSec donc pas de correction publique.

L'indice fait référence au *type juggling* de PHP.


## Exercice 06

Epreuve WebSec donc pas de correction publique.

L'indice chercher à faire comprendre que valider la nature d'un fichier en
se fondant uniquement sur quelques octets n'est pas vraiment une bonne idée.


## Exercice 07

Epreuve WebSec donc pas de correction publique.

L'indice fait référence à une *race condition*.


## Exercice 08

Toujours insister pour avoir un retour.
