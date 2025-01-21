import sys
import json 

def create_read_map(dataset):
    read_map = {}
    current_gi = None

    for line in dataset.split('\n'):
        if line.startswith('>'):
            fields = line.split('|')           
            gi = fields[-1].split('"')[1]
            current_gi = gi
            read_id = line.split('>')[1].split('.')[0]       
            if current_gi not in read_map:
                read_map[current_gi] = []
            read_map[current_gi].append(read_id)
    return read_map

def main():
    if len(sys.argv) != 3:
        print("Usage: python nome_script.py input_file output_file")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Load input
    with open(input_file, 'r') as f:
        dataset = f.readlines()
    dataset = ''.join(dataset)

    # Create read map
    read_map = create_read_map(dataset)

    # Write on file
    with open(output_file, 'w') as f:
        json.dump(read_map, f)

if __name__ == '__main__':
    main()

