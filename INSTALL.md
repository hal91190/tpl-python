# Guide d'installation de l'environnement de TPs Python

## Installer Python
Python est un langage de programmation *interprété*.
Pour exécuter un programme écrit dans ce langage, il faut disposer d'un *interpréteur Python* ainsi que de certaines bibliothèques installées sur la machine.

Nous utiliserons la [version 3.8](https://docs.python.org/fr/3.8/whatsnew/3.8.html) de Python.
En 2020, c'est la version la plus récente du langage disponible sur la plupart des architectures de machine.

Pour simplifier l'installation des outils nécessaires, nous allons utiliser une *distribution Python*.
Il en existe plusieurs mais nous nous appuyerons sur la distribution [Miniconda](https://docs.conda.io/en/latest/miniconda.html) qui est une version allégée de la distribution [Anaconda](https://www.anaconda.com/products/individual).

### Installer la distribution **Miniconda**
1. Télécharger la version de [Miniconda](https://docs.conda.io/en/latest/miniconda.html) pour **Python 3.8** et **adaptée à votre système**.
    * pour Windows, télécharger [Miniconda3 Windows 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
    * pour Mac OS, télécharger [Miniconda3 MacOSX 64-bit pkg](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg)
    * pour Linux, télécharger [Miniconda3 Linux 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
1. Installer Miniconda
    * pour Windows, double-cliquer sur le fichier `.exe` téléchargé précédemment puis accepter les choix par défaut
    * pour Mac OS, double-cliquer sur le fichier `.pkg` téléchargé précédemment puis accepter les choix par défaut
    * pour Linux, ouvrir un terminal dans le répertoire où se trouve le fichier téléchargé et taper :
        ```bash
        sh Miniconda3-latest-Linux-x86_64.sh
        ```
        À l'affichage de :
        ```
        Welcome to Miniconda3 py38_4.8.3

        In order to continue the installation process, please review the license
        agreement.
        Please, press ENTER to continue
        >>> 
        ```
        Appuyer sur la touche ENTRÉE, puis la licence du logiciel va s'afficher :
        ```
        [...]
        Do you accept the license terms? [yes|no]
        [no] >>> yes
        ```
        Taper *yes*, puis à la question :
        ```
        Miniconda3 will now be installed into this location:
        /home/user/miniconda3

        - Press ENTER to confirm the location
        - Press CTRL-C to abort the installation
        - Or specify a different location below

        [/home/user/miniconda3] >>>
        ```
        Accepter le choix par défaut, enfin, répondre *yes* à
        ```
        Do you wish the installer to initialize Miniconda3
        by running conda init? [yes|no]
        [no] >>> yes
        ```
        Fermer ensuite votre terminal.

1. Tester l'installation
    * sous Windows, ouvrir un *Anaconda Prompt*; sous Mac OS ou Linux, ouvrir un terminal et taper :
        ```bash
        conda list
        ```
        doit afficher une liste de bibliothèques :
        ```bash
        # packages in environment at /home/user/miniconda3:
        #
        # Name                    Version                   Build  Channel
        _libgcc_mutex             0.1                        main  
        brotlipy                  0.7.0           py38h7b6447c_1000  
        ca-certificates           2020.7.22                     0  
        certifi                   2020.6.20                py38_0  
        cffi                      1.14.2           py38he30daa8_0  
        chardet                   3.0.4                 py38_1003  
        conda                     4.8.4                    py38_0  
        [...]
        ```
        Pour vérifier la version de Python, taper :
        ```bash
        python -V
        ```
        qui doit afficher (*le dernier chiffre peut varier*) :
        ```
        Python 3.8.3
        ```

Plus d'informations (en anglais) peuvent être trouvées sur le site officiel de Miniconda ([Installation pour Windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html), [installation pour Max OS](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html), [installation pour Linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)).

## Installer un *système de gestion de versions*
Un *système de gestion de versions* (*Version Control System* ou *VCS* en anglais) est un logiciel qui conserve une trace de chaque modification importante effectuée sur un ensemble de documents.
Dans le contexte de la programmation, il sauvegarde et suit les modifications d'un ensemble de fichiers sources.

L'outil que nous allons utiliser pour cela se nomme [`git`](https://git-scm.com/).
C'est à l'heure actuelle (en 2020) le logiciel open source le plus utilisé pour cette tâche.

Continuer ???
### Création d'un compte `github`

### Copier le projet dans son espace `github` personnel

## Installer un éditeur de texte
De nombreuses applications peuvent être utilisées pour saisir un document textuel sur un ordinateur ([LibreOffice Writer](https://www.libreoffice.org/discover/writer/), [Notepad++](https://notepad-plus-plus.org/), ...).
Dans le contexte de la programmation, il est important que 
[Visual Studio Code](https://code.visualstudio.com/)

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
