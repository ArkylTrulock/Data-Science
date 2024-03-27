import spacy

#TASK 1
#------
# EXAMPLE 1
#----------

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2)) # 0.5929929675536907 - Cats are 60% similar to monkeys. This model has ascertained that they are both animals.
print(word3.similarity(word2)) # 0.4041501317354622 - Monkey is 40% similar to bannanas. This model has ascertained that monkeys are linked to bannanas. They eat bannanas.
print(word3.similarity(word1)) # 0.22358827466989753 - Cat is 22% similar to bannana. This model has ascertained that cats are not linked to bannanas. They prefer other food options.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#TASK 1
#------
# EXAMPLE 2
#----------

nlp = spacy.load('en_core_web_md')

tokens = nlp('cat monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#cat cat 1.0
#cat monkey 0.5929929614067078
#cat banana 0.2235882729291916
#monkey cat 0.5929929614067078
#monkey monkey 1.0
#monkey banana 0.404150128364563
#banana cat 0.2235882729291916
#banana monkey 0.404150128364563
#banana banana 1.0

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# There similarity is (0.5929929614067078) between cat & monkey.
# Cats are 60% similar to monkeys. This model has ascertained that they are both animals.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# The similarity is (0.404150128364563) between monkey & bannana . 
# Monkey is 40% similar to bannanas. This model has ascertained that monkeys are linked to bannanas. TThey most likely prefer to eat bannanas. 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Th similarity is (0.2235882729291916) between cat & bannana.
# Cat is 22% similar to bannana. This model has ascertained that cats are not linked to bannanas. They most likely prefer other food options. 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


#TASK 1
#------
#EXAMPLE 3
#---------

nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
#cat monkey 0.6611432433128357
#cat banana 0.24856486916542053
#monkey cat 0.6611432433128357
#monkey monkey 1.0
#monkey banana 0.3922763168811798
#banana cat 0.24856486916542053
#banana monkey 0.3922763168811798
#banana banana 1.0
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## There similarity is (0.6611432433128357) between cat & monkey. This is 6% higher than the similarity in the previous model.
# Cats are 66% similar to monkeys. This model has ascertained that they are both animals.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# The similarity is (0.3922763168811798) between monkey & bannana. This is 1% lower than the similarity in the previous model.
# Monkey is 39% similar to bannanas. This model has ascertained that monkeys are linked to bannanas. They most likely prefer to eat bannanas.        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Th similarity is (0.24856486916542053) between cat & bannana. This is 3% higher than the similarity in the previous model.
# Cat is 25% similar to bannana. This model has ascertained that cats are not linked to bannanas. They most likely prefer other food options.        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

