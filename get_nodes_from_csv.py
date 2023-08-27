import csv
import pandas as pd

data=pd.read_csv("english_assertions.csv",header=None,delim_whitespace=True)

data.columns=["relation","start_node","end_node"]



metaphor_columns=["word1","word2","score"]
csv_file = 'intermediate.csv'
conventional_data=pd.read_csv(csv_file)
conventional_words1=conventional_data["word1"]
conventional_words2=conventional_data["word2"]


        

positive_metaphoric_pairs_count=0
negative_metaphoric_pairs_count=0


for i in range(len(conventional_words1)):
  concept1=conventional_words1[i]
  concept2=conventional_words2[i]

  filtered_data = data[data.iloc[:, 1] == concept1]
  filtered_data_2 = data[data.iloc[:, 2] == concept1]
  combined_df = pd.concat([filtered_data, filtered_data_2], axis=0)
  end_exists = combined_df["start_node"].str.contains(concept2, case=False) | combined_df["end_node"].str.contains(concept2, case=False)
  if end_exists.any():
     positive_metaphoric_pairs_count+=1
     #print("Positive : ", concept1,concept2)
  else:
    negative_metaphoric_pairs_count+=1
    #print("Negative : ", concept1,concept2)
    

    

print("The fraction of pairs containing edges is : ",positive_metaphoric_pairs_count/len(conventional_words1))
print("The fraction of pairs not containing edges is : ",negative_metaphoric_pairs_count/len(conventional_words1))

