# Absolute Size Experiment
The Absolute Size Hypothesis is formulated as follows: in Archi (also Lak, Tsakhur and Rutul) remarkably small objects go to Gender 4 and/or remarkably big objects go to Gender 3.
 
## How do we test it?
We take a set of concepts that are really big and really small, map them onto words of the 4 languages of our study and retrieve gender values of these words. Then we run Fisher Exact test for every language to test for non-random skewed distribution of big and small above threshold between Gender 3 and Gender 4

## How do we know what is really big and small? 
We use 3 sources of concepts tagged for size:
1. [our own experiment](https://github.com/bravobaker/SizeMatters/tree/main/ABSOLUTE%20SIZE%20data/MA%26R)
2. [lists of large and small things by McRae et al. 2005](https://github.com/bravobaker/SizeMatters/tree/main/ABSOLUTE%20SIZE%20data/MCRAE)
3. [dataset by Binder et al. 2016](https://github.com/bravobaker/SizeMatters/tree/main/ABSOLUTE%20SIZE%20data/BINDER)
You may find the brief description of every experiment in the respective folders.


__NB!__	To run Fisher-exact test, we did not use all the concepts that are featured in these 3 experimental datasets, but we selected the __median__ as a threshold:
1. Binder et al. 2005 - objects rated at least 1.29/5.83 for ‘big’ and 1.51/5.7 for ‘small’
2. McRae et al. 2005 - objects tagged for size at least 10 times
3. Our own experiment - objects named as small / big more than 2 times


## data: 

1. [This](https://docs.google.com/spreadsheets/d/1-kcrfq8sUrK-lLhckK7L9J0CwlfeC0Mb/edit#gid=1362841377) is a database of all concepts. 
2. [These](https://docs.google.com/spreadsheets/d/1-poCyGW2NjUhXNxl7BLA6-6E0yjSZYFX/edit#gid=1586497774) are Archi words for these concepts (as an example)


## p-values:

1. _ARCHI_

|                   |                    | 3  | 4  |
|-------------------|--------------------|----|----|
| p-value:  0.012   | MA&R big ARCHI     | 43 | 19 |
|                   | MA&R small ARCHI   | 61 | 63 |
| p-value:  0.2379  | BINDER big ARCHI   | 49 | 22 |
|                   | BINDER small ARCHI | 47 | 33 |
| p-value:   0.0246 | MCRAE big ARCHI    | 17 | 3  |
|                   | MCRAE small ARCHI  | 12 | 12 |

In MA&R and MCRAE datasets size and gender values are not independent

2. _LAK_

|                     |                  | 3  | 4  |
|---------------------|------------------|----|----|
| p-value:   0.008    | MA&R big LAK     | 46 | 14 |
|                     | MA&R small LAK   | 62 | 49 |
| p-value:  0.2379    | BINDER big LAK   | 48 | 14 |
|                     | BINDER small LAK | 44 | 22 |
| p-value:  < 0.00001 | MCRAE big LAK    | 18 | 1  |
|                     | MCRAE small LAK  | 3  | 24 |

In MA&R and MCRAE datasets size and gender values are not independent

3. _RUTUL_

|                     |                    | 3  | 4  |
|---------------------|--------------------|----|----|
| p-value:   0.4387   | MA&R big RUTUL     | 37 | 27 |
|                     | MA&R small RUTUL   | 86 | 49 |
| p-value:  0.6291    | BINDER big RUTUL   | 52 | 28 |
|                     | BINDER small RUTUL | 51 | 33 |
| p-value:  < 0.00001 | MCRAE big RUTUL    | 1  | 19 |
|                     | MCRAE small RUTUL  | 26 | 5  |


In MCRAE dataset size and gender values are not independent but in the unexpected way

4. _TSAKHUR_

|                   |                      | 3  | 4  |
|-------------------|----------------------|----|----|
| p-value:  0.2903. | MA&R big TSAKHUR     | 35 | 36 |
|                   | MA&R small TSAKHUR   | 68 | 49 |
| p-value:  1       | BINDER big TSAKHUR   | 40 | 36 |
|                   | BINDER small TSAKHUR | 41 | 36 |
| p-value:  0.1107  | MCRAE big TSAKHUR    | 3  | 15 |
|                   | MCRAE small TSAKHUR  | 11 | 29 |  
