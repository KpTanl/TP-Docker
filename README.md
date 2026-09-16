# TP Docker

## Exercice 3 : Manipulation de base des conteneurs

Dans cet exercice, nous avons effectué les manipulations de base de Docker (téléchargement d'images, exécution et suppression de conteneurs). Toutes les étapes demandées ont été réalisées avec succès.

---

### 1. Vérification, téléchargement et exécution d'un conteneur

* **Étape 1** : Vérifier la version de Docker (`docker --version`)
* **Étape 2** : Lister les images disponibles localement (`docker images`)
* **Étape 3** : Télécharger l'image officielle depuis Docker Hub (`docker pull hello-world`)
* **Étape 4** : Exécuter un conteneur à partir de l'image (`docker run hello-world`)

![Vérification et exécution](ex-3/1.png)

---

### 2. Gestion et suppression du conteneur

* **Étape 5** : Lister les conteneurs en cours d'exécution (`docker ps`)
* **Étape 6** : Lister tous les conteneurs, actifs et arrêtés (`docker ps -a`)
* **Étape 7** : Supprimer le conteneur `hello-world` (`docker rm <ID_conteneur>`)

![Gestion et suppression du conteneur](ex-3/2.png)

---

### 3. Suppression de l'image Docker

* **Étape 8** : Supprimer l'image `hello-world` (`docker rmi hello-world:latest`) et vérifier la liste des images locales

![Suppression de l'image](ex-3/3.png)