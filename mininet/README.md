# Comment tester la topologie SDN

## Connexion

### Construire les images Docker

Pour construire les images Docker nécessaires, exécutez le script `create.sh` :
```sh
./create.sh
```

### Lancer la topologie

Pour lancer la topologie, exécutez le script `topology_sdn.py` avec les privilèges sudo :
```sh
sudo python3 mininet/topology_sdn.py
```

## Tester la topologie

Pour tester la connectivité entre les différents hôtes de votre topologie, utilisez les commandes `ping` suivantes :

### Tester la connectivité de z1 vers les autres hôtes :
```sh
containernet> z1 ping -c 1 z2  # ping z2
containernet> z1 ping -c 1 z3  # ping z3
containernet> z1 ping -c 1 scheduler  # ping scheduler
containernet> z1 ping -c 1 gi  # ping gi
containernet> z1 ping -c 1 server  # ping server
```

### Tester la connectivité de z2 vers les autres hôtes :
```sh
containernet> z2 ping -c 1 z1  # ping z1
containernet> z2 ping -c 1 z3  # ping z3
containernet> z2 ping -c 1 scheduler  # ping scheduler
containernet> z2 ping -c 1 gi  # ping gi
containernet> z2 ping -c 1 server  # ping server
```

### Tester la connectivité de z3 vers les autres hôtes :
```sh
containernet> z3 ping -c 1 z1  # ping z1
containernet> z3 ping -c 1 z2  # ping z2
containernet> z3 ping -c 1 scheduler  # ping scheduler
containernet> z3 ping -c 1 gi  # ping gi
containernet> z3 ping -c 1 server  # ping server
```

### Tester la connectivité de ordon (scheduler) vers les autres hôtes :
```sh
containernet> ordon ping -c 1 z1  # ping z1
containernet> ordon ping -c 1 z2  # ping z2
containernet> ordon ping -c 1 z3  # ping z3
containernet> ordon ping -c 1 gi  # ping gi
containernet> ordon ping -c 1 server  # ping server
```

### Tester la connectivité de gi (gateway_init) vers les autres hôtes :
```sh
containernet> gi ping -c 1 z1  # ping z1
containernet> gi ping -c 1 z2  # ping z2
containernet> gi ping -c 1 z3  # ping z3
containernet> gi ping -c 1 scheduler  # ping scheduler
containernet> gi ping -c 1 server  # ping server
```

### Tester la connectivité de server vers les autres hôtes :
```sh
containernet> server ping -c 1 z1  # ping z1
containernet> server ping -c 1 z2  # ping z2
containernet> server ping -c 1 z3  # ping z3
containernet> server ping -c 1 scheduler  # ping scheduler
containernet> server ping -c 1 gi  # ping gi
```

Ces commandes permettent de vérifier la connectivité entre tous les hôtes de la topologie.

## Monitoring

Le but du monitoring est de surveiller les performances et l'état des ports réseau en temps réel. Cela permet de détecter et de diagnostiquer les problèmes de réseau, d'optimiser les performances et de garantir la fiabilité du système.

### Objectifs du Monitoring

1. **Surveillance des Performances** :
    - Collecter des statistiques sur les paquets reçus et envoyés (`rx_packets`, `tx_packets`).
    - Mesurer le volume de données transférées (`rx_bytes`, `tx_bytes`).

2. **Détection des Problèmes** :
    - Identifier les paquets perdus ou abandonnés (`rx_dropped`, `tx_dropped`).
    - Détecter les erreurs de transmission et de réception (`rx_errors`, `tx_errors`).

3. **Optimisation du Réseau** :
    - Analyser les statistiques pour optimiser les configurations réseau.
    - Prendre des décisions basées sur les données collectées pour améliorer les performances.

### Utilisation du Monitoring

Pour tester l'API de monitoring, suivez les étapes ci-dessous :

1. **Lancer le script `sdci.py`** :
    - Ouvrez l'interface du contrôleur SDCI en exécutant la commande suivante :
      ```sh
      sudo python3 sdci.py
      ```

    - En sélectionnant 'Monitoring', une requête GET est envoyée à l'API pour récupérer les statistiques du port sélectionné.

### Exemple de Réponse JSON

Voici un exemple de réponse JSON que vous pouvez obtenir en utilisant la commande `curl` :

```json
{
  "1": [
     {
        "rx_packets": 29,
        "tx_packets": 17,
        "rx_bytes": 2166,
        "tx_bytes": 1258,
        "rx_dropped": 0,
        "tx_dropped": 0,
        "rx_errors": 0,
        "tx_errors": 0,
        "rx_frame_err": 0,
        "rx_over_err": 0,
        "rx_crc_err": 0,
        "collisions": 0,
        "duration_sec": 9239,
        "duration_nsec": 583000000,
        "port_no": 4
     },
     ...
  ]
}
```

Chaque catégorie dans la réponse JSON correspond à une métrique spécifique pour le port réseau, fournissant des informations détaillées sur les performances et l'état du port.