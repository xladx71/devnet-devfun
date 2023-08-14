#Meraki module from GitHub

import meraki

import csv
import os
import time

api_key = os.environ['MERAKI_DASHBOARD_API_KEY']


dashboard = meraki.DashboardAPI(api_key)


# CSV with serial numbers and port info
# Update with CSV for store/switch
with open('', 'r') as csvfile:
    #skip first row headers
    next(csvfile)
    #counter for current row in file
    counter = 1
    switch = csv.reader(csvfile)

    for serial, port, name, type, vlan, allowed_vlans, PoE_enabled in switch:
        counter = counter + 1

        if serial == "":
            print("Error: No serial number defined for row"  +  str(counter))
            quit()
        elif port == "":
            print("Error: No port defined for row"  +  str(counter))
            quit()
        my_serial = serial
        my_port = port
        my_name = name
        my_type = type
        my_vlan = vlan
        my_poe_enabled = bool(PoE_enabled)
        my_allowed_vlans = allowed_vlans


        # Will add the same tag to all ports, if not needed leave quotes
        my_tag = ''
        split_tag = my_tag.split(",")

        if vlan == '':
            response = dashboard.switch.updateDeviceSwitchPort(my_serial, my_port, name=my_name, tags=split_tag, enabled=True, type=my_type, poeEnabled=my_poe_enabled, allowedVlans= my_allowed_vlans)
        else:
            response = dashboard.switch.updateDeviceSwitchPort(my_serial, my_port, name=my_name, tags=split_tag, enabled=True, type=my_type, vlan=my_vlan, poeEnabled=my_poe_enabled, allowedVlans= my_allowed_vlans)
        # Sleep for ~300ms to avoid rate-limit
        print(response)
        time.sleep(0.3)
