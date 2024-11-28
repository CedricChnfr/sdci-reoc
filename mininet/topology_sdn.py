from mininet.net import Containernet
from mininet.node import Controller, RemoteController, DockerHost
from mininet.link import TCLink

def setup_topology():
    # Initialisation du réseau
    net = Containernet(controller=RemoteController)
    
    # Ajout du contrôleur SDN (Ryu)
    controller = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    # Création des switches
    s1 = net.addSwitch('s1')  # Switch pour Z1
    s2 = net.addSwitch('s2')  # Switch pour Z2
    s3 = net.addSwitch('s3')  # Switch pour Z3
    s4 = net.addSwitch('s4')  # Switch central (Ordon vers GI)

    # Création des hôtes (Z1, Z2, Z3)
    z1 = net.addDockerHost('z1', ip='10.0.0.1', dimage="host_python")
    z2 = net.addDockerHost('z2', ip='10.0.0.2', dimage="host_python")
    z3 = net.addDockerHost('z3', ip='10.0.0.3', dimage="host_python")
    
    # Création d'Ordon et de la passerelle GI
    ordon = net.addDockerHost('ordon', ip='10.0.0.100', dimage="vnf_python")
    gi = net.addDockerHost('gi', ip='10.0.0.254', dimage="vnf_python")

    # Connexion des hôtes aux switches
    net.addLink(z1, s1, cls=TCLink)
    net.addLink(z2, s2, cls=TCLink)
    net.addLink(z3, s3, cls=TCLink)

    # Connexion des switches à Ordon et GI
    net.addLink(s1, s4, cls=TCLink)
    net.addLink(s2, s4, cls=TCLink)
    net.addLink(s3, s4, cls=TCLink)
    net.addLink(s4, ordon, cls=TCLink)
    net.addLink(ordon, gi, cls=TCLink)

    # Lancer le réseau
    net.start()
    print("Topology is running.")
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    setup_topology()
