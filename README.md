# sdci-reoc
Software Defined Communication Infrastructure

## Topology

> Using a Docker container with only **Alpine** and **Nodejs**.
> For VIM-EMU instances on the data center we will use a specific **Xenial** instance with the help of this [requirement](https://github.com/containernet/vim-emu/wiki/Container-Requirements).

```bash
docker build . --file <filename> -t mondocker:latest
docker run -env VAR=... -i mondocker:latest
docker exec -it <instance> bash
```

We will need to create separated containers in our topology with the following scripts:
- [`server.js`](https://homepages.laas.fr/smedjiah/tmp/mw/server.js)
- [`gateway.js`](https://homepages.laas.fr/smedjiah/tmp/mw/gateway.js)
- [`device.js`](https://homepages.laas.fr/smedjiah/tmp/mw/device.js)
- [`application.js`](https://homepages.laas.fr/smedjiah/tmp/mw/application.js)

## JS Folder

Run the following command:
```bash
npm list express
```

## Monitoring

General Controler qui fonctionne avec une API rest, qui communique avce le SDN Controller et Vim-Emu. 

```
curl http://127.0.0.1:8080/stats/port/1
```

Menu contoller: 
    1/ provoquer incident (API Docker) (lancer un second device par ex.)
    2/ Démarrer monitoring (API Ryu) (tx_bytes, port_no=4)
    3/ arrêter le monintoring
    4/ Activer Ordonnanceur (API VIM-EMU pour lancer la VNF, Ryu pour les redirections)
    5/ Désactiver
    6/ Mode Auto (démarre monitoring -> vérifie si un seuil est dépassé : active l'use case)

Il existe plusieurs commande dans `containernet` pour observer la topologie:
```
links
sh ovs-vsctl show
sh ovs-vsctl get Bridge s1 datapath_id
```

Nous en avons déduit que chaque port était associé au suivant: 
- 3 (port 1): Z1
- 4 (port 2): Z2
- 5 (port 3): Z3

nodejs
vim emu
