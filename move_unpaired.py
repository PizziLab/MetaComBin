import sys
import json

def create_read_map(cluster):
    cluster_map = {}
    current_read = None

    for line in cluster.split('\n'):
            fields = line.split('.')
            current_read = fields[0] # Remove ".1" from read name
            
            if current_read not in cluster_map:
                cluster_map[current_read] = 0
            cluster_map[current_read] += 1

    return cluster_map

def unpaired_move(work_cl, cl1):
    copied = work_cl.copy()
    for read in work_cl.keys():
        if(work_cl[read] == 1):
            if read in cl1.keys():
                cl1[read] += 1
            del copied[read]
    return copied

def main():
    if len(sys.argv) != 5:
        print("Usage: python nome_script.py inputCl1 inputCl2 outputCl1 outputCl2")
        return
    
    cluster_file1 = sys.argv[1]
    cluster_file2 = sys.argv[2]
    output_file1 = sys.argv[3]
    output_file2 = sys.argv[4]

    # Load input files
    # Cluster 1
    with open(cluster_file1, 'r') as f:
        cluster1 = f.readlines()
    cluster1 = ''.join(cluster1)

    # Cluster 2
    with open(cluster_file2, 'r') as f:
        cluster2 = f.readlines()
    cluster2 = ''.join(cluster2)
    
    # Create read map - Cluster 1
    cluster_map1 = create_read_map(cluster1)

    # Create read map - Cluster 2
    cluster_map2 = create_read_map(cluster2)
    
    # Move unpaired reads from Cl2 to Cl1
    newCluster2 = unpaired_move(cluster_map2, cluster_map1)

    # Scrivo i nuovi cluster in dei file json
    with open(output_file1, 'w') as f:
        json.dump(cluster_map1, f)

    with open(output_file2, 'w') as f:
        json.dump(newCluster2, f)
    
if __name__ == '__main__':
    main()
