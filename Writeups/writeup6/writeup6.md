# Write-up 6: Project 2

**Name:** Louise Lima  
**Student ID:** llima23  
**Date:** 12/09/2025  

---
##Project Overview

##Goal:
Find the functional gene expression changes in patients with IBD and the celltypes with strongest changes

##Rationale:
IBD has very few treatments, most revolving around anti-inflammatory cytokine targeting. However, many of them have high rates of patients being resistant to the medication or developing tolerance
New solutions are needed, but to find more personalized medicines, we need a better understanidng of the polygenicity, the genes that are most effected in disease and the celltypes driving the differences in gene expression

##Specific Aims
1.Understanding the genes most differentially expressed in IBD
2.Understanding the celltypes and locations in the gut with most differentially expressed genes
3.Finding potential new drug targets/repurposing drugs for IBD

##Data
##Datasets
1. scRNAseq dataset (.h5ad file) of gut tissues throughout digestive tract -- focusing on colon, small intestine, and ileum for IBD
2. GWAS .tsv file with 18000 genes and their genetic variants association to IBD

##Suitability
most preprocessing will be filtering of data to make sure the genes of the two datasets align and are labeled in the same way, so that they can then be merged and compared

##Storage
I will be processing and storing all of this on Sherlock, since the GWAS dataset is 10GB
I will upload all code to my lab github

##Environment
Using sherlock
Common python and R packages used.
MAGMA analysis pipeline is used, downloaded from online -- for correlation analyses
version control maintained in an environment

##Pipeline
1. Differential expression analysis in python between healthy and disease gene expression
2. Significant genes identified from GWAS summary statistics
3. Correlation analyses using MAGMA analysis pipeline to determine the genes most associated and conditional analysis to find independent significant genes and celltypes.

##Machine Learning
Based on a person's genome -- predict their probability of being resistant to a therapeutic
Train model on their genetic variants and whether or not they are resistant to therapeutics
Predict new patients resistance

