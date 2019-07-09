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

### Limitations or/and Extensions

### My opinion
- The quality of the ideas
- Its potential impact

### [Original paper](https://arxiv.org/abs/1707.02268)