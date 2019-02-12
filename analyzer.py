import pandas as pd


def load_logs(path):
    # where data will be stored
    ips = []
    timestamps = []
    commands = []
    http_codes = []
    response_bytes = []

    # load file
    with open(path, 'r') as f:
        # analyze each line of file
        for line in f:
            # split by space
            line_splitted = line.split(' ')

            ips.append(line_splitted[0])
            timestamps.append(int(line_splitted[3]))
            commands.append(line_splitted[4])
            http_codes.append(int(line_splitted[5]))
            response_bytes.append(int(line_splitted[6]) if line_splitted[6].isdigit() else float('NaN'))

        df = pd.DataFrame(data={
            'ip': ips,
            'timestamp': timestamps,
            'command': commands,
            'http_code': http_codes,
            'response_bytes': response_bytes,
        })

        return df


def analyze_logs(df_logs):
    # TODO: Perform analysis here
    pass
