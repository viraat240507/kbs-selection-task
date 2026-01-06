1. Block Structure: 
a) Each block in my code is created using OOPs concepts in python
b) Each block is an object of class Block and has 6 attributes. These are: Index, Timestamp, Data, Previous Block Hash, Hash, Nonce
c) The block hash is created using SHA-256 algorithm

2. Detection of Tampering by Validation Logic: 
a) We check first of all whether the hash of a previous block is equal to the hash of the new block or not
b) Also, we maintain an additional condition to check whether the hash of the new block hence created is same or not after the block is added and further actions are performed by users on the network
c) Only when these two hashes match, will the new block be added into the blockchain network

3. Proof of Work Approach: 
a) We have created a mine_block function into the class Block
b) There is an argument variable called difficulty inside the above function, which is basically the number of zeroes before the hash of the block, in order for the miners in the network to decode the new hash created
c) Value of the difficulty variable is not set by the users, but by the blockchain algorithm itself to prevenet tampering
d) The effort put in by the miners to decode the new hash code needs to be shown, and it is called "Proof of Work"
e) Here, it is implemented using a while loop which goes on looping unless the new hash contains the required number of starting zeroes or the string needed as decided by the blockchain algorithm
f) This significant effort put in by the crypto miners ensures that Double Spending and Tampering is avoided to the greatest extent