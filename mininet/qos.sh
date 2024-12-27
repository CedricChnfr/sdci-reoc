#!/bin/bash

log() {
    log_date=$(date +"%d/%m/%y %T.%3N")
    echo -e "[$log_date]:\t$1" >> log.temp
}

create()
{
    sudo ovs-vsctl -- set port s1-eth1 qos=@qoseth1 \
    -- --id=@qoseth1 create qos type=linux-htb other-config:max-rate=1000000000 \
    queues=0=@q0 \
    -- --id=@q0 create queue other-config:min-rate=100000000 other-config:max-rate=1000000000 \

    sudo ovs-vsctl -- set port s1-eth2 qos=@qoseth2 \
    -- --id=@qoseth2 create qos type=linux-htb other-config:max-rate=1000 \
    queues=0=@q0 \
    -- --id=@q0 create queue other-config:min-rate=10 other-config:max-rate=1000 \

    # sudo ovs-vsctl -- set port s1-eth1 qos=@newqos \
    # -- --id=@newqos create qos type=linux-htb queues:0=@q0 queues:1=@q1 \
    # -- --id=@q0 create  queue  other-config:min-rate=1000000 other-config:max-rate=1000000 \
    # -- --id=@q1 create queue other-config:min-rate=1 other-config:max-rate=10 other_config:queue-size=10 \
    # > qos.temp
    
    log "Created queues"
    # curl -X POST -d @flow/z1.json http://127.0.0.1:8080/stats/flowentry/add
    # log "Assigned eth1-z1 to Queue 0"
    # curl -X POST -d @flow/z2.json http://127.0.0.1:8080/stats/flowentry/add
    # log "Assigned eth1-z2 to Queue 1"
    # curl -X POST -d @flow/z3.json http://127.0.0.1:8080/stats/flowentry/add
    # log "Assigned eth1-z3 to Queue 1"
}

remove()
{
    lines=()
    sudo ovs-vsctl clear port s1-eth1 qos
    log "Cleared port flow"

    while IFS= read -r line; do
        lines+=("$line")
    done < "qos.temp"
    sudo ovs-vsctl -- destroy qos  ${lines[0]}
    log "Removed QOS '${lines[0]}'"
    sudo ovs-vsctl -- destroy queue ${lines[1]}
    sudo ovs-vsctl -- destroy queue ${lines[2]}
    log "Removed queue '${lines[1]}'"
    log "Removed queue '${lines[2]}'"
    rm qos.temp

    curl -X DELETE http://127.0.0.1:8080/stats/flowentry/clear/1
    log "Removed flow entries"
    # sudo rm /etc/openvswitch/conf.db
    # JUST IN CASE >
}

# Check command line arguments
if [ "$1" == "create" ]; then
    create
elif [ "$1" == "remove" ]; then
    remove
else
    echo -e $RED"Usage: $0 {create|remove}"$RESET
fi

# iperf3 -c 10.0.0.254 -p 5012 -u -b 1G
# iperf3 -c 10.0.0.254 -p 5011 -u -b 1G

# iperf3 -s -p 5012
# iperf3 -s -p 5011
