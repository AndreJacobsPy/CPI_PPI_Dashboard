import pandas as pd
from functions import cleaning_steps, start_graph, end_graph

# need to loop through all the relevant sheets in spreadsheet
sheets = [f'200{i}' if i < 10 else f'20{i}' for i in range(3, 24)]
dfs = []

for sheet in sheets:
    print(f'Processing sheet {sheet}...')

    # read in excel sheet
    start, end = 'B', 'D'
    update = False
    while start in start_graph and end in end_graph:
        # looping through each month in spreadsheet
        if update:
            start = start_graph[start]
            end = end_graph[end]

        # read in new chunk of spreadsheet
        data = pd.read_excel('CPIHistoricalForecast.xlsx', usecols=f'A, {start}:{end}', skiprows=2, sheet_name=sheet)
        df = data.copy()

        ## cleaning data
        dfs.append(cleaning_steps(df.copy()))
        update = True

    # combine all dataframes
    df = pd.concat(dfs)
    # print(df.head())

print(df.shape)
df.to_excel('CPI_cleaned.xlsx')