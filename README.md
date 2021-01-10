###############################################################
Problem 1: LRU Cache
Explanation

Design Decisions:
LRU Cache is the ejecting of the Least recently used element fromt he cache(Datastructure) when the new element is added into it. 
I have utilised OrderedDict as the Datastructure for the cache as it preserves the order when the keys are inserted,by contrast A regular dictionary doesn't keep track of the insertion order,and iterating it gives the values in arbitrary order.

Time complexity: 
O(1) because each time an item is accessed we are only getting a specfic key in the cache and updating the cache takes O(1) time.

Space complexity: 
O(n) because we have to keep track of n elements in the Ordered Dictionary.
###############################################################


###############################################################
Problem 2:File Recursion 
Explanation

Design Decisions:
Implemented a recursive function call to find all the files in the directories and the underlying sub directories.

Time complexity: 
O(n) because the fuction is being called recursively n times before reaching the base case.

Space complexity: 
O(n) because we use list to store the values.
###############################################################


###############################################################
Problem 3:Huffman Coding 
Explanation

Design Decisions:
1) Created a Freq table of all the characters and their associated freq of occurence.
2) Sorted the table to make it easier to fetch the least frequent character each time. I have used a list to accomplish this.
3) Pop two least frequent characters from the list and merge them into one node and assign the sum of freq of these two child 
   nodes to the parent node.
4) We keep repeating the process until we run out of characters and the final node becomes the root of the tree.

Time complexity: 
O(n^2) because we have two nested lists that run in a quadratic time complexity.

Space complexity: 
O(n) because we use list to store the values.
###############################################################


###############################################################
Problem 4:Active Directory
Explanation

Design Decisions:
Implemented a recursive function call to find a user exists in the parent group and the underlying child and sub child groups.

Time complexity: 
O(n) because the function is being called recursively n times before reaching the base case.

space complexity: 
O(1) because we are only checking if it is true or not.
###############################################################


###############################################################
Problem 5:Blockchain
Explanation

Design Decisions:
The bLock chain is a listed link of blocks, each block cointains an array of transactions. The first block will have all the values except the previous Hash which will be 0. The next block will have the values with the previous first hash stored and at the end all the Block values are appended to a list.  


Time complexity: 
O(1) because as we are using Hash function to store the data.

Space complexity: 
O(n) because we use are using a list to store the Block values.
###############################################################


###############################################################
Problem 6:Union and Intersection
Explanation

Design Decisions:
Union Function: Uses Set Union function to adds all values from llist1 and llist2 to the set, which doesn't allow for duplicates. Then transfers the values to a linked list.
Intersection Function : Uses Set Intersection function to get the matched values from the two lists, Then transfers the values to a linked list.

Time complexity: 
O(n) because in both the functions we iterate over all the elements in the lists.

Space complexity: 
O(n) because we use list to store the values.
###############################################################




