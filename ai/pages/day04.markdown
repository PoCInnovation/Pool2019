status: hidden 
Title: Jour 04 - Convolutional neural networks
Template: page
odate: 2019-02-07T09:00:00

## Introduction

Lors de l'exercice 6 de la journée d'hier vous vous êtes rendu compte que les réseaux de neurones dit **fully connected** atteignent rapidement leurs limites.

Nous avons besoin d'utiliser un nouveau type de réseau de neuronnes qui va nous permettre d'isoler des patterns dans les images et s'en servir pour effectuer une prédiction.

Ces réseaux sont nommés: **Réseaux de neurones convolutionnels** (CNN)


## Convolution

La convolution est une operation mathématiques qui permet d'appliquer un filtre (kernel) à une image, elle est définie par la formule suivante: $$ \sum _{m=-\infty}^{\infty} f(n-m)g(m) $$

D'une manière plus simple, voici à quoi ressemble une convolution avec un **kernel** de taille 3x3 et un **stride** de 1x1

![](https://cdn-images-1.medium.com/max/1600/1*ZCjPUFrB6eHPRi4eyP6aaA.gif)
![](https://perso.esiee.fr/~perretb/I5FM/TAI/_images/conv2.png)

La formule peut parraitre effrayante mais il s'agit enfaite d'une opération relativement simple, dans l'ordre:

* On défini un filtre (kernel) contenant des valeurs
* On multiplie la zone de l'image par les valeurs du filtre
* On additionne toutes les valeurs du résultat
* On considère la valeur comme le nouveau pixel
* Le kernel est ensuite décalé de en fonction de la valeur de stride (un stride de 1 en x fait en sorte que le kernel ne se décale que d'un pixel à chaque fois)



## L'interet

L'interet de la convolution est de pouvoir appliquer des filtres sur une image qui vont faire ressortir des caractéristiques.

Nous aimerions pouvoir determiner si une image est un **X** ou un **O**.

Prenons d'abord un **X**, peu importe l'orientation du **X** on retrouve globalement des patterns similaires à chaque fois:

![](https://cdn-images-1.medium.com/max/1600/0*jtfOkswl_0xj-6w4.)

On commence par définir des filtres qui nous permettent de faire ressortir des patterns du **X**, par exemple le premier filtre et le troisième font ressortir les **bras** du **X**, le deuxième fera ressortir le **centre**

![](https://cdn-images-1.medium.com/max/1600/0*zDTt4c1vVhvfFqKU.)

On applique le premier filtre:

![](https://cdn-images-1.medium.com/max/1600/0*laCerWrLFcMlyvs2.)

Pour obtenir le résultat suivant:

![](https://cdn-images-1.medium.com/max/1600/0*73S06iq-v_Y5JbNB.)

On y voit très clairement que les bras du X qui sont orientés de la même manière on une très haute valeur, nous avons donc bien isolé un des patterns du **X**.

On applique tous nos autres filtres pour obtenir un résultat de cette forme:

![](https://cdn-images-1.medium.com/max/1600/0*a0j7AIaCX_pJrtZF.)

On appelle cet ensemble de résultats, **features maps**

---

## Réseau convolutionnel

Nous savons maintenant comment isoler des features clés d'une image, mais dans la réalité ce n'est pas nous qui définissons les valeurs utilisées dans les filtres.

Les valeurs contenues dans les filtres font enfaite office de **poids**, notre réseau va venir adapter ces valeurs au cours du temps pour isoler de mieux en mieux les features importantes d'une images.

---

Un exemple plus concret:

Prenons un bébé, le bébé à sa naissance est incapable de déterminer s'il s'agit d'un chien ou non quand il en voit un.
Un jour ses parents lui explique qu'un chien est un animal qui possède (ce sont ses **features maps**):

* Des oreilles
* Des poils
* Un museau
* Des griffes

Le cerveau humain étant extremement bien conçu va assimiler cette information, ainsi quand le bébé verra un chien, il isolera d'abord **les features** qui caractérises un chien puis s'en servira pour determiner si il s'agit ou non d'un chien.

Les CNN tentent de reproduire ce comportement humain, dans un premier temps il ne sait pas reconnaitre les features clés de l'image, mais après de l'entrainement, comme le bébé il est capable de les isoler et de s'en servir pour effectuer des prédictions.

---

## Features de haut niveau et bas niveau

Comme dans un Fully connected, un CNN possède plusieurs couches d'extraction de données,
les premières couches vont venir isoler les features de haut niveau (le corps, la tête, le buste, etc..) et les dernières couches sont celles qui isolent les features de bas niveau (poils, griffes, couleurs des yeux, etc...).

Avec ce que nous avons actuellement vu, il est encore difficile d'atteindre des features de bas niveau car nous n'effectuons aucunes réduction de dimension, ce qui empeche le procédé de convolution de converger vers des features de plus bas niveau.

Pour cela nous devons utiliser une nouvelle opération dite, de Pooling.

---

## Pooling

![](https://cdn-images-1.medium.com/max/1600/0*M9dewX5fpO1arUBd.)

Le Pooling est une méthode permettant de prendre une large image et d’en réduire la taille tout en préservant les informations les plus importantes qu’elle contient. Les mathématiques derrière la notion de pooling ne sont une nouvelle fois pas très complexe. En effet, il suffit de faire glisser une petite fenêtre pas à pas sur toutes les parties de l’image et de prendre la valeur maximum de cette fenêtre à chaque pas. En pratique, on utilise souvent une fenêtre de 2 ou 3 pixels de côté et une valeur de 2 pixels pour ce qui est de la valeur d’un pas.

Après avoir procédé au pooling, l’image n’a plus qu’un quart du nombre de ses pixels de départ

Le résultat est que le CNN peut trouver si une caractéristique est dans une image, sans se soucier de l’endroit où elle se trouve (le pooling casse la notion spaciale). Cela aide notamment à résoudre le problème liés au fait que les ordinateurs soient hyper-littéraires.

Le pooling permet aussi d'augmenter la vitesse de calcul et aussi de converger vers des features de plus bas niveau comme dis précedement.

---

## RELU

Un élément important dans l’ensemble du processus est l’Unité linéaire rectifiée ou ReLU. Les mathématiques derrière ce concept sont assez simples encore une fois: chaque fois qu’il y a une valeur négative dans un pixel, on la remplace par un 0. Ainsi, on permet au CNN de rester en bonne santé (mathématiquement parlant) en empêchant les valeurs apprises de rester coincer autour de 0 ou d’exploser vers l’infinie.

C’est un outil pas vraiment sexy mais fondamental car sans lequel le CNN ne produirait pas vraiment les résultats qu’on lui connaît.


## Wrap up

Voilà l'ordre dans lesquelles vous pouvez trouver des couches d'un CNN:

![](https://cdn-images-1.medium.com/max/1600/0*HWjBSG5tB9XtVEnd.)

Il s'agit biensur d'un exemple, il existe des centaines d'architectures différentes.

---

## Une dernière étape

Les features maps en sortie de notre réseaux convolutionnel sont ensuite applaties pour former un **vecteur** de **features** qui peut etre ensuite donné à un fully connected qui s'occupera de la classification en fonction des features isolées.

![](https://cdn-images-1.medium.com/max/1600/0*eOpPyVVPU7jTA8gH.)

Pour enfin donner l'architecture complète:

![](https://cdn-images-1.medium.com/max/1600/0*TFoomaHKXGaaVcng.)

---

## Faire le point

Vous savez maintenant faire un CNN, nous n'irons pas plus loin dans les mathématiques des CNN car Tensorflow va les faire pour nous. Si vous êtes intéréssés par la théorie dérrière, je vous invite à lire [cet article](https://medium.com/@CharlesCrouspeyre/comment-les-r%C3%A9seaux-de-neurones-%C3%A0-convolution-fonctionnent-b288519dbcf8) qui m'a inspiré dans la rédaction du sujet.


## Exercice 01 : Application des poids/filtres
Pour cet exercice, le but est de compléter le [code]({filename}/exercices/d02ex01.py) fourni pour obtenir les résultats ci-dessous. L'image source est fournie pour cet exercice.

**a -**
Sur cette image les patterns horizontaux sont beaucoup plus prononcés :
![enter image description here](https://lh3.googleusercontent.com/OSeIvDlTSnTxReLOW94ypC6e-60F6zacujKN0tlNZ8asZYoQA03nHjkmcGULOpQibPfDWHbgreDp)

**b -**
Ici les patterns verticaux sont plus visibles (les pylônes) :
![enter image description here](https://lh3.googleusercontent.com/V3NR-paL17VgGvhnlB7pVb4VuztF1-ijR41vj1K2DsTIChAys2Hdur4cvMcUrfSMQ-NGxYEIBkh8 "vertical")

Télécharger l'image [**source**]({filename}/images/d04/source.jpg)

**TIPS:**

* tf.nn.conv2d

## Exercice 2 : Fashion 2.0
Rappelez-vous de l'exercice 6 du jour 3, vous avez entrainner un modèle à reconnaître des vêtements. Si vous avez eu beaucoup de mal à avoir une bonne présision, tout est normal. Ici vous allez découvrir la puissance d'un réseau de neurones convolutif. 
Le but de cet exercice est d'entrainer un modele à reconnaitres les images du dataset *fashion* avec un CNN (Convolutional neural network). 

**Vous devez respecter l'architecture suivante :**

* -> Une couche de convolution 2d
* -> Une couche de Max Pooling 2d
* -> Une couche de Convolution 2d
* -> Une couche de Max Pooling 2d
* -> Une couche de Convolution 2d
* -> Une couche dense
* -> Une couche de sortie
	
Vous devez determiner la taille des kernels, les strides, la quantité de filtres à produire (je vous laisse vous renseigner sur ce qui fonctionne le mieux)

**Importer le dataset :**

    from tensorflow import keras
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

**Les classes :** 

    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 
	    'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
	    
**Fonction Convolution 2d :**

    tf.layers.conv2d(...)

**Fonction Max Pooling 2d :**

    tf.layers.max_pooling2d(...)
    
    
  
## Exercice 3: CIFAR 10

Cet exercice va vous préparer au rush, la consigne est simple:

En utilisant le dataset [CIFAR 10](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10), créer un modèle capable de prédire l'objet en question. 

Afin de mettre en pratique tous ce que nous avons vu jusqu'a présent vous devez encapsuler le modèle dans une **command line interface** qui devra fonctionner de la sorte:

	

```bash
./predict [PATH VERS L'IMAGE A PREDIRE]
```

Devra donner:

```bash
Prédiction: Avion
```

**TIPS:**

* tf.train.Saver
* CNN
* Fully connected

