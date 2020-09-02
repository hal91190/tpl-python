# tpl-python
Un template pour un projet Python.

## Prérequis
* Un interpréteur Python (version >= 3.8)
  * en juin 2020 :
    3.7 ([Debian](https://packages.debian.org/search?keywords=python3&searchon=names&exact=1&suite=all&section=all)/stable),
    3.8 ([Debian](https://packages.debian.org/search?keywords=python3&searchon=names&exact=1&suite=all&section=all)/testion),
    3.5 ([Ubuntu](https://packages.ubuntu.com/search?keywords=python3&searchon=names&exact=1&suite=all&section=all)/16.04),
    3.6 ([Ubuntu](https://packages.ubuntu.com/search?keywords=python3&searchon=names&exact=1&suite=all&section=all)/18.04),
    3.8 ([Ubuntu](https://packages.ubuntu.com/search?keywords=python3&searchon=names&exact=1&suite=all&section=all)/20.04),
    3.8 ([Windows/python.org](https://www.python.org/downloads/windows/)), 3.8 ([Mac OS X/python.org](https://www.python.org/downloads/mac-osx/)),
    3.7/3.8 ([Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)/tous systèmes),
    3.8 ([python.org](https://www.python.org/downloads/)/tous systèmes)
* Le gestionnaire de paquets Python [`pip`](https://pip.pypa.io/en/stable/)
  * la distribution Python de [python.org](https://www.python.org/) à partir de la version 3.4 contient `pip`
* Le module `venv` pour la gestion des environnements virtuels ([tutoriel](https://docs.python.org/3/tutorial/venv.html))
  * Le module `venv` existe dans la bibliothèque standard Python depuis la version 3.3
* Un IDE
  * par exemple, [Visual Studio Code](https://code.visualstudio.com/) avec l'extension [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) ([tutoriel](https://code.visualstudio.com/docs/python/python-tutorial))

### Remarques
* Les distributions Python de [python.org](https://www.python.org/) ou [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html) fournissent de base l'ensemble des prérequis Python.
* L'installation de base de la distribution Anaconda contient l'IDE [Spyder](https://www.spyder-ide.org/) et les notebooks [Jupyter](https://jupyter.org/). Ce n'est pas le cas de Miniconda qui est beaucoup plus légère (400 Mo contre 3 Go).
* L'installation de paquet python avec `pip` peut provoquer une compilation et donc nécessiter des outils adéquats sur la machine. Ce n'est pas le cas avec Anaconda/Miniconda.

## Préparation initiale du projet
Les étapes de cette section ne sont à effectuer qu'une fois lors de la création du projet local.

### Cloner le dépôt
```bash
git clone https://github.com/hal91190/tpl-python.git projet
```
Il est préférable de *forker* au préalable le projet dans son espace github personnel pour ensuite le cloner.
Cela permet par la suite de valider les modifications ce qui n'est pas possible sur le projet original à cause des droits d'accès.

### Création et activation de l'environnement
* Avec la distribution [python.org](https://www.python.org/)
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
* Avec la distribution [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)
  ```bash
  conda env create
  conda activate envpython
  ```

### Installation des dépendances
* Avec la distribution [python.org](https://www.python.org/)
  ```bash
  pip install -r requirements.txt
  ```
* Avec la distribution [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)

  L'installation des dépendances est faite en même temps que la création de l'environnement.

## Utilisation courante du projet
### Activation de l'environnement
* Avec la distribution [python.org](https://www.python.org/)
  ```bash
  source .venv/bin/activate
  ```
* Avec la distribution [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)
  ```bash
  conda activate envpython
  ```

### Exécuter un programme
* Hello
  ```bash
  python3 exercises/hello/hello.py
  ```
* explot (test de `matplotlib`)
  ```bash
  python3 exercises/explot/explot.py
  ```
* Kata _Fizzbuzz_ (avec tests unitaires)
  ```bash
  python3 exercises/fizzbuzz/test_fizzbuzz.py
  python3 exercises/fizzbuzz/fizzbuzz.py
  ```

### Validez un programme
```bash
flake8 exercises/fizzbuzz/fizzbuzz.py
mypy exercises/fizzbuzz/fizzbuzz.py
```

## Notes sur [Visual Studio Code](https://code.visualstudio.com/)/[Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* Pour sélectionner l'interpréteur ou l'environnement Python adéquat, il faut ouvrir la *Command Palette* (`Ctrl+Shift+P`), puis taper *Python: Select Interpreter*.
* Pour ouvrir un REPL Python dans l'environnement courant, il faut ouvrir la *Command Palette* (`Ctrl+Shift+P`), puis taper *Python: Start REPL*.
* Pour ouvrir un terminal dans l'environnement courant, il faut ouvrir la *Command Palette* (`Ctrl+Shift+P`), puis taper *Terminal: Create New Integrated Terminal*.

## Notes sur le projet
Cette section contient des notes sur la façon dont le projet a été créé.
**Ces actions ne sont pas à reproduire lors de l'usage du projet.**

### Création et activation
* Avec la distribution [python.org](https://www.python.org/)
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
* Avec la distribution [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)
  ```bash
  conda create -name envpython
  conda activate envpython
  conda install numpy matplotlib jupyter
  ```

### Installation des _linters_ ([flake8](https://flake8.pycqa.org/en/latest/index.html#), [mypy](http://mypy-lang.org/))
* Avec la distribution [python.org](https://www.python.org/)
  ```bash
  pip install flake8
  pip install mypy
  ```
* Avec la distribution [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)
  ```bash
  conda install flake8 mypy
  ```

### Sauvegarder l'environnement
* Avec la distribution [python.org](https://www.python.org/)
  ```bash
  pip freeze > requirements.txt
  ```
* Avec la distribution [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)
  ```bash
  conda env export --name envpython > environment.yml
  ```
