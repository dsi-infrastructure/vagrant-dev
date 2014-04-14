
## Environnement de développement

Permettre le développement de modules d'automatisation des installations systèmes.

### Pré-requis

Veuillez installer les pré-requis suivant :

* Vagrant 1.5.2
* Oracle Virtualbox 4.3.10 (la version propriétaire)

Ce système a été testé sur les environnements Ubuntu 12.04, MacOs X Mavericks et Windows 7 avec succès.

### Utilisation

On récupère l'ensemble du projet, ainsi que les modules puppet :

```bash
git clone http://gitlab.gov.pf/dsi-infrastructure/vagrant-infrastructure.git
cd vagrant-infrastructure
git submodule init
git submodule sync
git submodule update
```

Il faut ensuite modifier le fichier 'manifests/site.pp' pour activer les modules que vous voulez mettre à jours.

Une fois la modification du fichier faites, on active les paramètres hiera dans le dossier 'hieradata'.

Il ne reste plus qu'à démarrer l'instance :

```bash
vagrant up
```

A chaques modifications d'un module, le test s'effectue via la commande suivante :

```bash
vagrant provision
```

Remarque : les modules puppets sont des projets à part entière et donc, la définition des dépôts GIT est spécifiques à chaques modules.



