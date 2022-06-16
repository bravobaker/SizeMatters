# Absolute Size Experiment
The Absolute Size Hypothesis is formulated as follows: in Archi (also Lak, Tsakhur and Rutul) remarkably small objects go to Gender 4 and/or remarkably big objects go to Gender 3.
 
## How do we test it?
We take a set of concepts that are really big and really small, map them onto words of the 4 languages of our study and retrieve gender values of these words. Then we run Fisher Exact test for every language to test for non-random skewed distribution of big and small above threshold between Gender 3 and Gender 4

## How do we know what is really big and small? 
We use 3 sources of concepts tagged for size:
1. [our own experiment]()
2. [lists of large and small things by McRae et al. 2005]()
3. [dataset by Binder et al. 2016] ()
4. You may find the brief description of every experiment in the respective folders.


__NB!__	To run Fisher-exact test, we did not use all the concepts that are featured in these 3 experimental datasets, but we selected the __median__ as a threshold:
1. Binder et al. 2005 - objects rated at least 1.29/5.83 for ‘big’ and 1.51/5.7 for ‘small’
2. McRae et al. 2005 - objects tagged for size at least 10 times
3. Our own experiment - objects named as small / big more than 2 times 
Here are the p-values:

