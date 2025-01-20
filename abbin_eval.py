import json
import sys

# Verify that input and output files are present   
if len(sys.argv) != 4:
    print("Usage: python program_name.py cluster_reads.json specie_reads.json output_file.txt")
    sys.exit(1)

cluster_file = sys.argv[1]
specie_file = sys.argv[2]
output_file = sys.argv[3]

# Load 1st json file (cluster with reads)
with open(cluster_file, 'r') as file:
    cluster_reads = json.load(file)

# Load 2nd json file (truth file)
with open(specie_file, 'r') as file:
    specie_reads = json.load(file)

# function count_species counts every occurrence of a specie inside every cluster separately, dividing paired and unpaired reads
def count_species(group_dict, species_dict, outputfile):
    results = {'0': {}, '1': {}}
    unique_count = {'0': {}, '1': {}}
    value_to_species = {}
    for species, values in species_dict.items():
        for value in values:
            value_to_species[value] = species

    for group, values in group_dict.items():
        seen = {}

        for value in values:
            if value not in seen:
                seen[value] = 1
            else:
                seen[value] +=1

        for value, count in seen.items():
            
            if value in value_to_species:
                species = value_to_species[value]
                if species not in results[group]:
                    results[group][species] = 0
                results[group][species] += count

            if count == 1:
                if species not in unique_count[group]:
                    unique_count[group][species] = 0
                unique_count[group][species] +=1
                  
    with open(outputfile, 'w') as f:
        for group in results:
            f.write(f"Gruppo {group}: \n")
            for species in sorted(results[group]):
                total_count = results[group][species]
                unique_counts = unique_count[group].get(species, 0)
                f.write(f"Specie {species}: {total_count} valori (unici: {unique_counts})\n")

# Calling the function
count_species(cluster_reads, specie_reads, output_file)