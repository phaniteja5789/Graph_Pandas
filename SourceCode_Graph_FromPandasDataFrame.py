#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
import random


# In[2]:


df=pd.read_csv("C:\\Users\\krish\\OneDrive\\Desktop\\Graph_Data.csv")


# In[3]:


df.sort_values(by=["level"],ascending=True,inplace=True)


# In[4]:


class Node:
    def __init__(self,taskName,level):
        self.taskName=taskName
        self.level=level
        self.parents=[]
        self.children=[]


# In[5]:


df.head()


# In[6]:


queue_list_node=[]


# In[7]:


def GetRootNode():
    return df.iloc[0]

root_df=GetRootNode()
root_Node=Node(root_df.task_name,root_df.level)


# In[8]:


#Create queue and store all Nodes
queue_nodes=[]
queue_nodes.append(root_Node)
created_nodes={root_Node.taskName}


# In[9]:


#create a temporary dummy list to Nodes
traversal_nodes=[]


# In[10]:


def GetInfoOfNodeFromDF(FindTaskNameIndex):
    return df[df["task_name"]==FindTaskNameIndex].index[0]

while (len(queue_nodes)!=0):
    get_node=queue_nodes.pop(0)
    index_location=GetInfoOfNodeFromDF(get_node.taskName)
    child_nodes_str=re.sub("[\[\]]","",df.iloc[index_location].child_node)
    child_nodes_list=child_nodes_str.split(',')
    for i in child_nodes_list:
        if i!="None" and i not in created_nodes:
            child_node=Node(i,get_node.level+1)
            get_node.children.append(child_node)
            child_node.parents.append(get_node)
            queue_nodes.append(child_node)
            created_nodes.add(i)
        elif i!="None":
            for j in queue_nodes:
                if j.taskName==i:
                    j.parents.append(get_node)
    traversal_nodes.append(get_node)


# In[11]:


#path to get the traversal of task Name
def NodeIsPresentNowTraverse(NodeToBeTraversed,answer):
    answer.append(NodeToBeTraversed.taskName)
    if len(NodeToBeTraversed.parents)==0:
        return answer
    return NodeIsPresentNowTraverse(random.choice(NodeToBeTraversed.parents),answer)

def pathToTraversal(taskName):
    taskNames=[]
    for i in traversal_nodes:
        taskNames.append(i.taskName)
    if taskName in taskNames:
        answer=[]
        answer=NodeIsPresentNowTraverse(traversal_nodes[taskNames.index(taskName)],answer)
        final_answer=""
        for i in answer[len(answer)-1::-1]:
            final_answer+=i+" --> "
        print(final_answer.rstrip("--> "))
    else:
        print("Given Task Name is not present")
        


# In[15]:


taskName=input()
pathToTraversal(taskName)


# In[ ]:




