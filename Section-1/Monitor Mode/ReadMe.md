**How to change adopter mode from Managed to Monitor mode**

First learn a new command
> To get your wireless adopter only
> ```bash
> iwconfig
> ``` 
First disable the adopter
> To disable Adopter
> ```bash
> ifconfig <adopter name> down
> ``` 
Now kill any internet related process
> To disable Adopter
> ```bash
> airmon-ng check kill
> ``` 

Change Mode
> To disable Adopter
> ```bash
> iwconfig <adopter name> mode <mode name>
> ```  
> ```bash
> iwconfig wlan0 mode monitor
> ```  
> 

Alternative method to change mode
> To disable Adopter
> ```bash
> airmon-ng start <adoptor name>
> ```  
> ```bash
> airmon-ng start wlan0
> ```  
 
Now start the adoptor
> To disable Adopter
> ```bash
> ifconfig <adoptor name> up
> ``` 


To ensure that mode is change use command
> To check wireless adopters
> ```bash
> iwconfig
> ``` 