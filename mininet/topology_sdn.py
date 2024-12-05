from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
import logging
from mininet.log import setLogLevel
from emuvim.dcemulator.net import DCNetwork
from emuvim.api.rest.rest_api_endpoint import RestApiEndpoint
from emuvim.api.openstack.openstack_api_endpoint import OpenstackApiEndpoint

logging.basicConfig(level=logging.INFO)
setLogLevel('info')  # set Mininet loglevel
logging.getLogger('werkzeug').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.base').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.compute').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.keystone').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.nova').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.neutron').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.heat').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.heat.parser').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.glance').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.helper').setLevel(logging.DEBUG)

def setup_topology():
    # Initialisation du réseau
    net = DCNetwork(monitor=False, enable_learning=True)

    # Création des switches
    s1 = net.addSwitch('s1')    # Switch pour Z1, Z2 & Z3
    s2 = net.addSwitch('s2')    # Switch pour GI et DC
    s3 = net.addSwitch('s3')    # Switch pour le serveur

    # Création des hôtes (Z1, Z2, Z3)
    z1 = net.addDocker('z1', ip='10.0.0.1', dimage="reoc:burst")
    z2 = net.addDocker('z2', ip='10.0.0.2', dimage="reoc:test")
    z3 = net.addDocker('z3', ip='10.0.0.3', dimage="reoc:test")
    
    # Création d'Ordon et de la passerelle GI
    ordonnanceur = net.addDocker('ordon', ip='10.0.0.100', dimage="reoc:test")
    gateway_init = net.addDocker('gi', ip='10.0.0.254', dimage="reoc:test")

    # Création d'un serveur
    serveur = net.addDocker('serveur', ip='10.0.0.200', dimage="reoc:test")

    # Connexion des hôtes au s1
    net.addLink(s1, z1)
    net.addLink(s1, z2)
    net.addLink(s1, z3)

    # Connexion de Ordonnanceur, Gateway et s1 au s2
    net.addLink(s2, s1, intfName1='s2-s1', intfName2='s1-s2')
    net.addLink(s2, ordonnanceur)
    net.addLink(s2, gateway_init)
    
    # Connexion de s2 et serveur au s3
    net.addLink(s3, s2, intfName1='s3-s2', intfName2='s2-s3')
    net.addLink(s3, serveur)

    # Lancer le réseau
    net.start()
    net.CLI()   # Lancer la CLI de Mininet pour interagir avec le réseau
    net.stop()  # Arrêter le réseau après l'utilisation

# Fonction principale pour démarrer le réseau
if __name__ == '__main__':
    setup_topology()