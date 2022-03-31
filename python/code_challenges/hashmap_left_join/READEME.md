# Challenge
<!-- Short summary or background information -->
Write a function called left join that takes in two hash maps.

the first parameter is a hashmap that has words as keys and a synonym of the key as values.
The second parameter is a hashmap that has words  as keys and antonyms of the keys.

![white board](../hashmap-left-join/hashmap-left-join.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Loop through the left hashmap, add it to the list as key value pairs. Add the value of the matching keys on the right to the list. One for loop that goes through all the items and stores them so we have O(n).

Big O
Time complexity: O(n)
Space complexity: O(n)

## API
<!-- Description of each method publicly available in each of your hashtable -->
