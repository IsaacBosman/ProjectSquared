# import pandas lib as pd
import pandas as pd
import numpy as np
 
BOILER_PLATE = ["JPG Coaching 10 Week Men's", 'Monday: Upper', 'Tuesday: Lower', 'Thursday: Chest/Back', 'Friday: Arms + Lower B']

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('E:\Project^2\JPG Gym Spreadsheet.xlsx')
 
print(dataframe1)

#Returns a list of exercises
def get_exercises(dataframe):
    exercises = dataframe["Exercise"].unique()
    mask = np.ones(len(exercises), dtype=bool)
    for i, exercise in enumerate(exercises):
        if exercise in BOILER_PLATE or exercise is np.NAN:
            mask[[i]] = False
    exercises = exercises[mask,...]

    return exercises

def get_exercise_rows(dataframe, exercises):
    #Create a mask: 0 if value in Exercise column is not in exercises, 1 otherwise
    mask = dataframe.Exercise.isin(exercises)
    dataframe.drop(dataframe[~mask].index, inplace=True)
    return dataframe

def clean_exercise_rows(dataframe):
    cln_df = dataframe.dropna(subset=['Wt.'])
    return cln_df

exercises = get_exercises(dataframe1)



exercise_df = get_exercise_rows(dataframe1, exercises)
print(clean_exercise_rows(exercise_df))