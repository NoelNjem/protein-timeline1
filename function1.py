import sqlite3
import re
import pandas as pd
#import database.py

con = sqlite3.connect('database.db')
c = con.cursor()

# The first method of string splitting: separating the unit and value. Not used here if the database will be reformatted
# And following Dr. Ray's suggestion, this function will not be used
# Keeping the mysplit() command here in case we will need it in the future, but this current code is non-ideal for splitting
"""

def mysplit(s):
    unit = re.sub(r'^\d+', "", s)
    value = s[:len(unit)]
    return value, unit
    
    """

# The real meat of the function
# Obtaining the entities that have "contains" across the three tables that we have relationships listed

c.execute("select Entity_ID_1, count(*) from Relationships_1_1 WHERE Relationship = 'Contains' group by Entity_ID_1 ")
sizes1 = c.fetchall()

c.execute("select Entity_ID_1, count(*) from Relationships_1_2 WHERE Relationship = 'Contains' group by Entity_ID_1 ")
sizes2 = c.fetchall()

c.execute("select Entity_ID_1, count(*) from Relationships_1_3 WHERE Relationship = 'Contains' group by Entity_ID_1 ")
sizes3 = c.fetchall()

# Join into one table for calculation

joined = sizes1 + sizes2 + sizes3
"""
To print and check any of the tables: 

for x in joined: 
    print(x)

"""

# Joining the data and calculating a recommended height
# Currently our data does not have three-tier containment so this will suffice for now
# if there is containment within containment we will need to further encompass that case

joineddata = pd.DataFrame.from_records(joined, columns=['Entity ID', 'Contains']).groupby('Entity ID').sum()

# The current recommended height formula is double the number of units it contains plus one, so that it can fully contain it
joineddata['Recommended Height'] = joineddata['Contains'] * 2 + 1
print(joineddata)

# joineddata['Recommended Height'] can be used as return value wrapped in a function
# for columns that do not have a value assigned here (i.e., the entities that don't contain other entities), the default height will be 1