import pandas as pd

start_graph = {
    'B': 'E', 'E': 'H', 'H': 'K', 'K': 'N', 'N': 'Q', 'Q': 'T', 'T': 'W', 'W': 'Z',
    'Z': 'AC', 'AC': 'AF', 'AF': 'AI', 'AI': 'AL', 'AL': 'AO', 'AO': 'AR', 'AR': 'AU',
    'AU': 'AX', 'AX': 'BA'
}

end_graph = {
    'D': 'G', 'G': 'J', 'J': 'M', 'M': 'P', 'P': 'S', 'S': 'V', 'V': 'Y', 'Y': 'AB',
    'AB': 'AE', 'AE': 'AH', 'AH': 'AK', 'AK': 'AN', 'AN': 'AQ', 'AQ': 'AT', 'AT': 'AW',
    'AW': 'AZ', 'AZ': 'BC'
}

def cleaning_steps(data: pd.DataFrame) -> pd.DataFrame:
    date = data.columns[2].split('-')
    col_names = data.iloc[0].values
    col_names[0] = 'index'
    data = data.iloc[1:]
    data.columns = col_names

    # creating columns for date
    data['month'] = date[0]
    data['year'] = int(date[1]) + 2000

    # set index
    data = data.set_index('index').dropna()
    return data