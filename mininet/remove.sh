docker rm mn.serveur --force
docker rm mn.gi --force
docker rm mn.ordon --force
docker rm mn.z3 --force
docker rm mn.z2 --force
docker rm mn.z1 --force
sudo mn -c
sudo ip link delete s1-s2
sudo ip link delete s2-s1
sudo ip link delete s2-s3
sudo ip link delete s3-s2