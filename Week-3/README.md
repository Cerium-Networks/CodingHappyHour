# Happy Hour - Week 3

#### *Theme:* 
Data Structures

#### *Challenge:* 
Use immuteable data structures when you can :) 

## Problems

### Warmup

Using this list:
```python
numbers = [1, 5, 2, 4, 7, 21, 6, 6, 15, 15, 42, 1, 2, 8, 12, 2]
```
Take user input for a number (`n`) and remove `n` items from the list. However, numbers **MUST** be removed in order of least to greatest and can **only** print out one time.


### Problem 1

Using a programming language of your choice, write code that reads `animals.txt` into a list, **then** prints the list 

*Challenge:* Print the line number before the animal

*Challenge 2:* Print every other animal

### Problem 2

Using this same list, remove all duplicates **without** iterating over the list. (Hint: Use an alternate data stucture!)

*Challenge:* Do this in one line

### Problem 3

Reading in `animals.csv`, create a dictionary where the key is the animal name and the value is the sound the animal makes

*Challenge:* If there are multiple sounds an animal makes (according to the file), make the 'value' field a list of sounds

*Challenge 2:* Be sure there are no duplicate sounds - note the pig!

### Problem 4

Write a program that reads user input into a **stack**, taking in multiple inputs until they type `PRINT`. If the user types `UNDO`, remove the last item from the stack. 

*Challenge:* Implement a `REDO` feature that allows users to paste back in their `UNDO`'s in order of most recently un-done. 

Ex.

Enter a word(s): a dog
~ ran into
~ the store
~ UNDO
~ the street
~ and found
~ REDO
~ where they ate
~ a cat
~ UNDO
~ a snack
~ UNDO
~ a burger
~ and
~ REDO
~ and
~ REDO
~ PRINT

a dog ran into the street and found the store where they ate a burger and a snack and a cat


### Problem 5

Copy and Paste the following into your code:

```python
exampleGraph = {
    "Item A": [
        "Item A",
        "Item C",
        "Item D",
    ],
    "Item B": [
        "Item D",
        "Item C"
    ],
    "Item C": [
        "Item A",
        "Item B",
        "Item E"
    ],
    "Item D": [
        "Item A",
        "Item B"
    ],
    "Item E": [
        "Item C"
    ]
}
```

Write a program that will take in a 'Start' and an 'End' node, and find a path to connect the two **without any duplicates**.

*Challenge:* Make the above program accomplish the task in the least amount of steps possible


### Notes on Graphs

Graphs can become extremely complex- they are not restricted to the 'Dictionary of Lists' as a saw above- they can be dictionaries of dictionaries of dictionaries of lists, etc. The possibilities are truly endless. Observe the below:

```python
exampleGraph = {
    "Item A": {
        "Neighbors": [
            "Item A",
            "Item C",
        ],
        "IP": "10.10.10.10"
    },

    "Item B": {
        "Neighbors": [
            "Item D",
            "Item C"
        ]
        "IP" : "10.10.10.11",
        "Payload" : {
            "Name" : "Switch B",
            "Data" : "A cool hat"
        }
    },

    "Item C": {
        "Neighbors": [
            "Item A",
            "Item E"
        ]
    },

    "Item D": {
        "Neighbors": [
            "Item A",
            "Item B"
        ]
    }
        
    ],
    "Item E": ]{
        "Neighbors": [
            "Item C",
        ]
    }
}
```
