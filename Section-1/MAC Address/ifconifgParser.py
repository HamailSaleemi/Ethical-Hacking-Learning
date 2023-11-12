import CMD_RUN

def get_interface_obj_list(raw_array):
    def filter(interface_object):
        for key in interface_object.keys():
            index = 0
            popIndex = []
            for ele in interface_object[key]:
                index += 1
                if ele.startswith('inet'):
                    interface_object[key]['data']['IP address info'] = ele
                    popIndex.append(index)
            for ind in popIndex:
                interface_object[key].pop(ind)
    interface_obj = {}
    currentInterface = 0
    for ele in raw_array:
        if 'interface:{0}'.format(str(currentInterface)) not in interface_obj.keys():
            interface_obj['interface:{0}'.format(str(currentInterface))] = []
        if ele != '':
            interface_obj['interface:{0}'.format(str(currentInterface))].append(ele)
        else:
            currentInterface += 1
    currentInterfaces = list(interface_obj.keys())
    for ele in currentInterfaces:
        data = interface_obj[ele][0].split(':')
        interface_obj[ele][0] = data[1]
        interface_obj[data[0]] = interface_obj[ele]
        del interface_obj[ele]
    # Clean the data a little
    for key in interface_obj.keys():
        for i in range(len(interface_obj[key])):
            interface_obj[key][i] = ' '.join(interface_obj[key][i].split())
        temp = interface_obj[key]
        interface_obj[key] = {}
        interface_obj[key]['raw data'] = temp
    filter(interface_obj)
    return interface_obj

if __name__ == "__main__":
    # get interface information
    ifconfig_cmd = 'ifconfig'
    interface_raw = CMD_RUN.run_bash_command(ifconfig_cmd)
    interface_raw_arr = interface_raw.splitlines()
    del ifconfig_cmd
    interface_raw_obj = get_interface_obj_list(interface_raw_arr)
    del interface_raw_arr

    for interface in interface_raw_obj:
        print("Interface {0}".format(interface))
        print("Raw Data is",interface_raw_obj[interface]['raw data'])