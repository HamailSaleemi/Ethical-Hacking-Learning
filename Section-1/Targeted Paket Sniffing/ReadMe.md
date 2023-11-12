**Targeted Packet Sniffing**

For packet sniffing from a specific router.
You can see all the different devices connected to the router.


To start sniffing on your specific router
> Keep one thing in mind your adopter should be in **Monitor Mode** So you should run Monitor Mode file first
> ```bash
> airodump-ng --bssid <mac of adoptor> --channel <channel of adoptor> --write <file name to write> <adoptor name>
> ``` 

