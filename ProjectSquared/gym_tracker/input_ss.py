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

print(get_exercises(dataframe1))