# Write-up 4: Pipeline

**Name:** Louise Lima  
**Student ID:** llima23  
**Date:** 12/04/2025  

---

##1. Salmon Index
main addition: 
    if (params.index == null){
        param_index = SALMON_INDEX(params.transcriptome)
        quant_ch   = SALMON(trimmed_ch, params_index)}
    else:
        quant_ch   = SALMON(trimmed_ch, params.index)


