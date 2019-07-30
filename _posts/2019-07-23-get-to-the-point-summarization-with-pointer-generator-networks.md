---
layout: post
title: "Get To The Point: Summarization with Pointer-Generator Networks"
comments: true
description: "Neural sequence-to-sequence models have
provided a viable new approach for abstractive text summarization (meaning
they are not restricted to simply selecting
and rearranging passages from the original text). However, these models have two
shortcomings: they are liable to reproduce
factual details inaccurately, and they tend
to repeat themselves. In this work we propose a novel architecture that augments the
standard sequence-to-sequence attentional
model in two orthogonal ways. First,
we use a hybrid pointer-generator network
that can copy words from the source text
via pointing, which aids accurate reproduction of information, while retaining the
ability to produce novel words through the
generator. Second, we use coverage to
keep track of what has been summarized,
which discourages repetition. We apply
our model to the CNN / Daily Mail summarization task, outperforming the current
abstractive state-of-the-art by at least 2
ROUGE points."
showtags: true
tags: paper-reading nlp text-summarization abstractive-text-summarization
---

### Contribution
> Illustrate an model that sovles three issues in the context of multi-sentence summaries such as:
>
> 		- inaccurately reproducing factual details
> 		- inability to deal with out-of-vocabulary (OOV) words
> 		- repeating themself

### A deeper look
- Introduce the Pointer-Generator Networks to tackle the incorrect factual details when reproducing words. It is acutally a hybrid network that is able to copy words from source while keeping the ability to generate words.
- Using `coverage` to eliminate repetition in decoder period. It is the attention distribution to keep track of what's been covered so far, and penalize the network for attending to same parts again.

### Limitations or/and Extensions
- Sometimes fails to focus on the `core of the source text`
- `Incorrectly composes fragments` of the source text
- Sometimes `fail to make sense a whole`
- `Need higher-level abstraction` such as more powerful, compressive paraphrasing

### [Original paper](https://arxiv.org/abs/1704.04368) and [blog post](http://www.abigailsee.com/2017/04/16/taming-rnns-for-better-summarization.html)

### Code in [Pytorch](https://github.com/atulkum/pointer_summarizer) and [TensorFlow](https://github.com/abisee/pointer-generator)
