
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

**What are the limitations of your system?**
- As one of the sharp reviewers of our paper pointed out, we basically have a hyper-hyponym pair generator instead of real taxonomy builder. The reviewer:
 - *the task is to build a taxonomy. In the paper, nothing is talked about the strategy to structure the semantic space. Once hypernym/hyponyms pairs have been discovered, how terms are structured. If there is a link between each word pair, there may exist many cycles and too many edges which would render a useless taxonomy. Here the authors should clearly explain there strategy as it is the aim of the SEMEVAL contest. For example, some simple problems can occur. If "food" is the root of the taxonomy, the authors may calculate: v(food) op v(is-a_food). Then what is the root of the root? The authors will find a candidate in the space, which of course will be wrong. How do they deal with this simple problem?"*
- That was one of the problem that occurred during evaluation and we couldn't resolve the problem of the top of the domain ontology not linking to anything so our initial strategy was to ignore the entity at the top of the ontology since the TOP of all ontology should ideally be linked to nothing.
- But we're talking about sub-taxonomy of a specific domain here so our solution was just to link the top of the domain to `entity` concept or to its hypernym concept as per Wordnet.
- As highlighted in the paper our concern for pure hyper-hyponym pairs has caused the multi-inner cycles and low F&M scores, so the only resolution that we could see is to map all hyper-hyponym pairs onto a graph and then prune the graph to get an ontology with minimal cycles. 
- Still we think that the entity-relation-entity triplet (in this case hyper-hyponyms) generation approach is useful for the taxonomy induction without caring about the top node because we dont really need to know that food->entity since it should be a given, the edges between the food terms and which term is the most "hyper-food" connecting to food is more important. Also this is scalable to other relation to build a other knowledge bases rahter than hierarchical ontology
 
 

