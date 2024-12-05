# sdci-reoc
Software Defined Communication Infrastructure

## Topology

> Using a Docker container with only **Alpine** and **Nodejs**.
> For VIM-EMU instances on the data center we will use a specific **Xenial** instance with the help of this [requirement](https://github.com/containernet/vim-emu/wiki/Container-Requirements).

```bash
docker build . --file <filename> -t mondocker:latest
docker run -env VAR=... -i mondocker:latest
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

nodejs
vim emu
