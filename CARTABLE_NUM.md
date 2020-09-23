# Environnement de TP avec le cartable numérique

La machine virtuelle à utiliser une fois l'ordinateur du cartable numérique démarré est `debian`. C'est une machine virtuelle Linux.


### Prérequis
On suppose que vous disposez d'un compte `github` avec le projet copié dedans. 
Si tel n'est pas le cas, il faut faire les étapes "Création d'un compte `github`" et "Copier le projet dans son espace `github` personnel" du document [INSTALL.md](INSTALL.md).



### Installation de VSCode
Essayez de démarrer VSCode. Il est possible qu'il ne soit pas encore installé sur les ordinateurs du cartable numérique pour le premier TD. Si c'est le cas, il faut:
1. ouvrir un terminal
1. taper:
    ```bash
        wget https://go.microsoft.com/fwlink/?LinkID=760868 -O vscode.deb
        sudo dpkg -i vscode.deb && rm vscode.deb
        code --install-extension ms-python.python 
    ```
1. puis fermer le terminal.


### Création d'une copie locale du projet
1. Lancer VSCode
1. Cliquer sur l'icone en forme de graphe à 3 noeuds à gauche de l'écran (*Source Control* ou *Ctrl+Shift+G*)
1. Cliquer sur le bouton "Clone Repository" à gauche de l'écran ou *Ctrl+Shift+P* puis sélectionner "Git: Clone"
1. Sélectionner "Clone from Github", cliquez sur "Allow" dans la boite de dialogue puis accepter les différents choix proposés dans le navigateur ou dans une boite de dialogue VSCode
1. Sélectionner le dépôt "uvsqXXXXXXXX/l1-python" dans la liste déroulante puis choisissez l'emplacement local du projet
1. Ouvrir ensuite le répertoire créé ci-dessus



### Utiliser le projet
Pour utiliser le projet, consulter le [README.md](README.md) du projet.