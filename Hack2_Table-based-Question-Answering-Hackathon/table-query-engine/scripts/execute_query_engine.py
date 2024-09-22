import argparse
import json
import time

############################
# You can edit you code HERE
from query_engine import initialize_query_engine

import pandas as pd
import markdown

############################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to execute query engine.")
    parser.add_argument(
        "--query-json", type=str, required=True, help="Path to json of quert str."
    )
    parser.add_argument(
        "--save-dir",
        type=str,
        default="./output.jsonl",
        help="Path to output response.",
    )
    parser.add_argument(
        "--files",
        type=str,
        help="Path to input path of data",
    )
    args = parser.parse_args()

    ############################
    # You can edit you code HERE

    df = pd.read_csv(f"{args.files}/table.csv")

    f = open(f"{args.files}/data_description.md", 'r')
    md = markdown.markdown(f.read())

    query_engine = initialize_query_engine(df, md)
    ############################

    with open(args.query_json, "r") as f:
        query_json = json.load(f)
    # Reset save_dir
    with open(args.save_dir, "w") as f:
        pass

    for idx, query_str in enumerate(query_json):
        t1 = time.time()
        response = query_engine(query_str).response
        elapsed_time = time.time() - t1
        with open(args.save_dir, "a") as f:
            json.dump(
                {
                    "idx": idx,
                    "query_str": query_str,
                    "response": response,
                    "elapsed_time": elapsed_time,
                },
                f,
                ensure_ascii=False,
            )
            f.write("\n")
