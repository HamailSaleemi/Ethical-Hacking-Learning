## Network Penitration

> In this section we are going to Learn about network penetration which includes the following.
>> **pre-conection attacks**
>>>In which we will learn about the attacks which can be done while you are not connected to a network.

> **Gaining Access**
> > Then we will learn about how to get access of a network.

> **Post connection attacks**
> >how we can do alot of cool stuff once we are connected to the network.

**Note:**
> You should have a basic knowledge of Networking.
> To connect to the internet alot of devices are connected to the router.
> >your request to google is first send to router and then the router send the request to the outer world or you can say internet and get back to you to give a response.

**USB Addopter Recomended**
>1. RealTek RTL8812AU
>2. Atheros AR9271
>
> Adopter should also contain 3 modes:
> 1. Monitor mode.
> 2. Packet Injection.
> 3. AP mode.
> These are the Recomended chips for your USB adopter.
> >We need these specific adopters to to perform some tasks that a laplop's built-in adopters can not do.
 

**Getting Started with basic commands**
>ifconfig
This command is used to get all the interfaces connected you laptop.
You need to identify your wirless adoptor.
> >To identify your adopter look up for the following under the details of each interface.
> >
> >**inet** defines that ip address of your machine.
> >
> >**ether** defines the mac address of your device.

**Changing MAC Address**
> Visit folder **MAC Address** for more details.

**Change adopter mode from Managed to Monitor mode**
> Visit folder **Monitor Mode** for more details.


**Packet Sniffing**
**important note:** for packet sniffing we need our adopter to be in **Monitor Mode**
> For packet sniffing we can use **airodump-ng** to sniff packets from the adopter
> For mor details go to **Packet Sniffing** folder