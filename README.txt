From the link provided in the paper "A corpus of metaphor novelty scores for syntactically related word-pairs", 
download the two files ( train and test)

Experiment 1 : 
- For the pair of words, the range in dataset is (0-3), 0-1 indicating conventional, 2-3 indicating novel metaphors 
and 1-2 indicating metaphors that fall somewhere between conventional and novel. 
- Seperate the metaphors into three files, conventional.csv, novel.csv and intermediate.csv
- For the pair of words in those files, calculate if there exists a conceptnet path between them. Calculate what percentage of total
 metaphors in each file satisfy that.
- When checking if there exists a path, we should not only check the direct concepts, but also some other concepts
where the current one is part of. For example, there is no edge between alocohol and abuse, but there exists a 
concept "alcohol_abuse."  

