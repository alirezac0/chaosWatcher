import requests
import json
import sys

chaos_DB = 'https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/main/chaos-bugbounty-list.json'

response = requests.get(chaos_DB)
current_json = json.loads(response.text)
current_programs = current_json["programs"]

# Load the previous JSON file from a local file if it exists
try:
    with open('chaos-bugbounty-list.json', 'r') as f:
        previous_json = json.load(f)
        previous_programs = previous_json["programs"]
except FileNotFoundError:
    print("chaos-bugbounty-list.json file not found.\n")
    print("Saving the file from repo ...\n")
    with open('chaos-bugbounty-list.json', 'w') as f:
        json.dump(current_json, f)
    print("See you soon!")
    sys.exit(0)


# Compare the two JSON objects and print the differences

new_programs = [program for program in current_programs if program not in previous_programs]

previous_programs_names = [program['name'] for program in previous_programs]

new_programs_names = [program['name'] for program in current_programs]


# Find Removed Programs
for program in previous_programs:
    if program['name'] not in new_programs_names:
        print(program)

changed_programs = []

# Find New programs
for program in current_programs:
    if program in new_programs:
        if program['name'] in previous_programs_names:
            # Check key values
            changed_programs.append(program)
        else:
            # New program
            print("New program:\n")
            print(f"Name: {program['name']}")
            print(f"URL: {program['url']}")
            print(f"Offers Bounty?: {program['bounty']}")
            print(f"domains: {program['domains']}")

# Find Changed Programs
for changed_program in changed_programs:
    for previous_program in previous_programs:
        if changed_program['name'] == previous_program['name']:
            print(f"Changes has been made to {changed_program['name']} program:")
            if changed_program['bounty'] != previous_program['bounty']:
                print(f"Program bounty has been changed to {changed_program['bounty']}")
            if changed_program['url'] != previous_program['url']:
                print(f"Program URL has been changed to {changed_program['bounty']}")
            if slice(changed_program['domains']) != slice(previous_program['domains']):
                if slice(changed_program['domains']) - slice(previous_program['domains']):
                    print("New domain/domains has been added to the program:")
                    print(slice(changed_program['domains']) - slice(previous_program['domains']))
                if slice(previous_program['domains']) - slice(changed_program['domains']):
                    print("Old domain/domains has been removed from the program")
                    print(slice(previous_program['domains']) - slice(changed_program['domains']))


# Save the current JSON file for the next comparison
with open('chaos-bugbounty-list.json', 'w') as f:
    json.dump(current_json, f)
    print("Database Updated!")

