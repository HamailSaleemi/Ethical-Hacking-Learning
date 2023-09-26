## Changing MAC address of your machine

Use the comand below

``` bash
ifconfig
```
get the name of your interface and then run

Lets say the name of my interface is **wla0**

Now to change the MAC address of your wifi interface execute following 3 commands.
1. Disable interface:
```bash
ifconfig <interface name> down
```
```bash
ifconfig wlan0 down
```
2. Change Mac Address:
```bash
ifconfig <interface name> hw ether <New MAC Address>
```
```bash
ifconfig wlan0 hw ether 00:11:22:33:44:55
```

3. Enable interface:
```bash
ifconfig <interface name> up
```
```bash
ifconfig wlan0 up
```

**Note**
> Python Code to change the MAC Address is in **changeMAC.py**