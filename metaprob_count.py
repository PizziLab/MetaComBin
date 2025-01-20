import sys
import json
import csv

def process_files(csv_file, info_file, output_file):
    # Value to species map
    value_to_species = {}
    
    # Load the dataset file
    with open(info_file, 'r') as f:
        lines = f.readlines()
        
        for i in range(0, len(lines), 2):  # Every 4 rows, new read
            info_line = lines[i].strip()  # Info line
            parts = info_line.split('|') 
            value = parts[0][1:-1]  # If the format is ">r2.1 |"
            #value = parts[0][1:]  # If the format is "r2.1|"
            species = parts[-1].split('=')[-1]  # Species name
            
            value_to_species[value] = species
    
    # Count number for each group
    group_counts = {}
    
    with open(csv_file, 'r') as f:
        reader = f.readlines()
    
    reader = ''.join(reader)

    for row in reader.split('\n'):

        if len(row) < 1 or ',' not in row:
            continue
        value_group = row.split(',')[1]
        value = row.split('>')[1].split('|')[0] # Get value without '>'
        group = int(value_group)  # Group value as Int value
            
        if value not in value_to_species:
            continue  # Ignore not found values
            
        species = value_to_species[value]
            
        if group not in group_counts:
            group_counts[group] = {}
            
        if species not in group_counts[group]:
            group_counts[group][species] = 0
            
        group_counts[group][species] += 1  # Increase the count for that group and specie
    
    # Record the results
    with open(output_file, 'w') as f:
        for group, species_counts in sorted(group_counts.items()):
            f.write(f"Gruppo {group}:\n")
            for species, count in species_counts.items():
                f.write(f"  Specie {species}: {count} valori\n")

csv_file = sys.argv[1]
info_file = sys.argv[2]
output_file = sys.argv[3]

process_files(csv_file, info_file, output_file)

