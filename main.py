import os
from analyzer import (
    load_logs,
    analyze_logs
)

# ---------------------------------------------------

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
LOGS_PATH = os.path.join(DATA_DIR, 'log_small.txt')

# ---------------------------------------------------

if __name__ == '__main__':
    # load logs as dataframe
    df_logs = load_logs(LOGS_PATH)

    # analyze logs
    analyze_logs(df_logs)
