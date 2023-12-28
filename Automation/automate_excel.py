import pandas as pd

# Using a relative path if the Excel file is in the same directory
df = pd.read_excel('file.xlsx')

# OR using the full path
# df = pd.read_excel('/full/path/to/file.xlsx')

print(df)