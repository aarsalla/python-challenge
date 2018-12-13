#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


data_file = pd.read_csv("Resources/election_data.csv")

print(data_file)


# In[2]:


total_votes = len(data_file)
total_votes


# In[3]:


candidates_count = data_file["Candidate"].value_counts()
candidates_count


# In[4]:


percentage_votes = (candidates_count/total_votes)*100
percentage_votes


# In[5]:


winner = candidates_count.idxmax()
winner


# In[6]:


print("Election results")

print("--------------------------------------------------------------------------")

print("Total votes: " + str(total_votes))

print("----------------------------------------------------------------------------")

print("Khan:" + " " + str(round(percentage_votes[0],3)) + "%" + "("+str(candidates_count[0])+")")
      
print("Correy:" + " " + str(round(percentage_votes[1],3)) + "%" + "("+str(candidates_count[1])+")")
      
print("Li:" + " " + str(round(percentage_votes[2],3)) + "%" + "("+str(candidates_count[2])+")")
      
print("O'Tooley:" + " " + str(round(percentage_votes[3],3)) + "%" + "("+str(candidates_count[3])+")")

print("----------------------------------------------------------------------------------------")
      
print("winner: " + winner)


# In[7]:


file = open('pypoll.txt','w')
file.write("Election results")
file.write("\n....................................................................................")
file.write("\nTotal votes: " + str(total_votes))
file.write("\n----------------------------------------------------------------------------")
file.write("\nKhan:" + " " + str(round(percentage_votes[0],3)) + "%" + "("+str(candidates_count[0])+")")
file.write("\nCorrey:" + " " + str(round(percentage_votes[1],3)) + "%" + "("+str(candidates_count[1])+")")
file.write("\nLi:" + " " + str(round(percentage_votes[2],3)) + "%" + "("+str(candidates_count[2])+")")
file.write("\nO'Tooley:" + " " + str(round(percentage_votes[3],3)) + "%" + "("+str(candidates_count[3])+")")
file.write("\n----------------------------------------------------------------------------------------")
file.write("\nwinner: " + winner)
file.close()


# In[ ]:




