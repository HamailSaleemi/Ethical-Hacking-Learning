# Handshake Cracking
1. you need to create a list of words
2. give the list to handshake

## Creating a Wordlist
**Crunch** can be used to create the list of words
```bash
crunch [min] [max] [characters] -t [pattern] -o filename 
```
```bash
crunch 6 8 123abc$ -t a@@@@b -o wordlist 
```
Once you have created the wordlist using the command 

you can use this command to check if the password exists in your wordlist
```bash
aircrack-ng wpa_handshake.cap -w wordlist.txt 
```
Note: wpa_handshake.cap where we have our handshake. 
