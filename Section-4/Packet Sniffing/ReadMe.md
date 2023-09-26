**Packet Sniffing**

For packet sniffing your adopter should be in monitor mode



To start sniffing on your adopter to get all the wifi connections
> To start getting singals of wifi addoptor
> ```bash
> airodump-ng <adoptor name>
> ``` 
> ```bash
> airodump-ng wlan0
> ``` 

While packet sniffing using the command above it is possible that you can not see
it is because the command above will broadcast signal on 2GHz frequency and the wifi working on frequency greater than that
like 5G will not be seen
To start sniffing on your adopter to get all the wifi connections
> To get 5G wifi use the command below
> ```bash
> airodump-ng --band a <adoptor name>
> ``` 
> ```bash
> airodump-ng --band a wlan0
> ``` 


> To get 2 & 5G wifi use the command below
> ```bash
> airodump-ng --band abg <adoptor name>
> ``` 
> ```bash
> airodump-ng --band abg wlan0
> ``` 
> It is slower than getting a single band adoptors0
