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
    * pour Windows, double-cliquer sur le fichier `.exe` téléchargé précédemment puis accepter les choix par défaut **sauf à la dernière étape** :
      - accepter la licence ("I Agree")
      - "Install for", "Just Me (recommended)" ("Next")
      - "Choose Install Location", ("Next")
      - "Register Miniconda3 as my default Python 3.8", ("Install")
      - "Installation Complete", ("Next")
      - "Completing Miniconda3...", **décocher tout** ("Finish")
    * pour Mac OS, double-cliquer sur le fichier `.pkg` téléchargé précédemment puis accepter les choix par défaut
    <!-- TODO : détailler la procédure pour Mac OS -->
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
> Un "projet" sous `git` et `github` se nomme un *dépôt* (*repository* en anglais).
> Attention car la notion de projet (*project*) sous `github` est différente.

Le dépôt `git` contenant l'ensemble du projet n'est pas modifiable par tout le monde.
Pour pouvoir faire des changements dessus, il faut donc d'abord le *copier* dans votre espace personnel.
Sous `github`, cette opétation se nomme un **fork** et est utilisée pour copier un dépôt entre deux espaces utilisateurs.

La procédure pour cela est la suivante :
1. se rendre sur la page `github` du dépôt à copier (https://github.com/uvsq-info/l1-python dans notre cas),
1. cliquer sur le bouton *Fork* en haut à droite de l'écran
1. sélectionner votre espace personnel comme destination du fork

Vous disposez maintenant d'une copie personnelle du dépôt avec une URL qui devrait ressembler à https://github.com/uvsqXXXXXXXX/l1-python.

### Installer `git`
L'étape suivante consiste à récupérer une copie locale du projet.
Nous utiliserons pour cela l'interface `git` intégrée à l'éditeur de texte.
Cependant, cette dernière s'appuie sur l'outil en ligne de commande `git` que nous allons installer maintenant.

#### Sous Windows
1. Télécharger [git sous Windows](https://git-scm.com/download/win)
1. Double-cliquer sur le fichier téléchargé pour lancer l'installation
1. Conserver les choix par défaut proposés lors de l'installation **sauf pour les étapes en gras ci-dessous** :
    - accepter la licence ("Next")
    - "Select Destination Location", ("Next")
    - "Select Components", ("Next")
    - "Select Start Menu Folder", ("Next")
    - "Choosing the default editor used by Git", **choisir "Use Visual Studio Code as Git's default editor"** ("Next")
    - "Adjusting your PATH environment", déjà sélectionné "Git from the command line and also from 3rd-party software" ("Next")
    - "Choosing the SSH executable", déjà sélectionné "Use OpenSSH" ("Next")
    - "Choosing HTTPS transport backend", déjà sélectionné "Use the OpenSSL library" ("Next")
    - "Configuring the line ending conversions", déjà sélectionné "Checkout Windows-style, commit Unix-style line endings" ("Next")
    - "Configuring the terminal emulator to use with Git Bash", déjà sélectionné "Use MinTTY (the default terminal of MSYS2)" ("Next")
    - "Choose the default behavior of 'git pull'", déjà sélectionné "Default (fast-forward or merge)" ("Next")
    - "Choose a credentiel helper", **choisir "None"**("Next")
    - "Configuring extra options", déjà sélectionné "Enable file system caching" et "Enable symbolic links" ("Next")
    - "Configuring experimental options", rien n'est sélectionné ("Install")
    - "Completing the Git Setup Wizard", **décocher tout** ("Next")

#### Sous Mac OS
<!-- TODO : détailler la procédure pour Mac OS -->

#### Sous Linux
L'installation de `git` est très simple mais dépend de la distribution Linux installée.
Par exemple, avec une distribution `debian`, il suffit de taper dans un terminal :
```bash
sudo apt update
sudo apt install git
```

Pour trouver la commande correspondant à votre système, rendez-vous sur la page [Download for Linux and Unix](https://git-scm.com/download/linux) et choisissez les commandes adéquates.

### Finaliser et vérifier l'installation
1. Sous Windows, ouvrir un *Git Bash*; sous Mac OS et Linux, ouvrir un terminal et taper :
    ```bash
    git --version
    ```
    qui devrait afficher (les deux derniers numéros peuvent être différents) :
    ```bash
    git version 2.27.0
    ```
1. Dans le même terminal, taper (**en substituant votre prénom et votre nom**) :
    ```bash
    git config --global user.name "Prénom NOM"
    git config --global user.email "prenom.nom@ens.uvsq.fr"
    git config --global color.ui auto
    ```
1. Fermer le terminal

## Installer un éditeur de texte
De nombreuses applications peuvent être utilisées pour saisir un document textuel sur un ordinateur ([LibreOffice Writer](https://www.libreoffice.org/discover/writer/), [Notepad++](https://notepad-plus-plus.org/), ...).
Dans le contexte de la programmation, il est important que le texte du programme ne soit pas modifié par des informations de mise en forme comme le ferait un logiciel de *traitement de texte* comme LibreOffice Writer.

Il faut donc choisir un logiciel dans la catégorie des [éditeurs de texte](https://fr.wikipedia.org/wiki/%C3%89diteur_de_texte) ou des [environnement de développement intégré](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement) (*integrated development environment* ou *IDE* en anglais).
Les différents outils de ce type varient beaucoup en terme de fonctionnalités et de complexité d'usage.

Nous avons choisi le logiciel [Visual Studio Code](https://code.visualstudio.com/).
Il est un bon compromis entre fonctionnalités et complexité tout en étant disponible pour les principales architectures et systèmes d'exploitation.

### Installer Visual Studio Code
1. Télécharger la version de [Visual Studio Code](https://code.visualstudio.com/) adapté à votre système
1. Lancer l'installation du programme à partir du fichier téléchargé ([pour Windows](https://code.visualstudio.com/docs/setup/windows), [pour Mac OS](https://code.visualstudio.com/docs/setup/mac), [pour Linux](https://code.visualstudio.com/docs/setup/linux))

Nous ne détaillons pas ici la procédure d'installation car elle ne présente pas de difficulté majeure.

## Récupérer et initialiser le projet localement
### Création d'une copie locale du projet
Récupérer localement le projet `github`
- clonage du dépôt avec VSCode
    - lancer VSCode
    - cliquer sur l'icone en forme de graphe à 3 noeuds à gauche de l'écran (Source Control ou Ctrl+Shift+G)
    - cliquer sur le bouton "Clone Repository" à gauche de l'écran
    - sélectionner "Clone from Github", cliquez sur "Allow" dans la boite de dialogue puis accepter les différents choix proposés dans le navigateur ou dans une boite de dialogue
    - sélectionner le dépôt "uvsqXXXXXXXX/l1-python" puis choisissez l'emplacement local du projet
    - ouvrir ensuite le répertoire créé ci-dessus


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

## Références
### Python
* [Site officiel](https://www.python.org/)
* [Documentation](https://docs.python.org/fr/3/) en français
* [Carte de référence](https://perso.limsi.fr/pointal/python:abrege), ensemble de [liens](https://perso.limsi.fr/pointal/liens:python_links), L. Pointal
* [Cours de Python](https://python.sdv.univ-paris-diderot.fr/), Patrick Fuchs et Pierre Poulain

### Git
* [Site officiel](https://git-scm.com/)
* [Documentation](https://git-scm.com/doc)
* Carte de référence (en français) ([web](https://training.github.com/downloads/fr/github-git-cheat-sheet/), [pdf](https://training.github.com/downloads/fr/github-git-cheat-sheet.pdf))
* Le livre [Pro Git](https://git-scm.com/book/fr/v2) (*Scott Chacon et Ben Straub, Apress*) en français

### Visual Studio Code
* [Site officiel](https://code.visualstudio.com/)
* [Documentation](https://code.visualstudio.com/docs) (en anglais)
* [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
* Extension [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) ([tutoriel](https://code.visualstudio.com/docs/python/python-tutorial))
