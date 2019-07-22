---
layout: post
title: "Text Summarization Techniques: A Brief Survey"
comments: true
description: "In recent years, there has been an exploision in the amount of text data from a variety of sources.
This volumes of text is an invaluable source of information and knowledge which needs to be effectively summarized to be useful."
showtags: true
tags: paper-reading nlp text-summarization
---

### Contribution
> Review the dissimilar processess for summarization and illustrate the effectiveness and shortcomings of different methods

### A deeper look
#### General problem
- People are overwhelmed by the massive information from media and internet which need to be compelling summarized to be fruitful. That's why we need `automatic text summarization` which is the task of producing a succint, concise and fluent summary while preserving the key information content and overall meaning. 


- ***Key phrases*** method:
	1. Cue method: the presence or absence of certain cue words in cue dictionary
	2. Title method: the sum of all content words appearing in the title and the headings of a text
	3. Location method: sentences appearing in the beginning of the document as well as the beginning of paragraphs have a higher probability of being relevant.

- Two different approaches to text summarization:
	- `Extractive summarization` (this paper is working on) identify the important sentences, sections, words and generating them verbatim
	- `Abstractive summarization` generates important material in a new way

#### Extractive summarization techniques
`Intermediate representation`: create some intermediate representation of text, then try to summarize the salient content from the representation
	- topic representation
	- indicator representation 

`Sentence Score`: after generating the intermediate representation, we assign to each sentence the *important score* which is computed by aggregating evidence from different indicator found by the machine learning approach.

`Summary sentences selection`: select top *k most important* sentences to produce a summary.

#### Topic representation approaches
- Topic words: identify words that desribe the topic of input document
	1. Using frequency thresholds
	2. Log-likelihood ratio test to indentify `topic signature`
- Frequency-driven approaches
	1. Word probability
		- Disavantage: must decide the top words list (not very straight forward task)
	2. TF/IDF (Term Frequency - Inverse Document Frequency)
		- Advantage: assess the importance of words and identify the common words in the documents
		- The weigth of each word *w* in the document *d* is computed as follows: $$q(w) = f_{d}(w) * \log \frac{\mid D \mid}{f_{D}(w)}$$
	3. Centroid-base summarization
- Latent Semantic Analysis: an unsupervised method for extracting a representation of text semantics based on observed words
	- Disadvantage: a topic may need more than one sentenct to conveys its information
	- Enhancement: LSA-based method to leverage the weight function: $$g(s_i) = \sqrt{\sum_{j=1}^{m}d_{ij}^2}$$
- Bayesian Topic Models
	- Kullbak-LIebler (KL) divergence
	- Latent Dirichlet Allocation (LDA) - extensively used for `multi-document summarization` recently

#### Knowledge bases and automatic summarization
- The need of considering knowledge bases (semantic-based or ontology-based summarizers)
- Email summarization

#### The impact of context in summarization
- Web summarization
- Scientific articles summarization

#### Indicator representation approaches
- Graph methods for summarization: influenced by PageRank algorithm, represent the documents as a connected graph
- Machine learning for summarization: 
	1. Bayes's rule: $$P\left(s \in \mathcal{S} \mid F_{1}, F_{2}, \ldots, F_{k}\right)=\frac{P\left(F_{1}, F_{2}, \ldots, F_{k}\right) \mid s \in \mathcal{S} ) P(s \in \mathcal{S})}{P\left(F_{1}, F_{2}, \ldots, F_{k}\right)}$$
		- $$s$$ is a sentence from the document collection
		- $$F_1, F_2, ..., F_k$$ are features used in classification
		- $$\mathcal{S}$$ is the summary to be generated
	2. Disadvantage: supervised learning needs a lot of training document with labeled data
	3. Alternatives:
		- Annotated corpora creation
		- Semi-supervised approaches

#### Evaluation
- Evaluation of automatically produced summaries
	1. Method
		1. SUMMAC
		2. DUC (the document understanding conference)
		3. TAC (Text Analysis Conference)
	2. Difficulties:
		1. Decide and specify the most important parts of the original text to preserve.
		2. Identify these pieces of important information in the candidate summary.
		3. The readability of the summary in terms of grammatically and coherence has to be evaluated.
- Human evaluation
- Automatic evaluation methods
	1. ROUGE (Recall Oriented Understudy for Gisting Evaluation)
		- ROUGE-n: recall-based measure and based on comparision of n-grams. The score is computed as: $$ROUGE-n = \frac{p}{q}$$
		- ROUGE-L: employes the concept of *longest common subsequence* (LCS)
		- ROUGE-SU: skip bi-gram and uni-gram
		
### [Original paper](https://arxiv.org/abs/1707.02268)