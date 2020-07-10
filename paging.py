# A Python implementation of simulating three page replacement algorithms (LRU, FIFO, OPT)
# Author: Joel Hamilton - University of Cape Town
# CSC3002F Operating Systems Assignment 1 2020

import sys
import random

# This function uses FIFO to determine which page to remove from the memory frames.
def FIFO(size, pages):
    print('Pages in memory after each page use when using FIFO:')
    pageInputOrder = [] # This is a queue to maintain the order of the page sequence so that it is known which page needs to be removed.
    numberOfPageFaults = 0
    pageFrames = [] # This is a list which represents the page frames and the order of all the pages within it.
    for i in range(len(pages)):
        if pages[i] in pageFrames:
            continue
        elif len(pageFrames) < size:
            numberOfPageFaults = numberOfPageFaults+1
            pageInputOrder.append(pages[i])
            pageFrames.append(pages[i])
        else:
            numberOfPageFaults = numberOfPageFaults+1
            pageFrames[pageFrames.index(pageInputOrder[0])] = pages[i]
            pageInputOrder.remove(pageInputOrder[0])
            pageInputOrder.append(pages[i])
        print(pageFrames)
    return numberOfPageFaults

# This function ensures that the page in memory which has been used least recently is the page which is removed.
def LRU(size, pages):
    print('Pages in memory after each page use when using LRU:')
    pageUsageOrder = []
    # The above line initiates a queue to maintain the order of page usage so that it is known which page needs to be removed.
    numberOfPageFaults = 0
    pageFrames = [] # This is a list which represents the page frames and the order of all the pages within it.
    for j in range(len(pages)):
        if pages[j] in pageFrames:
            pageUsageOrder.remove(pages[j])
            pageUsageOrder.append(pages[j])
        elif len(pageFrames) < size:
            numberOfPageFaults = numberOfPageFaults+1
            pageUsageOrder.append(pages[j])
            pageFrames.append(pages[j])
        else:
            numberOfPageFaults = numberOfPageFaults+1
            indexToPutNewPageAt = pageFrames.index(pageUsageOrder[0])
            pageFrames[indexToPutNewPageAt] = pages[j]
            pageUsageOrder.remove(pageUsageOrder[0])
            pageUsageOrder.append(pages[j])
        print(pageFrames)
    return numberOfPageFaults

# This function ensures that the page in memory whose next use is furthest in the future is the page which is removed.
def OPT(size, pages):
    print('Pages in memory after each page use when using OPT:')
    numberOfPageFaults = 0
    pageFrames = [] # This is a list which represents the page frames and the order of all the pages within it.    
    pagesToCome = [] # This is a list which gets shorter and shorter, and only contains which pages are still to be used
    for k in range(len(pages)):
        pagesToCome.append(pages[k])
    for m in range (len(pages)):
        if pages[m] in pageFrames:
            pagesToCome.remove(pages[m])
        elif len(pageFrames) < size:
            numberOfPageFaults = numberOfPageFaults+1
            pagesToCome.remove(pages[m])
            pageFrames.append(pages[m])
        else:
            pagesToCome.remove(pages[m])
            numberOfPageFaults = numberOfPageFaults+1
            listOfUpcomingIndexes = []
            indexToRemove = 0
            for n in range(len(pageFrames)):
                if pageFrames[n] not in pagesToCome:
                    itemToRemove = pageFrames[n]
                    indexToRemove = -1
                else:
                    listOfUpcomingIndexes.append(pagesToCome.index(pageFrames[n]))
            if (len(listOfUpcomingIndexes) > 0) and (indexToRemove != -1):
                indexToRemove = max(listOfUpcomingIndexes)
                itemToRemove = pagesToCome[indexToRemove]
                indexInPageFrameToReplace = pageFrames.index(itemToRemove)
                pageFrames[indexInPageFrameToReplace] = pages[m]
            else:
                pageFrames[pageFrames.index(itemToRemove)] = pages[m]
        print(pageFrames)
    return numberOfPageFaults

# This main function takes in the number of page frames and then generates a page sequence of specified length
# and tests FIFO, LRU, and OPT with this sequence. It then prints out the number of page faults.
def main():
    size = int(sys.argv[1])
    numPages = eval(input('Enter the length of the page reference sequence: \n'))
    pages = []
    for q in range(numPages):
        pages.append(random.randint(0, 9))
    print ('The page sequence being used is:', pages)
    print ('FIFO', FIFO(size, pages), 'page faults.')
    print ('LRU', LRU(size, pages), 'page faults.')
    print ('OPT', OPT(size, pages), 'page faults.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ('Usage: python paging.py', )
    else:
        main()