import sys
print "Please enter the number of hosts you wish to have in the network"
print "Maximum number of hosts is 256"
try:
        num_of_hosts=input()
except:
        print "Number of hosts must be an integer"
        sys.exit()
else:
        if num_of_hosts>256:
                print "Cannot simulate more than 256 nodes"
                sys.exit()
        numofhostfile=open("/home/mininet/MininetInputFile.txt","w")               #writing number of hosts into a file and making it accessible to mininet 
        numofhostfile.write(str(num_of_hosts)+"\n")
        numofhostfile.close()
        policyFile=open("/home/mininet/pox/pox/misc/FirewallPolicies.csv","w")       #making the database file and adding rules to it
        policyFile.write("id,mac_0,mac_1\n")
        print "Please enter the set of hosts between which you want to disable communication"
        print "Format:<host number 0> <host number 1>"
        print "Please type \"exit()\" if you want to stop entering rules"
        ruleNumber=0
        while(1):                                                                    #taking the rules
                rule=raw_input()
                hosts=rule.split(" ")
                if rule=="exit()":
                        break
                elif len(hosts)!=2:
                        print "Invalid rule.Not added to the database"
                else:
                        ruleNumber+=1
                        host_0=int(hosts[0])
                        host_1=int(hosts[1])
                        if host_0<0 or host_0>num_of_hosts:
                                print "Invalid Host number 0 entered"
                        elif host_1<0 or host_1>num_of_hosts:
                                print "Invalid Host number 1 entered"
                        else:
                                precedingZeroes="00:00:00:00:00:"
                                policyFile.write(str(ruleNumber)+",")             #writing contents to file
                                policyFile.write(precedingZeroes)
                                if host_0<16:
                                        policyFile.write("0")
                                policyFile.write(hex(host_0)[2:]+",")
                                policyFile.write(precedingZeroes)
                                if(host_1<16):
                                        policyFile.write("0")
                                policyFile.write(hex(host_1)[2:]+"\n")
        print "Rules entered successfully.Please feel free to run the POX controller"