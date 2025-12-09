#!/usr/bin/env python3

#read in from ecoli_bakta_out/assembly.faa
from Bio import SeqIO
import matplotlib.pyplot as plt
import pandas as pd
protein_fasta = "ecoli_bakta_out/assembly.faa"

# Use SeqIO.parse for multiple sequences in the file
# The "fasta" format string correctly handles .faa files
sequences = SeqIO.parse(protein_fasta, "fasta")

# Iterate through the sequences and access their data
protein_data = []
for record in sequences:
   protein_id = record.id
   protein_name = record.description.split(' ', 1)[1] if ' ' in record.description else record.description
   protein_data.append({'protein_id': protein_id, 'protein_name': protein_name})
   #print(f"ID: {record.id}")
   #print(f"Description: {record.description}")
   #print(f"Sequence: {record.seq}")
   #print("-" * 20)

# If you expect only a single sequence in the file, you can use SeqIO.read
    # single_sequence = SeqIO.read(file_path, "fasta")
    # print(f"ID (single): {single_sequence.id}")
    # print(f"Sequence (single): {single_sequence.seq}")
df_names = pd.DataFrame(protein_data)
print(f"Loaded {len(df_names)} protein records from the FAA file.")

#read in from ecoli_prot90_cluster.tsv
import csv
clusters = "ecoli_prot90_cluster.tsv"
df = pd.read_csv(clusters, sep='\t')
# Ensure column names match the file structure
df.columns = ['cluster_id', 'protein_id']

# 2. Identify clusters with more than one protein (paralogs)
# Group by 'cluster_id' and filter groups where the size is > 1
paralog_clusters_df = df.groupby('cluster_id').filter(lambda x: len(x) > 1)
paralog_clusters_df = paralog_clusters_df.groupby('cluster_id').size().reset_index(name='cluster_sizex')
print(paralog_clusters_df.head())

# 3. Compute the copy number for each protein (number of occurrences per cluster)
# Use groupby on both columns and count occurrences
#protein_counts = df.groupby(['cluster_id', 'protein_id']).size().reset_index(name='copy_number')
protein_counts = df.groupby('protein_id').size().reset_index(name='copy_number')
print(protein_counts)

joint_df = pd.merge(protein_counts, df_names, on='protein_id', how='inner')

# Reorder columns as requested: protein_id, protein_name, copy_number
joint_df = joint_df[['protein_id', 'protein_name', 'copy_number']]

print("\nSuccessfully created joint DataFrame:")
print(joint_df.head())
print(f"Total rows in joint DataFrame: {len(joint_df)}")

# Optional: Save the combined results to a new file
joint_df.to_csv('joint_paralog_data.tsv', sep='\t', index=False)

# 5. Visualization (Bar plot of top 10 most frequent paralogs)
top_n = 10
top_paralogs = paralog_clusters_df.sort_values(by='cluster_sizex', ascending=False).head(top_n)

plt.figure(figsize=(12, 6))
# Use protein names for better labels
plt.barh(top_paralogs['cluster_id'], top_paralogs['cluster_sizex'], color='skyblue')
#plt.barh(top_paralogs['protein_name'], top_paralogs['copy_number'], color='skyblue')
plt.xlabel('Copy Number (Frequency)')
plt.ylabel('Cluster Name')
plt.title(f'Top {top_n} Most Frequent Paralogs Across the Genome')
plt.gca().invert_yaxis() # Highest count at the top
plt.tight_layout()

# Save and show the visualization
plt.savefig('top_clusters.png')
print(f"Visualization saved to {'top_clusters.png'}")
plt.show()

"""
print("\nData with copy number for each protein:")
print(df_with_counts.head())

summary = pd.Dataframe(columns=['protein_id','protein_"""

"""# Read as a list of lists
with open(clusters, 'r', encoding='utf8') as tsv_file:
    tsv_reader = csv.reader(tsv_file, delimiter='\t')
    for row in tsv_reader:
        print(row)

# Read as a dictionary for each row (using header as keys)
with open(clusters, 'r', encoding='utf8') as tsv_file:
    tsv_dict_reader = csv.DictReader(tsv_file, delimiter='\t')
    for row_dict in tsv_dict_reader:
        print(row_dict)
        # Access specific fields:
        # print(row_dict['HeaderName'])
"""
