# Post Connection Attack


## 1. Gather information for all devices connected to the network.
``` bash
netdiscover -r 10.0.2.1/24
```
Here 10.0.2 is the constant address of network.

### Using ZenMap for information gathering.
You can simply install zenmap on your linux

and in *Target* field you can enter the range on which you want to make *scans*.

you can select type of scan from the *Profile* and gather information from there.
