USAAR-SemEval-2015
==================

USAAR participation in SemEval2015


The [*Sensible* Hackers](https://sites.google.com/site/usaarhat/) @ Saarland University participated in the following SemEval shared tasks:

 - Task 02 - Semantic Textual Similarity (English) 
 - Task 07 - Diachronic Text Evaluation (Subtask1)
 - Task 17 - Taxonomy Evaluation


Nitty-Gritty (Task 17)
=====
Due to the 4 page limitations of the paper, we were not able to squeeze more information onto Task 17 paper, so here's the As to the Qs that one might have:

**Which system did you submit for the task?**
- We submitted the `is-a` vector based system and then there was some error where the taxonomy ends up without the root and so we have to append our string based model to the final submission so that the evaluation script will work

**What is the string-based system? (since it's not in the paper)**
- It's very much like Els Lefever's Morpho-syntactic analyzer in the LT3 system. 
- We iterate through every possible term pair and then if `term1` is in `term2` and the length of `term1` is more than 3 then we consider `term1` to be a hypernym of `term2`
- See https://github.com/alvations/USAAR-SemEval-2015/blob/master/task17-USAAR-WLV/using_stringdist.py

**How did you build the wikicorpus vectors? Did you tokenize or normalize the text in anyway?**
- We followed the [Emerson et al. (2014)](https://github.com/alvations/SeedLing) to clean and extract a text dump from Wikipedia. Then we extracted all wikipedia articles that contains the our terms in our taxonomy. 
- We single tokenized all the multiword terms, e.g. `hubble space telescope` -> `hubble_space_telescope`. And also `is a` -> `is_a`, before we train a phrasal word2vec model using the wiki articles with `gensim`. 
- So there are many other single-tokenized ngrams that are in the space but they would most probably not mess with the already single-tokenized terms. 

**How many terms weren't found (in the wikidump)?**
- We didn't do a count of how many were found in the wikidump and then built into the space but we can safely treat the number of unique vertices we can extract from the space as the number of terms we found on wiki. 
 - `chemical`: 7177 out of 24816, `WN_chemical`: 891 out of 1444
 - `equipment`: 198 out of 614, `WN_equipment`: 191 out of 486
 - `food`: 869 out of 1586, `WN_food`: 933 out of 1575
 - `science`: 279 out of 464, `WN_science`: 260 out of 451

**Did you only use "is a"? Or did you use any other definitional patterns ("are called", "known as", "a type of", ...)**
- Nope, we use the full wiki articles processed and extracted as described above.

**Did you use any sentence containing "is a" or only sentences containing a SemEval term? or only the first sentence of a Wikipedia article?**
- Yes, we use sentences containing `is_a` as well as all other sentences within the article that contains the term. We use the full article when training our neural net vector space. Our hypothesis is that any words that appears in the same wiki article as the term is somewhat related to it. So training a vector space from the whole article gives denser vectors with more information.





Contributors
====

 - Liling Tan
 - Rohit Gupta (USAAR-WLV) 
 - Carol Scarton (USAAR-SHEFFIELD)
 - Noam Ordan (USAAR-chronos)
 - Josef van Genabith (USAAR-WLV, USAAR-SHEFFIELD)
