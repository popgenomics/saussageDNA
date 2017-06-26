# saussageDNA.py  Produces one fasta file per window of fixed size (arg2) from a fasta file (arg1) 
Also produces a txt file per fasta file: locus_name, contig_name, first position of the non-coding region (0-based), last position of non-coding region (0-based)  
  
## Exemple:  
./saussageDNA.py nonCoding_Hmel201012_0.fasta 10000 
**arg1:** fasta file  
**arg2:** window size (non-overlapping) 
  
The fasta file is an alignement of one contig for different individuals.  
  
