# MetaComBin 

MetaCombin is a pipeline for the binning of metagenomics reads. It combines two metagenomics read binning approaches: AbundanceBin (based on species abundances) and MetaProb (based on reads overlap). The two tools can be downloaded from their respective repositories.

AbundanceBin: https://omics.informatics.indiana.edu/AbundanceBin/

MetaProb: https://bitbucket.org/samu661/metaprob/src/master/


---

Step 1 : Run AbundanceBin
- AbundancdeBin takes as input a single fasta file. If you are working with paired-end reads (e.g. dataset.fasta.1 and dataset.fasta.2), you must provide a single input dataset.fasta file that is a combined version of the .1 and .2 paired end files 

Example for running from the command line:

      abundancebin -input file.fasta -output abCluster.log -RECURSIVE_CLASSIFICATION

---


Step 2 : Evaluate AbundanceBin results
- The output of AbundanceBin is a set of n files (one for each cluster named abCluster.log.1 abCluster.log.2 ... abCluster.log.n
- The input clusters.json file is the results of the merging of all the .log clusters obtained from AbundanceBin
- The input data_truth.json is the .fasta file converted into read - specie pairs

Example for running from command line:

    python3 abbin_eval.py [clusters.json] [data_truth.json] [output.txt]

---

Step 3 : Move unpaired reads

- Move unpaired reads from the cluster X with the highest number of unpaired reads [abCluster.log.X] to another cluster [abCluster.log.Y]. This must be repeated for each other cluster Y in which the reads of [abCluster.log.X] can be moved. If after the re-assignment of all the unpaired reads of abCluster.log.X there are still clusters with unpaired reads, repeat the process by taking the next cluster with the highest number of unpaired reads in input as [abCluster.log.X]. 

Example for running from command line:

    python3 move_unpaired.py [cl1.log.1] [cl2.log.2] [newCl1.json] [newCl2.json]

---

Step 4 : Split each cluster obtained from the previous step, and thus composed by paired-reads only, in two files, one per part of the pair, to set up the appropriate input format for MetaProb

Example for running from command line:
   
    python3 split_cluster.py [cluster.json] [dataset.fasta] [cluster.fna.1] [cluster.fna.2]

---

Step 5 : Run MetaProb on each cluster

Example for running from command line:
   
    MetaProb -feature 1 -pi input.fna.1 input.fna.2

---

Step 6 : Evaluate MetaProb results
- Let file.fna.1.clusters.csv the file returned in output by MetaProb

Example for running from command line:
  
    python3 metaprob_count.py [file.fna.1.clusters.csv] [dataset.fna.1] [output.txt]

---
