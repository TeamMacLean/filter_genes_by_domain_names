## Introduction

Filtering out genes by gene names. The data is in multiple columns, first column has gene name and the rest columns start with domain name.

## Usage:

python filter_genes_by_domain_names.py inputfilename

## Sample test data

```OBART12G07330.1 Rx_N(start=20, stop=100, evalue=1.9e-13) NB-ARC(start=182, stop=426, evalue=2.2e-52)
OBART12G07370.1 Rx_N(start=12, stop=99, evalue=5e-21) NB-ARC(start=173, stop=390, evalue=5.8e-48) LRR_8(start=604, stop=642, evalue=0.68)
OBART12G07970.1 Rx_N(start=30, stop=113, evalue=1.1e-18) NB-ARC(start=190, stop=414, evalue=7.5e-49) DPR8(start=604, stop=642, evalue=0.68)
OBART12G07330.1 DPR8(start=20, stop=100, evalue=1.9e-13) NB-ARC(start=182, stop=426, evalue=2.2e-52)
OBART11G22480.1 Rx_N(start=9, stop=89, evalue=1.2e-23) NB-ARC(start=185, stop=392, evalue=8.9e-48) LRR_8(start=513, stop=567, evalue=0.00012) LRR_4(start=850, stop=890, evalue=0.82)```


## Rules to filter out 
Xdomains="TIR", "TIR2", "LRR", "LRR_8", "Rx_N","RPW8"

1) if there is a X domain and NB-ARC，remove it
2) if there is a X domain, NBARC and one or more non X domain, keep it
3) if there are multiple X domains and NBARC, remove it
4) if there is a non X domain and NBARC, keep it
5）if there is no X domain, no non X domain and only one domain that is NBARC, remove it

Using the test data above, the script has to print out line 3 and 4 only.

