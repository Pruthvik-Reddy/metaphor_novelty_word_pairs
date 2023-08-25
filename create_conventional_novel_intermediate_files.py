import csv
import pandas as pd

data=pd.read_csv("Metaphor_Novelty_train.csv")

novel_words_1=[]
novel_words_2=[]
novel_scores=[]

conventional_words_1=[]
conventional_words_2=[]
conventional_scores=[]

intermediate_words_1=[]
intermediate_words_2=[]
intermediate_scores=[]


for ind,row in data.iterrows():
    id=row["ID"]
    score=row["Score"]
    words=id.split("__")
    word1=words[1].split("_")[0]
    word2=words[2].split("_")[0]
    
    if score<1.0:
      conventional_words_1.append(word1)
      conventional_words_2.append(word2)
      conventional_scores.append(score)
    elif score>2.0 and score<3.0:
      novel_words_1.append(word1)
      novel_words_2.append(word2)
      novel_scores.append(score)
      
    else:
      intermediate_words_1.append(word1)
      intermediate_words_2.append(word2)
      intermediate_scores.append(score)

columns=["word1","word2","score"]
conventional_data={"word1":conventional_words_1,"word2":conventional_words_2,"score":conventional_scores}
intermediate_data={"word1":intermediate_words_1,"word2":intermediate_words_2,"score":intermediate_scores}
novel_data={"word1":novel_words_1,"word2":novel_words_2,"score":novel_scores}

conventional_df=pd.DataFrame(conventional_data)
intermediate_df=pd.DataFrame(intermediate_data)
novel_df=pd.DataFrame(novel_data)

conventional_df.to_csv("conventional.csv")
intermediate_df.to_csv("intermediate.csv")
novel_df.to_csv("novel.csv")