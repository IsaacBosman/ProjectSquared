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

#Groups exercises by day performed on
def group_by_day(dataframe, exercises):
    dataframe.sort_values(by=['Date'])

    all_ex = set(exercises)
    enc_ex = set()

    date_dict = {}
    #stop after all exercises in 'exercises' encountered
    for i in range(0,len(dataframe.index)):
        ex = dataframe['Exercise'].values[i:i+1]
        date = dataframe['Date'].values[i:i+1]
        if date[0] in date_dict.keys():
            date_dict[date[0]].append(ex[0])
        else:
            date_dict[date[0]] = [ex[0]]
        
        if ex[0] in all_ex:
            enc_ex.add(ex[0])
        
        if len(all_ex - enc_ex) == 0:
            break
    num_days = len(date_dict.keys())

    day_groups = {}
    for x, y in enumerate(date_dict.values()):
        day_groups[x] = y
    return day_groups

exercises = get_exercises(dataframe1)

exercise_df = get_exercise_rows(dataframe1, exercises)

print(group_by_day(exercise_df, exercises))

exercise_df = clean_exercise_rows(exercise_df)

print(exercise_df)