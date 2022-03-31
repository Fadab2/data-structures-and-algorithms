# Hashtables
<!-- Short summary or background information -->
Hashtable is a way to store data in a way that retrieving it is very effecient.
This achieved by storing the data in a list using indexes where the index leads to a bucket of that data.

## Challenge
<!-- Description of the challenge -->
Implement a Hashtable Class with the following methods:
set()
get()
contains()
keys()
hash()



## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Started with 1024 indexes list size. To calculate the indexes the corresponding ASCII values of the characters were added, then multiplied by a prime number and then the modulular of that number against the size of list were used as the index.
Generally speaking the Big O is:
Time complexity: O(1)
Space complexity: O(n)

## API
<!-- Description of each method publicly available in each of your hashtable -->
