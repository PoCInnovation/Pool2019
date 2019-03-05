status: hidden
Template: waiting
odate: 2019-02-06T09:00:00
Title: Jour 03 - Découverte de Tensorflow

⚠ **Attention** ⚠

N'oubliez pas que vous n'êtes pas noté, prenez le temps de comprendre correctement chaque exercices, Tensorflow sera votre outil de travail pour la suite de la piscine.

Les exercices de cette journée sont très peu guidés volontairement, nous souhaitons vous apprendre comment se documenter seul dans un milleu scientifique et en constante évolution.

PS: Evitez quand même de copier le code sur internet sinon c'est NO FUN. 

PS PS: Vraiment

# Introduction

Tensorflow est une librairie open-source très puissante développée par Google Brain pour le développement des **Deep Neural Networks** (DNNs). La librairie a été dans un premier temps disponible en novembre 2015 sous license Apache 2.x, le github du projet possède plus de 800 contributeurs pour + de 17.000 de commits en seulement 2 ans. 

Voyons dans un premier temps pourquoi Tensorflow s'illustre comme le Framework n°1 dans le développement de DNN. Tensorflow permet le déploiement grandement facilité sur plusieurs CPU, plusieurs GPU, dans un serveur, un smartphone, un laptop. Il y a énormement de librairies pour le développement de DNN aujourd'hui (PyTorch, Theano, Caffe, MxNet)

La plupart de ces librairies possède un système d'auto-dérivation (**auto-differentation** in english my friend), elles supportent aussi la répartition sur CPU / GPU et ont la plupart des modèles connus directement implémentés (CNNs, RNNs, DBNs).

Vous vous demandez surement ce qui rend Tensorflow spécial ?

- Tensorflow fonctionne avec beaucoup de languages (Python, C++, Java, R, Go, etc..) et même la plupart des languages qui sorte encore aujourd'hui propose des "Bindings" avec l'API C++ de Tensorflow
- Tensorflow fonctionne sur plusieurs plateformes (Mobile, Distribué)
- Tensorflow est supporté par tout les **cloud providers** (AWS, Google, Azure)
- Keras une API **haut niveau** très connue a été intégrée avec Tensorflow et le rend encore plus simple d'utilisation 
- Tensorflow facilite énormement la mise en production 
- Tensorflow possède une très bonne communauté pour le support
- Tensorflow est plus qu'un framework, c'est une suite, composée de Tensorflow, Tensorboard, TensorServing

---

## Installation

> Nous travaillerons exlusivement sous python 3.x, merci de ne pas utiliser python 2 afin d'éviter des questions inutiles.

L'installation de Tensorflow est relativement simple, elle se fait de cette manière:

```shell
pip3 install tensorflow --user
```

Vous pouvez vérifier votre installation Tensorflow en tapant ces quelques lignes dans votre interpreteur python3:

```bash
python3
```

Puis tapez:

```python
import tensorflow as tf
print(tf.__version__)
```

Si vous avez rencontré un problème lors de l'installation et que vous avez trouvé la solution, merci de la communiquer sur le chat de la piscine.

---

## Graph Tensorflow

Tensorflow représente tout les calculs qui seront effectués sous forme de [graph](https://en.wikipedia.org/wiki/Graph_theory) de calcul.

Chaque noeuds de ce graph est nommé [**Tensor**](https://www.tensorflow.org/guide/tensors), en mathématiques un Tenseur est un concept qui permet de généraliser: les scalaires, les matrices, les vecteurs et les données ayant des dimensions encore plus élevées.

Tensorflow à choisi de représenter les noeuds par des tenseurs car chaque noeuds du graph représente enfaite une opération qui produira éventuellement une matrice, un vecteur, un scalaire ou même rien du tout.


<img style="width: 350px" src="https://www.oreilly.com/library/view/hands-on-machine-learning/9781491962282/assets/mlst_0901.png"></img>

Ce type de graph ce lit du bas vers le haut: 
 
1. On multiplie $x$ par lui même pour $x \longrightarrow x²$. 
2. L'étape suivante est de multiplier le résultat de **l'étape 1** par $y$. 
3. On prend ensuite la variable $y$ et on l'additionne à la constante $2$. 
4. Ensuite on prend les résultats de ces deux opérations et on les additionnent. 

Cela constitue un moyen simple et très clair de représenter une fonction.
Mais Google a été encore plus loin en développant Tensorflow, grace à ce principe de graph il est également possible de répartir très facilement les calculs.


<img style="width: 350px" src="https://www.oreilly.com/library/view/hands-on-machine-learning/9781491962282/assets/mlst_0902.png"></img>

Sur cette image on voit qu'il est possible de découper notre graph en plusieurs blocs qui sont indépendants l'un de l'autre et c'est comme sa que Tensorflow gère comme un grand la répartition des calculs sur GPU.

Il est important de noter qu'un graph Tensorflow décrit uniquement les opérations à effectuer, aucune variables ne sont encore initialisées a la création du Graph.
  
---

## Session Tensorflow

Une session Tensorflow (```tf.Session```) permet de charger un graph de calcul et d'executer les tenseurs individuellement, elle s'occupe aussi d'initialiser les variables.

Il est possible d'avoir plusieurs sessions qui executent le même graph de calculs mais avec des variables différentes.

Un exemple d'execution de graph dans une session:

<img src="https://www.tensorflow.org/images/tensors_flowing.gif"></img>

---

## Hello world dans Tensorflow

Le premier programme que vous allez créer en utilisant Tensorflow va simplement afficher un message sur votre Terminal.

Dans votre interpréteur python3 commencer par importer Tensorflow:

```python
import tensorflow as tf
```

On créer un tenseur qui représente une variable **constante** (```tf.constant```), dans notre cas il s'agira d'une chaine de caractères:

```python
message = tf.constant('1v1 rust only flashscope')
```

On initialise une session Tensorflow puis on execute le Tenseur avec la méthode ```run``` de notre ```tf.Session```:

```python
session = tf.Session()
result = session.run(message).decode()
print(result)
```

> Output: 1v1 rust only flashscope

Si vous lisez la documentation Tensorflow sur la session, vous remarquerez surement qu'il est possible de donner un graph en paramètre or nous n'en avons pas fourni ici.
Cela s'explique car par défault tout les tenseurs qui sont crées sont automatiquement stockés dans le graph "Global", si aucuns paramètres n'est fourni à ```tf.Session``` celle ci charge le graph Global.

On aurait aussi pu définir un graph qui n'est pas global:

```python
mock_graph = tf.Graph() 

with mock_graph.as_default() as g:
	message = tf.constant('1v1 rust only flashscope')
	
session = tf.Session(graph=mock_graph)

print(session.run(mock_graph).decode())

tf.reset_default_graph()
```

Ici on utilise ```tf.Graph()``` pour créer un nouveau graph Tensorflow.  
On dit ensuite à Tensorflow que le nouveau graph considéré par default est le graph que nous venons de créer, ainsi tout les tenseurs qui seront crées par la suite seront automatiquement ajoutés à ce graph:

```python
with mock_graph.as_default() as g:
	... code here ...
```

Enfin la dernière étape est ```tf.reset_default_graph()```qui permet de dire à Tensorflow que le nouveau graph par défault est le graph Global.

## Comprendre les graphs Tensorflow

Nous aimerons reproduire le graph de calcul suivant:

![graph ex01](https://raw.githubusercontent.com/PoCFrance/Pool2019/master/ai//images/d03/ex01.png)

En outre cela revient à reproduire l'équation $x = 2^2 + 3^2$:

Pour cela nous allons créer 2 Variables (```tf.Variable```), ces variables sont des valeurs qui peuvent être uniquement modifiées par la session Tensorflow, elles ne peuvent pas être modifiées à partir de l'exterieur.

```python
import tensorflow as tf

var1 = tf.Variable(2)
var2 = tf.Variable(3)

var1_add = var1 * var1
var2_add = var2 * var2

result = var1_add + var2_add

sess = tf.Session()

print('Result of (2*2) + (3*3): ',  sess.run(result))

```
> Output:
> Error

Ce code ne fonctionnera pas, contraitement au ```tf.constant```, la session n'initialise pas automatiquement les ```tf.Variable```, il faut lancer l'initializer de chaque tenseurs.

```python3
sess.run(var1.initializer)
sess.run(var2.initializer)

print('Result of (2*2) + (3*3): ',  sess.run(result))
```
> Output:
> 13

Lorsque votre projet prend de l'ampleur il devient vite embetant de devoir appeler tout les initializers un part un vous pouvez donc faire appel à ```tf.global_variables_initializer()```

```python3
sess.run(tf.global_variables_initializer())
print('Result of (2*2) + (3*3): ',  sess.run(result))
```

### Exercice 01

Dans un fichier **ex01.py**  
Reproduisez le graph de calcul Tensorflow qui représente l'équation: $$x = (3*2^2) - 12^5$$

## La notion de placeholder

Jusqu'a présent nous pouvions uniquement modéliser des équations mais nous aimerions pouvoir modéliser des fonctions prenant des paramètres qui peuvent être changés à chaque execution de tenseurs.

Nous allons représenter une fonction très basique: $$f(x) = 3x + 2$$

```python
import tensorflow as tf

# Tout les tenseurs peuvent être nommés, prenez l'habitude de le faire
x = tf.placeholder(tf.int32, name='x')
result = 3 + x + 2
```

Un ```tf.placeholder``` permet de créer un tenseur qui va contenir un futur paramètre, comme son nom l'indique voyez un placeholder comme "une boite qui contient une valeur"

Les valeurs de nos placeholders doivent être donnés à l'execution du tenseur en utilisant le deuxième paramètre de ```tf.Session().run()``` nommé **feed_dict**.

Vous remarquerez aussi qu'aucune variables n'ont été créees pour $3$ et $2$, c'est parce que Tensorflow detecte qu'il s'agit de constantes et déclare automatiquement des ```tf.constant```

Maintenant que nous avons modélisé cette fonction, nous pouvons l'executer plusieurs fois avec des valeurs différentes sans avoir à créer une nouvelle ``tf.Session()``` à chaque fois.

```python

... suite du code çi dessus ...

sess = tf.Session()

print(sess.run(result, feed_dict={x: 3}))
print(sess.run(result, feed_dict={x: 10}))
print(sess.run(result, feed_dict={x: 100}))

```

> Output:
> 8
> 15
> 105

Notez cependant que Tensorflow créer des dépendances entre vos tenseurs, par exemple prenons cette fonction: $$ f(x, y) = 3x + y $$

```python3
import tensorflow as tf

x = tf.placeholder(tf.int32, name='x')
y = tf.placeholder(tf.int32, name='y')

result = 3*x+y

sess = tf.Session()
```

On essaye maintenant d'executer notre fonction en donnant seulement $x$:

```python
print(sess.run(result, feed_dict={x: 3}))
```

![nuclear](https://media.giphy.com/media/HhTXt43pk1I1W/200.gif)

Cela vient du fait que le tenseur $result$ a une dépendance sur $x$ mais également une dépendance sur $y$, ainsi il faut donner $x$ et $y$ dans notre feed dict pour que cela fonctionne:

```python
print(sess.run(result, feed_dict={x: 3, y: 2}))
```

> Output:
> 11

## La puissance des tenseurs

Reprenons la dernière fonction: $$f(x) = 3x + y $$

Jusqu'a présent, tout les graph que nous avons créers ne pouvaient prendre en paramètres que des scalaires (nombres).

Comme vu dans la deuxième journée, pour modéliser un réseau de neurones nous aimerions pouvoir tout représenter sous forme vectoriel.  

Tensorflow propose justement de faire les calculs sous forme vectoriel !
Pour cela il faut préciser la dimension de la donnée qu'on souhaite manipuler (shape en anglais), reprenons l'exemple çi dessous:

```python3
import tensorflow as tf

x = tf.placeholder(tf.int32, name='x')
y = tf.placeholder(tf.int32, name='y')

result = 3*x+y

sess = tf.Session()
```

Nous aimerions transformer ce code afin que $x$ et $y$ soit des vecteurs de dimension 5:

```python3
import tensorflow as tf

x = tf.placeholder(tf.int32, name='x', shape=[5])
y = tf.placeholder(tf.int32, name='y', shape=[5])

result = 3*x+y

sess = tf.Session()
```

Et voilà ! Notre graph est déja prêt à prendre en paramètres 2 vecteurs.
Il est important de noter que Tensorflow travaille avec la librairie Numpy, les paramètres $x$ et $y$ devront être de type Numpy.Array

Essayons de lancer quelque exemples:

```python
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])
print(sess.run(result, feed_dict={x: arr1, y: arr2}))
```
> Output:
> [8 10 12 14 16]

```python
arr1 = np.random.uniform(size=[5])
arr2 = np.random.uniform(size=[5])
print(sess.run(result, feed_dict={x: arr1, y: arr2}))
```

> Output:
> Random

## Les optimiseurs

Faire une descente de gradient à la main peut rapidement devenir répétitif et très vite compliqué à maintenir, Tensorflow propose donc des optimiseurs déja prêt à minimiser vos fonctions !

Prenons la même équation que précédement:

$$ x = θ₁ + θ₂ + 2 $$

Nous aimerions trouver les valeurs de θ₁ et θ₂ qui minimise l'équation.

On instancie déja notre équation:

```python
import tensorflow as tf

theta01 = tf.Variable(2)
theta02 = tf.Variable(10)
result = theta01 + theta02 + 2

sess = tf.Session()
sess.run(result)

```
> Output: 14

Puis on déclare un optimiseur (Descente de Gradient içi), on lui demande de minimiser l'output de notre equation

```
import tensorflow as tf

theta01 = tf.Variable(2)
theta02 = tf.Variable(10)
result = theta01 + theta02 + 2

sess = tf.Session()
optimizer = tf.train.GradientDescentOptimizer(0.1)
train_op = optimizer.minimize(result)
```

Ici nous avons dans un premier temps instancié un optimiseur, puis crée un tenseur d'optimisation, à chaque fois que ce tenseur est appelé, une étape de descente de gradient sera effectuée sur les paramètres de notre équation.
Il suffit de mettre cela dans une boucle pour voir le résultat:

```
import tensorflow as tf

theta01 = tf.Variable(2.0)
theta02 = tf.Variable(10.0)
result = theta01 + theta02 + 2.0

sess = tf.Session()
sess.run(tf.global_variables_initializer())
optimizer = tf.train.GradientDescentOptimizer(0.1)
train_op = optimizer.minimize(result)

for global_step in range(50):
	out, _ = sess.run([result, train_op])
	print(out)
```

Lancez ce code, vous verrez le résultat de notre expression diminue ! (Remarquez que les int32 on été passé en float32, les optimizers ne peuvent pas travailler avec des Int)

Comme vous pouvez le voir le résultat de notre équation diminue de plus en plus car nous la minimisons en fonction de $θ₁$ et $θ₂$

Un autre point important, en paramètre de **session.run()** nous avons donné une liste, cela permet d'executer plusieurs Tenseurs en un seul parcours de Graph.

## Faire le point

A l'heure actuelle vous savez:
	
* Modéliser une fonction dans Tensorflow
* Créer des constantes, des variables et des placeholders
* Minimiser une fonction

Prenez une pause, la journée commence maintenant 🙃

---

### Exercice 02

Dans un fichier **ex02.py**, commencez par importer Tensorflow et Numpy

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
```

Le but de l'exercice est d'effectuer une regression linéaire sur le prix des maisons à Boston.

Commencez par récuperer le dataset:

```python
boston = tf.contrib.learn.datasets.load_dataset('boston')
X_train, Y_train = boston.data[:, 5], boston.target
```

X_train et Y_train sont vos données d'entrainement pour cet exercice:

* **X_train**: nombre de chambres
* **Y_train**: prix de la maison

Vous pouvez afficher les données en utilisant matplotlib

```python
plt.scatter(X_train, Y_train)
plt.show()
```

Pensez toujours à prendre le temps d'explorer vos données d'entrainement, c'est vraiment important !

![plot ex02](https://raw.githubusercontent.com/PoCFrance/Pool2019/master/ai//images/d03/ex02_plot.png)

Il ne vous reste plus qu'a constituer le graph tensorflow et à entrainer votre modèle.
Si vous avez un doute n'hésitez pas à aller sur la documentation de Tensorflow, elle est très clair.

Pour la fonction d'erreur vous pouvez la définir vous même ou utiliser la [MSE](https://www.tensorflow.org/api_docs/python/tf/losses/mean_squared_error) de Tensorflow

Voici le genre de résultat à obtenir:

![result ex02](https://raw.githubusercontent.com/PoCFrance/Pool2019/master/ai//images/d03/ex02_result.png)

---

TIPS:

Vous pouvez déclarer une variable d'une valeur aléatoire en utilisant [```tf.random_uniform```](https://www.tensorflow.org/api_docs/python/tf/random/uniform). 
La shape précisée a ```tf.random_uniform``` est (), elle représente une dimension de 1, en gros juste un nombre (scalaire).

```python
var = tf.Variable(tf.random_uniform(()))
```

---

Selon vous comment pourriez vous faire pour augmenter la vitesse d'entrainement et la précision ?
Vous pouvez appeler un assistant pour donner votre opinion.

---

### Exercice 03

Il arrive souvent que notre résultat soit dépendant de plusieurs variables d'entrées, en réalité il est même très rare que le dataset soit dépendant que d'une seule variable.

Dans cet exercice nous utilisons le même dataset que l'exercice précent sauf que nous utilisons toutes les variables afin d'effectuer une [regression lineaire à plusieurs variables](https://www.hackerearth.com/fr/practice/machine-learning/linear-regression/multivariate-linear-regression-1/tutorial/).

Dans un fichier **ex03.py** commencez par importer les packages habituels:

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
```

Puis chargez le dataset complet:

```python
boston = tf.contrib.learn.datasets.load_dataset('boston')
X_train, Y_train = boston.data, boston.target
```

Pensez toujours à afficher les dimensions des données avec lesquels vous travaillez, car cela vous permet de définir vos placeholders, variables, etc...

Vous pourriez avoir besoin d'utiliser [```tf.reduce_mean```](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean)

---

## Sauvegarder un modèle

Vous vous êtes surement posé la question de comment il est possible de garder l'état de notre modèle après l'entrainement, car jusqu'à présent, une fois le script fermé, tout notre entrainement était perdu.

Tensorflow a pensé à une solution nommée ```tf.Saver``` c'est une solution très simple pour sauvegarder un modèle dans un état donné.

Pour sauvegarder:

```python
import tensorflow as tf

... modèle défini et entrainé ...

saver = tf.Saver()

saver.save('path/de/sauvegarde', sess)
```

Pour restaurer:

```python
import tensorflow as tf

... modèle défini et entrainé ...

saver = tf.Saver()

saver.restore(sess, 'path/de/sauvegarde')
```

Lors d'une restauration de modèle il suffit de définir une session mais pas besoin d'initialiser les variables, c'est le saver qui s'occupe de restaurer les valeurs de chaque paramètres.

---

## Tensorboard ##

Tensorflow propose un outil très puissant pour la visualisation de données, il se nomme Tensorboard.

Avec Tensorboard vous pouvez afficher énormément d'informations de nature différentes (images, scalaire, embedding, etc...).  
Pour cette piscine nous utiliserons uniquement l'affichage d'Images et de scalaires.


Pour utiliser Tensorboard il faut commencer par instancier un filewriter en donnant l'attribut 
```graph``` de notre ```tf.Session```:


```python
writer = tf.summary.FileWriter('path/vers/vos/logs', sess.graph)
```

Il faut ensuite créer des Tenseurs qui sérialise les tenseurs que l'ont souhaitent afficher dans tensorboard

```python
# On souhaite afficher la variable 'var1' qui est un scalaire
var1 = tf.Variable(2.7)

# On créer ensuite un tenseur de sérialisation
var1_summary = tf.summary.scalar(var1, name='variable1')

# Puis on l'ajoute a Tensorboard grace au FileWriter
filewriter.add_summary(idx, var1_summary)

```
**idx** représente le timestamp, essayer de le changer vous comprendrez l'interêt

Il ne vous reste plus qu'a lancé tensorboard de cette manière:

```bash
tensorboard --logdir='path/vers/vos/logs'
```

Et de visiter avec votre navigateur **127.0.0.1:6006**


### Exercice 04

Cet exercice est un peu comme le Hello World du deep learning, vous allez créer un modèle capable de reconnaitre des chiffres manuscrits !

L'exercice est composé de deux parties, une partie en utilisant **l'API bas niveau** de Tensorflow et une deuxième partie beaucoup plus courte ou nous aborderons **l'API haut niveau** de Tensorflow qui nous accompagnera durant tout le reste de la piscine.

Faites un réseau de neuronne comportant 784 neurones d'entrées, 300 neurones cachées et 10 neurones de sorties qui désignent une probablités pour chaque chiffres.

Posez vous la question de pourquoi 784 neurones en entrée, regardez bien les dimensions du dataset.

Le dernier layer de ce réseau désigne des probabilités, pour appliquer une non linéarité sur ce layer on utilise la fonction d'activation [**softmax**](https://fr.wikipedia.org/wiki/Fonction_softmax), c'est une fonction très utilisée dans les problèmes de classification, on la met sur le dernier layer uniquement car elle fixe les bornes de notre vecteur de sortie entre 0 et 1 (0 à 100%), elle est aussi beaucoup plus longue à calculer que la fonction sigmoid ([```tf.nn.softmax```](https://www.tensorflow.org/api_docs/python/tf/nn/softmax))

A titre d'exemple, voici ce que la fonction softmax produit comme résultat:


$$ z = (1;3;2,5;5;4;2) $$  

$$ softmax(z) = (0,011;0,082;0,050;0,605;0,222;0,030) $$

Vous pouvez appliquer la cross entropie, elle fonctionne également très bien avec la softmax, afin de vous faciliter la tache renseignez vous sur la [sparse softmax cross entropy](https://www.tensorflow.org/api_docs/python/tf/nn/sparse_softmax_cross_entropy_with_logits)

⚠ Pensez bien à regarder la formule appliquée par Tensorflow lors de l'utilisation de la sparse softmax cross entropy, appliquer 2 fois une non linéarité rend instable votre modèle.

Dans un fichier **ex04.png** commencez par importer:

```python
import tensorflow as tf
import numpy as np
```

Puis charger le MNIST Dataset:

```python
dataset = tf.keras.datasets.mnist.load_data(path='mnist.npz')
```

**TIPS**:
Vous pouvez créer une variable d'une shape spécifique, voiçi un exemple:

```python
W = tf.Variable(tf.random_uniform([300, 1])
```

![mnist](https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png)

---

### Exercice 05

Comme vous l'aurez remarqué pendant le dernier exercice, créer un réseau de neuronne avec l'API bas niveau de Tensorflow devient vite très long et répétitif, pour la suite de la piscine nous allons utiliser une API très haut niveau de Tensorflow, Keras.

L'installation de Keras ce fait ainsi:


```python
pip3 install keras
```

Je vous invite à lire le [guide de démarrage Keras](https://keras.io/getting-started/sequential-model-guide/)

Vous pouvez utiliser l'API fonctionelle ou sequentielle de Keras, prenez celle avec laquelle vous semblez le plus à l'aise.

TIPS:

- Vous aurez besoin des Dense layers

---

### Exercice 06

Reprenez le code précedement crée et essayer le avec ce nouveau dataset:

```python
tf.keras.datasets.fashion_mnist.load_data()
```

La dimension des données est la même, seule l'organisation du dataset change.

A votre avis, pourquoi la précision est médiocre ?

## Conclusion de la journée

Cette journée avait pour but de vous apprendre à résoudre les problèmes vous même avec une nouvelle technologie, aujourd'hui nous utilisons Tensorflow, peut être que demain vous utiliserez plutot PyTorch, vous devez être capable de vous adapter à plusieurs milleux différents. La data science n'échappe pas à cette mentalité, un bon data scientist est quelqu'un qui prend le temps de lire les nouveaux papiers de recherche et apprend comment les appliquer en production.

Enfin, vous avez vu que les réseaux de neurones ont leurs limite sur des données complexes, nous verrons demain comment remédier à cela.






