import CMD_RUN

if __name__ == "__main__":
    # Replace this command with the Bash command you want to run
    newMACAddress = '00:11:22:33:44:66'
    interface = 'wlp2s0'
    interface_down = 'ifconfig {0} down'.format(interface)
    change_mac_address = 'ifconfig {0} hw ether {1}'.format(interface,newMACAddress)
    interface_up = 'ifconfig {0} up'.format(interface)
    CMD_RUN.run_bash_command(interface_down)
    CMD_RUN.run_bash_command(change_mac_address)
    CMD_RUN.run_bash_command(interface_up)
