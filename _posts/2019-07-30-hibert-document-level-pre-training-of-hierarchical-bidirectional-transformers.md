---
layout: post
title: "HIBERT: Document Level Pre-training of Hierarchical Bidirectional Transformers for Document Summarization"
comments: true
description: "Neural extractive summarization models usually employ a hierarchical encoder for document encoding and they are trained using sentence-level labels, which are created
heuristically using rule-based methods. Training the hierarchical encoder with these inaccurate labels is challenging. Inspired by the
recent work on pre-training transformer sentence encoders (Devlin et al., 2018), we propose HIBERT (as shorthand for HIerachical
Bidirectional Encoder Representations from
Transformers) for document encoding and a
method to pre-train it using unlabeled data. We
apply the pre-trained HIBERT to our summarization model and it outperforms its randomly
initialized counterpart by 1.25 ROUGE on the
CNN/Dailymail dataset and by 2.0 ROUGE
on a version of New York Times dataset. We
also achieve the state-of-the-art performance
on these two datasets."
showtags: true
tags: paper-reading nlp document-summarization acl extractive-summarizations
---

### Contribution
- Propose `HIBERT` (HIearchical Bidirectional Encoder Representations from Transofrmaers) for doucment encoding and a method to pre-train it using unlabled data
- Application of HIBERT in document summarization

### A deeper look
#### General model
Choose `transformer` because of its better performance than LSTM in many tasks

#### Problems and solutions

Problem | Solutions
:---: | :---:
Training complex neural models with _inaccuracy binary_ labels | Pretrain the _complex_ part of the extractive model on unlabled data
Previous model focus on pre-train word embeddings or sentence encoders | Concentrate on pre-train the hierachical document encoders (important to summarization)
Considering basic uints of previous model is a word | Pay attention to sentences


#### Model
- Document representation
	- Use two encoders: `sentence encoder` and `document encoder`, both based on `transformer encoder`
- Pre-training
	- Document masking: randomly select 15% of the sentences in document, the mask them with 80%, 10%, and 10% for masked word, no mask, and noices respectively.
	- Sentence prediction: try to predict the masked sentences.
- Extractive summarization
	- Select the most important sentences in a document as its summary.

#### Dataset, evaluations
- Datasets
	- CNN/Dailymail (CNNDM)
	- New York Times (NYT50)
	- GIGA-CM
- Evaluations
	- Reach the state of the art in ROUGE-1, ROUGE-2, ROUGE-L with CNNDM and NYT50

### [Original paper](https://arxiv.org/pdf/1905.06566.pdf)
