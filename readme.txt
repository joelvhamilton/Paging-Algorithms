Paging.py is a short python program to model three page replacement algorithms (FIFO, LRU, and OPT). This program can be used for helping students learn how each of these algorithms choose which page to replace given a page fault occurring due to limited memory. 

The program takes in the number of page frames in memory as a command line argument, and then prompts the user to input the length of the page sequence which is going to be used to show how the algorithms work. A page sequence of the specified length is then randomly generated and is printed out for the user's reference, where each page is represented by an integer from 0-9, hence the number of page frames in memory cannot exceed 8, otherwise no page faults will ever occur. The program then executes each algorithm on this sequence and prints out what pages are in memory after each page use.

To use paging.py:

Run the following command:
python3 paging.py <number of frames (any integer from 1-9)>
