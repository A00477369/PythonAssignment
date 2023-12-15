import pandas as pd

df = pd.read_csv('titles.csv')

def count_vowels_in_column(dataframe, column_name):
    
    if column_name not in dataframe.columns:
        print(f"Column '{column_name}' not found in the DataFrame.")
        return

    dataframe[column_name] = dataframe[column_name].astype(str)

    vowel_counts = dataframe[column_name].str.lower().str.count('[aeiou]')


    dataframe[f'{column_name}_vowel_count'] = vowel_counts

    return dataframe

result_df = count_vowels_in_column(df, 'title')

print(result_df)

result_df.to_csv("output.csv", index = False)
