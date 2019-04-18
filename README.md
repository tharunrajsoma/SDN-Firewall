# SDN-Firewall
SDN based firewall to block malicious hosts and links using Mininet network emulator

## SDN
-	SDN is a new approach in designing, building, and managing networks that separates the network’s control and forwarding planes to better optimize each.
-	SDN method centralizes control of the network by separating the control logic to become completely programmable.
## SDN Controller
-	SDN controller offer a centralized view of the overall network and enable network administrators to mention to the underlying systems (like switches and routers) how the forwarding plane should handle network traffic.
## SDN as a firewall
- SDN evolved from the concept of decoupling the lower-layer packet/frame forwarding from the control function that dynamically, intelligently determines how application traffic should be transported.
- The separation of the control plane from the forwarding plane allows networks to facilitate packet processing in new and innovative ways which makes it as a firewall where in control plane code can be written to block specific packets or hosts.
## Packet forwarding Procedure
- All the flows within a network switch are placed by a running controller and packet forwarding is done based on the rules in the controller.
- If a flow is not present (table-miss), then the switch calls the controller to ask for help determining how the packet should be forwarded.

## Pox Controller
- POX is an open source development platform for creating a python based software-defined networking (SDN) control applications, such as SDN controllers.
- POX which enables rapid development and prototyping is used for most of the present SDN projects.
- We wrote a python code to run on the pox controller to block few hosts and allow some other hosts to ping based on the input given by the user.
## Mininet as Virtual Network
- Mininet creates a realistic virtual network, running real kernel, switch and application code, on a single machine.
## Mininet Commands
> sudo mn --topo=single,3 --controller=none --mac


The above command does below things:
1. --topo: To create a topology of one switch and three hosts 
2. --contoller: Here we made controller to be equal to be none so that mininet doesn`t use it`s own default controller.
3. --mac: This command to read mac addresses. <br />
<br />

> net

Above command shows the switches, hosts, links and controller present.<br />
<br />

> dump

Above command depicts the exact topology. Gives below details.
1. Controller ip, pid, port number are present.
2. Hosts and switches links and pid numbers are shown.

### Customizing the topology

To add a host:
> py net.addHost('h4')

<br />

To get a link between the switch “s1” and host h4:
> py net.addLink(s1,net.get('h4'))

<br />

To show the mappings b/w ports
> sh ovs-ofctl show s1	

## Description of firewall python code
-	On running “GeneratePolicy.py” the rules from the .csv file (need to be given by the user) are read and stored in a list.
-	Next, the set of rules is sent in the form of a message to the controller 
-	The controller receives the message and acts accordingly
## Description of topology file:
- Customized (Bus type) topology is created by taking the input form the user about the number of hosts to be created based on this each switch is connected to each host and links are provided to it.
- This can be done in Mininet virtual netwrok environment by using the commands mentioned above about a host creation and connecting to a link.

