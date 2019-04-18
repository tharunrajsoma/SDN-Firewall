from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
import os                                       #for including the home environment variable
import csv

log = core.getLogger()
policy_database = "%s/pox/pox/misc/FirewallPolicies.csv" %os.environ['HOME']        #table which serves as a database by storing the rules

class Firewall (EventMixin):
    
    def __init__ (self):
            self.listenTo(core.openflow)                    #listening for connection from mininet
            log.debug("Enabling Firewall Module")               #debugging data
            self.deny = []                          #list into which the rules are loaded
            filePointer=open(policy_database, 'rb')
                reader = csv.DictReader(filePointer)                            #reading the csv file in table format
                for row in reader:
                    self.deny.append((EthAddr(row['mac_0']), EthAddr(row['mac_1']))) #adding the rule to the list
                    self.deny.append((EthAddr(row['mac_1']), EthAddr(row['mac_0'])))

    def _handle_ConnectionUp (self, event):    #function that runs the firewall
            for (src, dst) in self.deny:
                    match = of.ofp_match()
                    match.dl_src = src
                    match.dl_dst = dst
                    msg = of.ofp_flow_mod()
                    msg.match = match
                    event.connection.send(msg)
            log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():       #starting the firewall
    core.registerNew(Firewall)
