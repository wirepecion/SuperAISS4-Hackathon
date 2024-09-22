#!/bin/bash
#SBATCH -p compute                          # Specify partition [Compute/Memory/GPU]
#SBATCH -N 1 -c 64                      # Specify number of nodes and processors per task
#SBATCH --ntasks-per-node=1		# Specify number of tasks per node
#SBATCH --gpus-per-node=0	        # Specify total number of GPUs
#SBATCH -t 4:00:00                     # Specify maximum time limit (hour: minute: second)
#SBATCH -A lt900053                 # Specify project name
#SBATCH -J zero_to_fp32                          # Specify job name


ml Mamba
conda deactivate
conda activate ./env

python ./scripts/zero_to_fp32.py \
    /project/lt900053-ai2415/jack-finetune/SuperAI_LLM_FineTune/llama-big \
    /project/lt900053-ai2415/jack-finetune/SuperAI_LLM_FineTune/llama-big/pytorch_model.bin