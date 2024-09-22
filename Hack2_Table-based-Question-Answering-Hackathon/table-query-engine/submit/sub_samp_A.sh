#!/bin/bash
#SBATCH -p gpu                          # Specify partition [Compute/Memory/GPU]
#SBATCH -N 1 -c 64                      # Specify number of nodes and processors per task
#SBATCH --ntasks-per-node=1		        # Specify number of tasks per node
#SBATCH --gpus-per-node=4		        # Specify total number of GPUs
#SBATCH -t 12:00:00                    # Specify maximum time limit (hour: minute: second)
#SBATCH -A lt900047                     # Specify project name
#SBATCH -J TBLA_Machima_hackathon_submission         # Specify job name
#SBATCH -o /home/projratc/SPAIHack/logs/TBLA-Machima.out

module restore
ml Mamba
ml cudatoolkit/23.3_11.8
ml gcc/10.3.0

conda deactivate
conda activate /project/lt900053-ai2415/production/env/production
export VLLM_NCCL_SO_PATH="/home/projratc/.local/lib/python3.9/site-packages/nvidia/nccl/lib/libnccl.so.2"

python /project/lt900053-ai2415/production/table-query-engine/scripts/execute_query_engine.py \
    --query-json /home/projratc/SPAIHack/TBLA/small_question.json \
    --save-dir /home/projratc/SPAIHack/submission/TBLA/Machima-small-submission.jsonl \
    --csv-file /project/lt900053-ai2415/production/datasets/TBLA/tbla.csv