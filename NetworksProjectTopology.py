#Simple Bus Type Topology

from mininet.topo import Topo
import sys
class MyTopo( Topo ):

    def __init__( self ):
        Topo.__init__( self )
    self.hostArray = []                               #list that stores the names of hosts
    self.switchArray = []                             #list that stores the names of switches 
    self.hostArray.append('')
    self.switchArray.append('')                       #empty for h0 since we are taking from 1
    self.num_of_hosts=-1
    try:
        input_file=open("/home/mininet/MininetInputFile.txt","r")   #this file contains number of hosts 
        self.num_of_hosts=int(input_file.readline())
    except:
        print "Please make sure that you run GeneratePolicy.py before starting Mininet"  #First policy file must be generated 
        sys.exit()
    if self.num_of_hosts==0:
        print "Number of hosts must be a positive integer" 
        sys.exit()
    for i in range(self.num_of_hosts):
        self.hostArray.append(self.addHost('h'+str(i+1)))                                #adding hosts
        self.switchArray.append(self.addSwitch('s'+str(i+1)))                            #adding switches
    for j in range(self.num_of_hosts-1):  
        self.addLink( self.switchArray[j+1],self.hostArray[j+1] )                        #adding links
        self.addLink( self.switchArray[j+1], self.switchArray[j+2] ) 
    self.addLink( self.switchArray[self.num_of_hosts],self.hostArray[self.num_of_hosts] )
topos = { 'mytopo': ( lambda: MyTopo() ) }