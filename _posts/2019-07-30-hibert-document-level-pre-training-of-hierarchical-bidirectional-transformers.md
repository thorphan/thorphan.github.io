---
layout: post
title: "HIBERT: Document Level Pre-training of Hierarchical Bidirectional Transformers for Document Summarization (TODO)"
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
> one or two sentence summary of the paper

### A deeper look
- example assumptions made
- arguments presesnted
- data analyzed
- conclusions drawn

### Limitations or/and Extensions

### Comment
- The quality of the ideas
- Its potential impact

### [Original paper](https://arxiv.org/pdf/1905.06566.pdf)
