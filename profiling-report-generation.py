import pandas as pd
from ydata_profiling import ProfileReport
import argparse
import logging
from tqdm import tqdm
import time


def ydata_profile(df_path, report_path):
    logging.info(f"reading csv from:{df_path}")
    df = pd.read_csv(df_path)
    logging.info(f"generating profile report...")
    profile = ProfileReport(df, title="Profiling Report")
    logging.info(f"saving report at{report_path}")
    profile.to_file(report_path)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Script started successfully.")
    parser = argparse.ArgumentParser(description="Generate a data profiling")
    parser.add_argument("df_path", type=str, help="path to the csv file")
    parser.add_argument(
        "report_path", type=str, help="path to save the profiling report"
    )
    args = parser.parse_args()

    ydata_profile(args.df_path, args.report_path)
