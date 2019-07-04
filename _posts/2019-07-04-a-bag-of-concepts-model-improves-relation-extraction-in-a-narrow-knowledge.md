---
layout: post
title: "A bag-of-concepts model improves relation extraction in a narrow knowledge domain with limited data"
comments: true
description: "This paper focuses on a traditional relation extraction task in the context of limited annotated 
data and a narrow knowledge domain. They explore this task with a clinical corpus consisting
of 200 breast cancer follow-up treatment letters in which 16 distinct types of relations are
annotated."
showtags: true
tags: paper-reading nlp-biomedical nlp relation-extraction
---

### Contribution
> Proposed two ways to perform `relation extraction` for a `narrow knowledge domain` with only small avaiable data set

### A deeper look
#### Problem
- The SOTA machine learning algorithms may overfit in narrow knowledge domain due to a limited quantity of training instances
- Construction of high-precision rules defining relevant contexts is time-consuming and expensive, requiring extensvie effort from domain expext

#### Solutions

Give two approaches:

1. Typed sentential Co-occurrence, give Window bounded Co-occurrence (WBC) model, is an extension of simple co-occurrence method (same author, published 2 years ago)
	

2. Supervised binary classification

#### Results
- The intra-sentential rule-based approach outperforms the approach which allows for a larger context window
- The supervised learning models outperforms rule-based approaches under $$F_1$$ measure
- BoC features outperform models with BoW, dependency parse, or sentence embedding features
- SVM outperforms complex models such as a feed-forward ANN in our low resource scenario, with less tendency to overfitting

### Limitations or/and Extensions

### My opinion
- The quality of the ideas
- Its potential impact

### [Original paper](https://arxiv.org/abs/1904.10743)