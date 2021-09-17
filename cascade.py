
# Imports

import pandas as pd
import numpy as np

"""# Generate data"""

optList = 'Opt1	Opt2	Opt3	Opt4	Opt5	Opt6	Opt7	Opt8	Opt9	Opt10	Opt11	Opt12	Opt13	Opt14	Opt15'
optList = optList.split('	')

# Lets pick 10 out of 15 randomly for 20 different observations
# Create a table of these 10 options for the 20 obs

prefList = []
for obs in range(20):
    temp_arr = np.random.choice(optList, 10, replace = False)
    prefList.append(temp_arr)
colNames = ['p'+str(i) for i in range(1,11)]
df = pd.DataFrame(prefList, columns=colNames)

df.head()

"""# Drop items

"""

# Plan is to drop some of these options randomly. 
# The dataframe should adjust the preferences accordingly.
# The dropped preferences can show a None or a Nan or whatever.

# Using replace to make certain options NA (Not available)
# Exp 1 - Replace all Odd values with NA

df.replace(['Opt1','Opt3','Opt5','Opt7','Opt9','Opt11','Opt13','Opt15'], 'NA', inplace = True)

df.head()

"""# Cascade Arrange"""

# Cascade/Rearrange the options in this new table
def cascadeHelper(dataseries, invalidText = 'NA', highToLow = True):
    '''
    Helper function for cascadeMove

    data: input type for data is series.
    invalidText: Ths is the the text which marks NA or nan or the string which needs to be moved out fo the way.
    highToLow: True if the preferences are marked high to low. This means after cascading, the preferences will be marked 1-k followed by NAs
                if False, the preferences will be NAs followed by 1-k preferences
    
    The order of the preferences is preserved.
    '''
    dataseries.replace(invalidText, np.nan, inplace = True)
    Cnt_na = dataseries.isna().sum()
    if highToLow == True:
        return dataseries.dropna().append(pd.Series(['NA']*Cnt_na)).reset_index(drop = True)
    elif highToLow == False:
        return pd.Series(['NA']*Cnt_na).append(dataseries.dropna()).reset_index(drop = True)
    

def cascadeMove(df, invalidText = 'NA', highToLow = True, ax = 1):
    '''
    Moves the preferences to the front or to the end by dropping out NAs.
    Can choose axis to move them up or down instead.

    Calls the cascadeHelper function
    '''
    tempColNames = df.columns
    df = df.apply(cascadeHelper, axis = ax , args = (invalidText, highToLow))
    df.columns = tempColNames
    return df

cascadeMove(df, invalidText = 'NA', highToLow = True, ax = 1)

