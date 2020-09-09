# Environnement de TPs Python pour les L1 UVSQ

## Prérequis
L'utilisation de ce projet suppose que vous avez suivi la procédure d'installation des différents outils.
Cette procédure est détaillée dans le document [INSTALL.md](INSTALL.md).

## Utilisation du projet avec [Visual Studio Code](https://code.visualstudio.com/)
Toutes les manipulations de cette section sont à effectuer dans Visual Studio Code.

### Vérifier l'environnement utilisé
1. Dans la liste "EXPLORER" à gauche de l'écran, sélectionner le fichier "examples/hello/hello.py"
1. Vérifier dans la barre d'état en bas à gauche que l'environnement est bien "Python 3.8.X XX-bit ('l1-python': conda)"
    * si ce n'est pas le cas, sélectionner l'interpréteur Python 3.8 dans l'environnement l1-python "Python 3.8.X XX-bit ('l1-python': conda)" en cliquant en bas à gauche dans la barre d'état ou *Ctrl+Shift+P* puis sélectionner "Python: Select Environment")

### Exécuter un programme
* Hello
  1. Dans la liste "EXPLORER" à gauche de l'écran, ouvrir `examples/hello/hello.py`
  1. Cliquer sur le triangle vert en haut à droite de la fenêtre de l'éditeur Python
* explot (test de `matplotlib`)
  1. Dans la liste "EXPLORER" à gauche de l'écran, ouvrir `examples/explot/explot.py`
  1. Cliquer sur le triangle vert en haut à droite de la fenêtre de l'éditeur Python
* Kata _Fizzbuzz_ (avec tests unitaires)
  1. Dans la liste "EXPLORER" à gauche de l'écran, ouvrir `examples/fizzbuzz/test_fizzbuzz.py` ou `examples/fizzbuzz/fizzbuzz.py`
  1. Cliquer sur le triangle vert en haut à droite de la fenêtre de l'éditeur Python
* Interface graphique (test de `tkinter`)
  1. Dans la liste "EXPLORER" à gauche de l'écran, ouvrir `examples/gui/example01.py`, `examples/gui/example02.py` ou `examples/gui/example03.py`
  1. Cliquer sur le triangle vert en haut à droite de la fenêtre de l'éditeur Python
* Notebook Jupyter
  1. Dans la liste "EXPLORER" à gauche de l'écran, ouvrir `examples/exjupyter/exjupyter.ipynb`
  1. Sélectionner l'interpréteur Python "Python 3.8.X XX-bit ('l1-python': conda)" en haut à gauche de la fenêtre du notebook
  1. Cliquer sur les deux petits triangles (*Run all cells*) du notebook

### Faire un exercice

### Sauvegarder les changements sur son compte `github`

### Remarque
* Pour ouvrir un *REPL Python* dans l'environnement courant, il faut ouvrir la *Command Palette* (`Ctrl+Shift+P`), puis taper *Python: Start REPL*.

## Utilisation du projet dans un terminal
### Activation de l'environnement
Il est nécessaire d'activer l'environnement du projet pour avoir accès à la version adéquat de Python ainsi qu'à toutes les bibliothèques.

```bash
conda activate l1-python
```

### Exécuter un programme
* Hello
  ```bash
  python examples/hello/hello.py
  ```
* explot (test de `matplotlib`)
  ```bash
  python examples/explot/explot.py
  ```
* Kata _Fizzbuzz_ (avec tests unitaires)
  ```bash
  python examples/fizzbuzz/test_fizzbuzz.py
  python examples/fizzbuzz/fizzbuzz.py
  ```
* Interface graphique (test de `tkinter`)
  ```bash
  python examples/gui/example01.py # dessiner dans la fenêtre
  python examples/gui/example02.py # dessiner dans la fenêtre
  python examples/gui/example03.py
  ```

### Validez un programme
Certains outils assistent le développeur dans l'écriture de programmes.
Ces outils forment la catégorie des *linters*.
Il en existe plusieurs pour la plupart des langages de programmation.
Il est bien entendu fortement recommandé d'utiliser ces outils pour vérifier ses programmes.

Deux d'entre eux sont disponibles dans cet environnement :
* [flake8](https://flake8.pycqa.org/en/latest/) qui valide en particulier le respect du style de codage [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* [mypy](http://mypy-lang.org/) qui valide statiquement les types utilisés

Pour les exécuter sur un fichier Python :
```bash
flake8 examples/fizzbuzz/fizzbuzz.py
mypy examples/fizzbuzz/fizzbuzz.py
```
