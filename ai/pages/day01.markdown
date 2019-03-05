Title: Jour 01 - Découverte du machine learning avec la regression linéaire


#### ⚠ Attention ⚠

* Les notions abordées dans cette piscine sont purement mathématiques. Si certains ne sont pas à l’aise avec les maths, n’hésitez surtout pas à poser toutes vos questions à vos encadrants pédagogiques;

* Nous avons fait le choix d’utiliser des notations mathématiques plus ou moins rigoureuses. Ce choix a été motivé par le fait que toutes les avancées en matières d’intelligence artificielle se font via des démonstrations mathématiques, en voiçi un exemple: http://proceedings.mlr.press/v32/silver14.pdf . Ainsi, si vous décidez de continuer dans cette voie, vous serez déjà familiers avec cette rigueur.

* Il est également possible que certains se sentent complètement perdus. C’est normal ! L’intelligence artificielle est un concept très abstrait, fondé sur des principes mathématiques parfois complexes. Tenez bon et posez des questions. Ne lâchez rien !

<div style="page-break-after: always;"></div>

## Introduction au Machine Learning

Selon Wikipedia:
 > L'apprentissage automatique (en anglais machine learning, littéralement « l'apprentissage machine ») ou apprentissage statistique est un champ d'étude de l'intelligence artificielle qui se fonde sur des approches statistiques pour donner aux ordinateurs la capacité d' « apprendre » à partir de données, c'est-à-dire d'améliorer leurs performances à résoudre des tâches sans être explicitement programmés pour chacune.”

Selon cette définition, l’apprentissage automatique (ou machine learning / ML) consiste en l’élaboration d’un structure capable **d’apprendre à partir d’exemples**. En d’autres termes, le machine learning permet l’approximation d’une fonction définie par les exemples donnés au cours de l’apprentissage.
Un concept particulier est donc très important dans le machine learning: celui de “données”. Sans données, le modèle (mot signifiant cette structure capable d’apprendre) ne peut rien faire. Heureusement, grâce à l’arrivée d’internet, une masse très conséquente de donnée (plus ou moins open source) est à notre disposition, ce qui a permit l'essor du Deep Learning depuis 2010 environ.

Commençons par un exemple concret.

<div style="page-break-after: always;"></div>

## Analyse de la donnée

---

### **Exercice 1** - Découvrez la donnée:

Ouvrez le jeu de donnée [Blood.csv](https://github.com/PoCFrance/Pool2019/tree/master/ai/exercices/day01/Blood.csv) fourni avec le sujet grâce à un tableur.

Nous avons un ensemble de donnée de pression systolique (pression sanguine mesurée lors de la contraction du coeur) en fonction de l'âge de patients:

|Age|Systolic Blood Pressure (in millimeter of mercury)|
|---|---|
|39|144|
|47|220|
|45|138|
|47|145|
|...|...|

Nous allons, par la suite, apprendre comment créer un modèle capable de faire des prédictions de pression systolique en fonction de l’âge de nouveaux patients, non présents dans le jeu de donnée.

---

### **Exercice 2** - Visualiser la donnée:

En Data Science, visualiser et explorer sa donnée est primordial.
Tracez les valeurs de pression sanguine en fonction de l’âge des patients pour pouvoir mieux interpréter notre donnée.
Choisissez judicieusement le type de graphique le plus adapté à ce dataset.


<div style="page-break-after: always;"></div>

---

### **Exercice 3** - Interpréter la donnée:

Quel lien observez vous entre l’âge et la pression sanguine systolique ?
Selon vous, quelle fonction mathématique serait la plus adapte pour représenter cette donnée ?


---

<style>
.swag {
  text-decoration: none;
  display: inline-block;
  padding: 8px 16px;
}

.swag:hover {
  background-color: #ddd;
  color: black;
}

.previous {
  background-color: black;
  color: black;
}

.next {
  background-color: black;
  color: white;
}

.round {
  border-radius: 50%;
}
</style>

<a href="https://github.com/PoCFrance/Pool2019/tree/master/ai/subjects/day01-2.markdown" class="swag next">Partie 2 &#8250;</a>
