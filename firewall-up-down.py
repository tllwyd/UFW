import subprocess

# This script will bring the ufw firewall up and block all commmunication unless IP addresses are added to the allow list (see allow list script)

# Displays the UFW rules to the user
subprocess.run(['sudo', 'ufw', 'status', 'numbered'])

firewall_status = input("Do you want to bring the firewall up or down?: ").lower()

# check if the user want to bring the firewall up or down
if firewall_status == "up":
    # Ask the user to enter the ufw rule number where they want to add the block rule
    # Note, this rule should always be placed about the v4 port 53 rules
    print("To bring the firewall up, you need to insert the DENY rule above the port 53 rules by selecting the top port 53 rule.")
    print("This will insert the rule above it and push the port 53 rule down.")
    
    rule_number = input("Enter the ufw rule number of the top port 53 rules to bring the firewall up: ")

    # Make sure the user entered valid whole number
    try:
        rule_number = int(rule_number)
        # Add the DENY rule to the user input specific rule 
        subprocess.run(['sudo','ufw','insert',str(rule_number),'deny','in','from','any','to','any'])

    # If the user did not enter a valid whole number
    except ValueError:
        print("Please enter a valid WHOLE number")
        sys.exit(1)

# If the user wants to bring the firewall down
elif firewall_status == "down":
    # Ask the user to enter the ufw rule number where they want to delete 
    # Note, this rule should always be placed about the v4 port 53 rules and a DENY from all rule
    print("To bring the firewall down, you must delete the DENY from all rule typically above the IPv4 port 53 rules...")
    rule_number = input("Enter the ufw rule number you want to delete: ")

    # Make sure the user entered valid whole number
    try:
        rule_number = int(rule_number)
        # Delete the user defined rule
        subprocess.run(['sudo','ufw','delete',str(rule_number)])

    # If the user did not enter a valid whole number
    except ValueError:
        print("Please enter a valid WHOLE number")
        sys.exit(1)

else:
    print("Please enter up or down")

# Displays the UFW rules to the user
subprocess.run(['sudo', 'ufw', 'status', 'numbered'])






