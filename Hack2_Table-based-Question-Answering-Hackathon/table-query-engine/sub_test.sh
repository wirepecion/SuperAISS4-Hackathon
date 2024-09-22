#!/bin/bash
#SBATCH -p gpu                          # Specify partition [Compute/Memory/GPU]
#SBATCH -N 1 -c 64                      # Specify number of nodes and processors per task
#SBATCH --ntasks-per-node=1		        # Specify number of tasks per node
#SBATCH --gpus-per-node=4		        # Specify total number of GPUs
#SBATCH -t 12:00:00                    # Specify maximum time limit (hour: minute: second)
#SBATCH -A lt900053                      # Specify project name
#SBATCH -J TBLTEST_hackathon_submission         # Specify job name
#SBATCH -o /project/lt900053-ai2415/production/table-query-engine/out/test_log.out

module restore
ml Mamba
ml cudatoolkit/23.3_11.8
ml gcc

conda deactivate
conda activate /project/lt900053-ai2415/production/env/production
# export VLLM_NCCL_SO_PATH="~/.local/lib/python3.9/site-packages/nvidia/nccl/lib/libnccl.so.2"

python /project/lt900053-ai2415/production/table-query-engine/scripts/execute_query_engine.py \
    --query-json /project/lt900053-ai2415/production/datasets/TBLA/question_sample.json \
    --save-dir /project/lt900053-ai2415/production/table-query-engine/out/test.jsonl \
    --file /project/lt900053-ai2415/production/datasets/TBLA
