---
layout: post
title: "Multi-News a Large-Scale Multi-Document Summarization Dataset and Abstractive Hierarchical Model"
comments: true
description: "Automatic generation of summaries from multiple news articles is a valuable tool as the
number of online publications grows rapidly.
Single document summarization (SDS) systems have benefited from advances in neural encoder-decoder model thanks to the availability of large datasets. However, multidocument summarization (MDS) of news articles has been limited to datasets of a couple
of hundred examples. In this paper, we introduce Multi-News, the first large-scale MDS
news dataset. Additionally, we propose an
end-to-end model which incorporates a traditional extractive summarization model with a
standard SDS model and achieves competitive
results on MDS datasets. We benchmark several methods on Multi-News and release our
data and code in hope that this work will promote advances in summarization in the multidocument setting"
showtags: true
tags: paper-reading acl abstractive-summarization multi-document-summarization nlp
---

### Contribution
- Introduce the first large-scale multi-document summarization [datasets](https://github.com/Alex-Fabbri/Multi-News) in the news domain
- Propose HiMAP model consisting of a [Pointer-Generator Network](https://arxiv.org/abs/1704.04368) and an integrated [MMR module](https://dl.acm.org/citation.cfm?id=291025) 

### A deeper look

Problem | Solutions
:---: | :---:
A lack of datasets for multi-document summarizatoin | Multi-new dataset
Multi-document summarization | Hi-MAP (Hierachical Maximal Marginal Relevance-Attention Pointer-generator) model

#### Hi-MAP model
General picture
[![](/assets/images/20190912-himap-model.PNG)](https://arxiv.org/pdf/1906.01749.pdf)

1. Sentence representation
- Input: $$D = [s_1, s_2, .., s_n]$$ is a collection of sentences from all the source documents, a given sentence $$s_i = [w_{k-m}, w_{k-m+1}, .., w_{k}]$$
- Put all sentences $$s_i$$ with all words $$w_l$$ to *Bi-LSTM (Pointer-generator encoder)* and get $$h_l^w$$ (the word level hidden state of the _l-th_ word). Now we have the word-level sentence embeddings of the document $$h_D^w = [h_{s_1}^w, h_{s_2}^w, .., h_{s_n}^w]$$
- Put the word-level embeddings to a *sentence level LSTM netowrk* to get $$h_D^s = [h_{1}^s, h_{2}^s, .., h_{n}^s]$$, we also put the decoded summary as a single sentence to get the output $$s_sum$$
2. MMR-Attention and MMR-attention Pointer-Generation
They compute MMR scores to rank all sentences from senetence representation $$h_D^s$$ with the query document $$s_sum$$, we then update the word-level attention weights for pointer-generation model using MMR scores


### Comments
- The quality of the ideas
  - They represent the whole summary as a single sentence, but actually it is not. We need to find a better way to display summary representation
- They don't public source code
- Its potential impact
  - Their datasets could leverage the investigation of researchers about the multi-document summarization

### [Original paper](https://arxiv.org/pdf/1906.01749.pdf)
