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
    3.7/3.8 ([Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)/tous systèmes)
    3.8 ([python.org](https://www.python.org/downloads/)/tous systèmes)
* Un IDE
  * par exemple, [Visual Studio Code](https://code.visualstudio.com/) avec l'extension [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) ([tutoriel](https://code.visualstudio.com/docs/python/python-tutorial))
* Le gestionnaire de paquets Python [`pip`](https://pip.pypa.io/en/stable/)
  * la distribution Python de [python.org](https://www.python.org/) à partir de la version 3.4 contient `pip`
* Le module `venv` pour la gestion des environnements virtuels ([tutoriel](https://docs.python.org/3/tutorial/venv.html))
  * Le module `venv` existe dans la bibliothèque standard Python depuis la version 3.3

### Remarques
* L'installation de base de la distribution Anaconda contient l'IDE [Spyder](https://www.spyder-ide.org/) et les notebooks [Jupyter](https://jupyter.org/). Ce n'est pas le cas de Miniconda qui est beaucoup plus légère (400 Mo contre 3 Go).

## Utilisation du projet
### Cloner le dépôt
```bash
git clone https://github.com/hal91190/tpl-python.git projet
```

### Création et activation de l'environnement
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Installation des dépendances
```bash
pip install -r requirements.txt
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

## Création initial de l'environnement
### Création et activation
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Installation des _linters_ ([flake8](https://flake8.pycqa.org/en/latest/index.html#), [mypy](http://mypy-lang.org/))
```bash
pip install flake8
pip install mypy
```

### Sauvegarder l'environnement
```bash
pip freeze > requirements.txt
```
