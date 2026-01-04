import pandas as pd
import json
from IPython.display import display

# function to read JSON data and extract win/loss records
def loadData(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def buildMatrix(data):
    # Get all team names and sort them
    teams = sorted(data.keys())
    
    # Create a matrix to hold the win values
    matrix = {}
    
    for home_team in teams:
        matrix[home_team] = {}
        for away_team in teams:
            if home_team == away_team:
                # when home team = away team, set to "--"
                matrix[home_team][away_team] = "--"
            else:
                # Extract the "W" (wins) values from the nested dictionary
                wins = data[home_team][away_team]["W"]
                matrix[home_team][away_team] = wins
    
    # Convert to DataFrame with teams as both rows and columns
    df = pd.DataFrame(matrix).T
    df.index.name = "Tm"
    df.columns.name = None
    
    return df

## main function which will call other functions to produce matrix visualization of json data
def main():
    filename = "data.json"
    data = loadData(filename)
    result_df = buildMatrix(data)
    display(result_df)

main()