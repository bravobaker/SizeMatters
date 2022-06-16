# CATEGORIAL SIZE EXPERIMENT

In this experiment we test for the __Categorial Size Hypothesis.__ It is formulated as follows: in Archi (also Lak, Tsakhur and Rutul) within specific conceptual categories, small objects go to Gender 4 and/or big objects go to Gender 3. Here we probe for semantic categories of BIRDS, ANIMALS, WILD ANIMALS, BODYPARTS, TOOLS. 

Overall procedure looks like this: we take Kibrik & Kodzasov «Imya» Thesaurus (1990?) and retrieve all the members of the respective semantic categories. Then we assign size values to the concepts within a given category: we try to find out how different members of BIRDS/TOLLS/etc. are related to each others size-wisely. To do so we run our card-sorting experiment:


## CARD-SORTING
We asked participants to group together members of a given category on the grounds of their similarity in size and give a name to each of the group. Cards for every semantic category are evaluated by 10 participants. For every collected answer, we ranked the groups in accordnce with their names and assigned all members of a group to one size value with respect to group's rank. Next, we took the mean value for every concept and compiled these mean values into the intra-categorial scale. At this point we got 5 scales of concepts for 5 semantic categories. Within every scale concepts are ranked on the grounds of their size scores. Then we translated concepts into 4 languages and retrieved gender values of every word in a given language. At this point, for every language, we got 5 databases of this kind:

| concept | size value | word | gender value |
|---------|------------|------|--------------|

In the end, we run Mann-Whitney U test to check for above-random separation (mutual displacement) in the ordering of two samples (gender 3 nouns and gender 4 nouns) along a scale:

![](mann_whitney_u.png)

## In this folder you may find:

1. sets of concepts that we used together with their aggregated ranks: [this is a user-friendly googleshit](https://docs.google.com/spreadsheets/d/1iyhobgl_OLAbf6Jxh0p7683mJyM9ZTA-PoJPzS3DaZU/edit#gid=588242402). You can sort it and see the how members of a given category align into a scale. 
2. all the produced rankings before the aggregation: [this is a user-frienfly google sheet](https://docs.google.com/spreadsheets/d/1lqKpp8eTUgpMqK0UJmE1mrqHaKqMkXKCQswXnRumGbs/edit#gid=640697967). You can filter it by _user id_ to see what the actual category labels were, before we turned them into ranks. 


## These are the p-values that we got:

1. __ARCHI__

BIRDS: gender 3 is bigger, p-value: 0.005622733175078314

BODYPARTS: there is no significant difference, p-value: 0.8277382910534468

TOOLS: gender 4 is bigger, p-value: 0.006927526368356346

ANIMALS: gender 3 is bigger, p-value: 0.018023701756087862

WILD ANIMALS: there is no significant difference, p-value: 0.05976215381948469



2. __LAK__ (all ANIMALS and BIRDS go gender 3)

BODYPARTS: there is no significant difference, p-value: 0.1831870613765758

TOOLS: there is no significant difference, p-value: 0.4644182618953264 



3. __RUTUL__ (all ANIMALS and BIRDS go gender 3)

BODYPARTS: there is no significant difference, p-value: 0.15060528553926286

TOOLS: there is no significant difference, p-value: 0.10516742324521319



4. __TSAKHUR__ (all BIRDS are gender 3)

WILD ANIMALS: there is no significant difference, p-value: 0.8736424410187432

ANIMALS: there is no significant difference, p-value: 0.13939509407377476

TOOLS: there is no significant difference, p-value: 0.7320931128468913

BODYPARTS: there  is no significant difference, p-value: 0.05976215381948469


