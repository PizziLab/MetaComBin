import json
import sys

# Verify correct arguments
if len(sys.argv) != 4:
    print("Usage: python program_name.py cluster1.log.1 cluster2.log.2 output_file.json")
    sys.exit(1)

cluster_file1 = sys.argv[1]
cluster_file2 = sys.argv[2]
output_file = sys.argv[3]

# Load 1st file
with open(cluster_file1, 'r') as file:
    cluster_reads1 = file.readlines()
cluster_reads1 = ''.join(cluster_reads1)

# Load 2nd file
with open(cluster_file2, 'r') as file:
    cluster_reads2 = file.readlines()
cluster_reads2 = ''.join(cluster_reads2)

# function to create dictionary with clusters and reads
def assegnazione_reads_cluster(cluster1, cluster2):
    cluster_dict = {}
    cl1 = cluster1.split('\n')
    cl2 = cluster2.split('\n')
    for read1 in cl1:
        if 0 not in cluster_dict:
            cluster_dict[0] = []
        cluster_dict[0].append(read1.split('.')[0])

    for read2 in cl2:
        if 1 not in cluster_dict:
            cluster_dict[1] = []
        cluster_dict[1].append(read2.split('.')[0])
    return cluster_dict

cluster_j = assegnazione_reads_cluster(cluster_reads1, cluster_reads2)

# Write on file
with open(output_file, 'w') as file:
    json.dump(cluster_j, file)