# N-AryGraph_Pandas
Implementation of N-Ary Graph from Pandas DataFrame

**Requirement :**

  Get the Traversal Path to reach any Node that is present in the data frame.
  
**Input**

  The below is the dataframe
  
  <img width="496" alt="image" src="https://github.com/phaniteja5789/N-AryTree_Pandas/assets/36558484/32462d9e-e835-4011-bca0-bfe4c1591cf9">

 
**Implementation Approach**

  1.) Based on the data frame given, sorted the dataframe based on the Level Column in the dataframe
  2.) From Level-0, Implemented a BFS Traversal with using Queue DataStructure and construct the graph
  3.) From the input node, with the help of Parents column, traverse the path from given node till root node
  
 **Installed Modules**
 
 1.) Pandas
 2.) Numpy
 3.) re
 4.) random
 
 **Data Structures Used**
 1.) List
 2.) Queue using List
 3.) Set
 
 **Sample Input & Output**
 Input - N2
 give the traversal to reach N2 Node
 
 Output - 
 <img width="202" alt="image" src="https://github.com/phaniteja5789/N-AryTree_Pandas/assets/36558484/7c60ef64-2c0d-4a8a-8813-1ce0a6663d97">
 
 Similarly based on the data frame, we can build the N-Ary Graph with n number of children and n number of parents.
 
 
