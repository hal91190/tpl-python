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

L'outil `git` gérera votre projet localement sur une machine mais il est très utile de faire héberger son projet sur le web.
C'est ce que propose la plateforme [github](https://github.com/).
Ce service offre la possibilité de sauvegarder son projet dans le cloud afin de pouvoir le récupérer de n'importe quelle machine connectée.

### Création d'un compte `github`
À l'adresse https://github.com/join, créer un compte en précisant :
* le nom d'utilisateur (*username*) `uvsqXXXXXXXX` en remplaçant `XXXXXXXX` par votre numéro d'étudiant,
* l'adresse mail (*Email address*) `prenom.nom@ens.uvsq.fr`,
* et un mot de passe (*Password*).

Il faut ensuite consulter les mails à cette adresse pour confirmer l'adresse d'inscription.

### Copier le projet dans son espace `github` personnel
Le dépôt git contenant l'ensemble du projet n'est pas modifiable par tout le monde.
Pour pouvoir faire des changements dessus, il faut donc d'abord le *copier* dans votre espace personnel.
Sous github, cette opétation se nomme un **fork** et est utilisé pour copier un dépôt entre deux espaces utilisateurs.

La procédure pour cela est la suivante :
1. se rendre sur la page du dépôt git à copier (https://github.com/hal91190/tpl-python dans notre cas),
1. cliquer sur le bouton *Fork* en haut à droite de l'écran
1. sélectionner votre espace personnel comme destination du fork

Vous disposez maintenant d'une copie personnelle du dépôt avec une URL qui devrait ressembler à https://github.com/uvsqXXXXXXXX/tpl-python.

### Installer `git`
L'étape suivante consiste à récupérer une copie locale du projet.
Nous utiliserons pour cela l'interface `git` intégrée à l'éditeur de texte mais cette dernière s'appuie sur l'outil en ligne de commande `git` que nous allons installer maintenant.

#### Sous Windows
1. Télécharger [git sous Windows](https://git-scm.com/download/win)
1. Double-cliquer sur le fichier téléchargé pour lancer l'installation
3. Conserver les choix par défaut proposés lors de l'installation

#### Sous Mac OS

#### Sous Linux
L'installation de `git` est très simple mais dépend de la distribution Linux installée.
Par exemple, avec une distribution `debian`, il suffit de taper dans un terminal :
```bash
sudo apt update
sudo apt install git
```

Pour trouver la commande correspondant à votre système, rendez-vous sur la page [Download for Linux and Unix](https://git-scm.com/download/linux) et choisissez les commandes adéquates.

## Installer un éditeur de texte
De nombreuses applications peuvent être utilisées pour saisir un document textuel sur un ordinateur ([LibreOffice Writer](https://www.libreoffice.org/discover/writer/), [Notepad++](https://notepad-plus-plus.org/), ...).
Dans le contexte de la programmation, il est important que 
[Visual Studio Code](https://code.visualstudio.com/)

* Un IDE
  * par exemple, [Visual Studio Code](https://code.visualstudio.com/) avec l'extension [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) ([tutoriel](https://code.visualstudio.com/docs/python/python-tutorial))

## Récupérer et initialiser le projet localement
### Création d'une copie locale du projet
Récupérer localement le projet `github`
- clonage du dépôt avec VSCode
  VSCode supporte github en utilisant le login de l'utilisateur github => clonage très simple

- ouverture du README => installation de l'extension Markdown pour la prévisualisation

- ouverture de hello.py => installation de l'extension MS Python

- dans VSCode
  choisir l'interpréteur "Python 3.8.X XX-bit ('envpython': conda)" (Ctrl+Shift+P, "Python: Select Environment" ou click en bas à gauche)
  choisir le shell par défaut "Command Prompt" (Ctrl+Shift+P, "Terminal: Select Default Shell")

  exécuter hello.py -> OK
  exécuter fizzbuzz.py et test_fizzbuzz.py -> OK
  exécuter explot.py -> OK
  exécuter exjupyter.ipnb -> OK après sélection de l'interpréteur en haut à droite
  exécuter gui/exemple0X.py -> OK

### Création et activation de l'environnement
* Avec la distribution [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)
  ```bash
  conda env create
  conda activate envpython
  ```
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
