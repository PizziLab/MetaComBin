import sys
import json

def main():
    if len(sys.argv) != 5:
        print("Usage: python nome_script.py inputCl dataset.fasta output_file.fna.1 output_file.fna.2")
        return
    
    cluster_file = sys.argv[1]
    dataset_file = sys.argv[2]
    output_file1 = sys.argv[3]
    output_file2 = sys.argv[4]

    # Load dataset
    with open(dataset_file, 'r') as f:
        dataset = f.readlines()
    dataset = ''.join(dataset)
    
    # Load cluster
    with open(cluster_file, 'r') as file:
        cluster = json.load(file)
    
    with open(output_file1, 'w') as out1:
        with open(output_file2, 'w') as out2:
            data = dataset.split('\n')
            for read in cluster.keys():
                if(read != ""):
                    for i in range(len(data)):
                        if(data[i].startswith('>')):
                            if(read == data[i].split('>')[1].split('.')[0]):
                                out1.write(data[i])
                                out1.write('\n')
                                out1.write(data[i+1])
                                out1.write('\n')
                                out2.write(data[i+2])
                                out2.write('\n')
                                out2.write(data[i+3])
                                out2.write('\n')

if __name__ == '__main__':
    main()
