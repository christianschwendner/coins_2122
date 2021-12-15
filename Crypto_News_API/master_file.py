import pandas as pd
import os
import glob


# use glob to get all the excel files
# in the folder
path = os.getcwd()
excel_files = glob.glob(os.path.join("output", "*.xlsx"))

print("Read in files ...")
# loop over the list of excel files
appended_data = []
for f in excel_files:
    # read the excel file
    df = pd.read_excel(f)
    # store DataFrame in list
    appended_data.append(df)

    # print the filename
    print('File Name:', f.split("\\")[-1])

print("Concat & preprocess ...")
all_articles_df = pd.concat(appended_data, ignore_index=True)
all_articles_df['publishedAt'] = pd.to_datetime(all_articles_df['publishedAt'])
all_articles_df['publishedAt'] = all_articles_df['publishedAt'].dt.tz_localize(None)
print("Articles: " + str(len(all_articles_df)))

print("Save master")
all_articles_df.to_excel("output/master/articles_all_master.xlsx")

print("Job finished.")
