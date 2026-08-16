# CS336 Assignment 1 (Basics) 题目清单

Source: `cs336_assignment1_basics.pdf` (Version 26.0.3, Spring 2026)

本文只整理题目与 Deliverable，方便你自己写答案。提交时需要：

- `writeup.pdf`: Answer all the written questions. Please typeset your responses.
- `code.zip`: Contains all the code you’ve written.
- Optional leaderboard PR.

答题约定：

- **书面题**：在对应「答案」栏填写。
- **实现题**：在「完成情况」栏记录测试、适配器、备注；不要把完整代码贴进本文件。
- 勾选框：`[ ]` 未完成，`[x]` 已完成。

---

## Progress

| # | ID | Title | Points | Type | Done |
|---|----|-------|--------|------|------|
| 1 | `unicode1` | Understanding Unicode | 1 | written | [ ] |
| 2 | `unicode2` | Unicode Encodings | 3 | written | [ ] |
| 3 | `train_bpe` | BPE Tokenizer Training | 15 | code | [ ] |
| 4 | `train_bpe_tinystories` | BPE Training on TinyStories | 2 | experiment / written | [ ] |
| 5 | `train_bpe_expts_owt` | BPE Training on OpenWebText | 2 | experiment / written | [ ] |
| 6 | `tokenizer` | Implementing the tokenizer | 15 | code | [ ] |
| 7 | `tokenizer_experiments` | Experiments with tokenizers | 4 | experiment / written | [ ] |
| 8 | `linear` | Implementing the linear module | 1 | code | [ ] |
| 9 | `embedding` | Implement the embedding module | 1 | code | [ ] |
| 10 | `rmsnorm` | Root Mean Square Layer Normalization | 1 | code | [ ] |
| 11 | `positionwise_feedforward` | Implement the position-wise feed-forward network | 2 | code | [ ] |
| 12 | `rope` | Implement RoPE | 2 | code | [ ] |
| 13 | `softmax` | Implement softmax | 1 | code | [ ] |
| 14 | `scaled_dot_product_attention` | Implement scaled dot-product attention | 5 | code | [ ] |
| 15 | `multihead_self_attention` | Implement causal multi-head self-attention | 5 | code | [ ] |
| 16 | `transformer_block` | Implement the Transformer block | 3 | code | [ ] |
| 17 | `transformer_lm` | Implementing the Transformer LM | 3 | code | [ ] |
| 18 | `transformer_accounting` | Transformer LM resource accounting | 5 | written | [ ] |
| 19 | `cross_entropy` | Implement cross-entropy | 1 | code | [ ] |
| 20 | `learning_rate_tuning` | Tuning the learning rate | 1 | written | [ ] |
| 21 | `adamw` | Implement AdamW | 2 | code | [ ] |
| 22 | `adamw_accounting` | Resource accounting for training with AdamW | 2 | written | [ ] |
| 23 | `learning_rate_schedule` | Implement cosine learning rate schedule with warmup | 1 | code | [ ] |
| 24 | `gradient_clipping` | Implement gradient clipping | 1 | code | [ ] |
| 25 | `data_loading` | Implement data loading | 2 | code | [ ] |
| 26 | `checkpointing` | Implement model checkpointing | 1 | code | [ ] |
| 27 | `training_together` | Put it together | 4 | code | [ ] |
| 28 | `decoding` | Decoding | 3 | code | [ ] |
| 29 | `experiment_log` | Experiment logging | 3 | experiment | [ ] |
| 30 | `learning_rate` | Tune the learning rate | 3 | experiment | [ ] |
| 31 | `batch_size_experiment` | Batch size variations | 1 | experiment | [ ] |
| 32 | `generate` | Generate text | 1 | experiment | [ ] |
| 33 | `layer_norm_ablation` | Remove RMSNorm and train | 1 | experiment | [ ] |
| 34 | `pre_norm_ablation` | Implement post-norm and train | 1 | experiment | [ ] |
| 35 | `no_pos_emb` | Implement NoPE | 1 | experiment | [ ] |
| 36 | `swiglu_ablation` | SwiGLU vs. SiLU | 1 | experiment | [ ] |
| 37 | `main_experiment` | Experiment on OWT | 2 | experiment | [ ] |
| 38 | `leaderboard` | Leaderboard | 6 | experiment | [ ] |

**Total: 109 points**

---

## 2 Byte-Pair Encoding (BPE) Tokenizer

### Problem (unicode1): Understanding Unicode (1 point)

**(a)** What Unicode character does `chr(0)` return?

Deliverable: A one-sentence response.

**答案 (a)：**

```
'\x00'
```

**(b)** How does this character’s string representation (`__repr__()`) differ from its printed representation?

Deliverable: A one-sentence response.

**答案 (b)：**

```
The 'repr' function returns a string to help programmers understand the object.
```

**(c)** What happens when this character occurs in text? It may be helpful to play around with the following in your Python interpreter and see if it matches your expectations:

```python
>>> chr(0)
>>> print(chr(0))
>>> "this is a test" + chr(0) + "string"
>>> print("this is a test" + chr(0) + "string")
```

Deliverable: A one-sentence response.

**答案 (c)：**

```
Its string representation, nothing, string and nothing.
```

---

### Problem (unicode2): Unicode Encodings (3 points)

**(a)** What are some reasons to prefer training our tokenizer on UTF-8 encoded bytes, rather than UTF-16 or UTF-32? It may be helpful to compare the output of these encodings for various input strings.

**Deliverable**: A one-to-two sentence response.

**答案 (a)：**

```
1. The coding shceme of UTF-8 is variable-length and shortest can be 1 byte, so it can save space.
2. Only UTF-8 compatible with ASCII
```

**(b)** Consider the following (incorrect) function, which is intended to decode a UTF-8 byte string into a Unicode string. Why is this function incorrect? Provide an example of an input byte string that yields incorrect results.

```python
def decode_utf8_bytes_to_str_wrong(bytestring: bytes):
    return "".join([bytes([b]).decode("utf-8") for b in bytestring])

>>> decode_utf8_bytes_to_str_wrong("hello".encode("utf-8"))
'hello'
```

Deliverable: An example input byte string for which `decode_utf8_bytes_to_str_wrong` produces incorrect output, with a one-sentence explanation of why the function is incorrect.

**答案 (b)：**

```
The UTF-8 is variable-length coding scheme, so must decode the whole sequence at once, rather than byte by byte.
Here is a conter-example:
>>> decode_utf8_bytes_to_str_wrong("你好".encode("utf-8"))
Traceback (most recent call last):
  File "<python-input-10>", line 1, in <module>
    decode_utf8_bytes_to_str_wrong("你好".encode("utf-8"))
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "<python-input-8>", line 2, in decode_utf8_bytes_to_str_wrong
    return "".join([bytes([b]).decode("utf-8") for b in bytestring])
                    ~~~~~~~~~~~~~~~~~^^^^^^^^^
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe4 in position 0: unexpected end of data
```

**(c)** Give a two-byte sequence that does not decode to any Unicode character(s).

Deliverable: An example, with a one-sentence explanation.

**答案 (c)：**

```
b'\xe4\xbd' (Which is actually obtained through "你好".encode("utf-8")[:2])

```

---

### Problem (train_bpe): BPE Tokenizer Training (15 points)

Deliverable: Write a function that, given a path to an input text file, trains a (byte-level) BPE tokenizer. Your BPE training function should handle (at least) the following input parameters:

**Input**

- `input_path: str` Path to a text file with BPE tokenizer training data.
- `vocab_size: int` A positive integer that defines the maximum final vocabulary size (including the initial byte vocabulary, vocabulary items produced from merging, and any special tokens).
- `special_tokens: list[str]` A list of strings to add to the vocabulary. During training, treat them as hard boundaries that prevent merges across their spans, but do not include them when computing merge statistics.

Your BPE training function should return the resulting vocabulary and merges:

**Output**

- `vocab: dict[int, bytes]` The tokenizer vocabulary, a mapping from int (token ID in the vocabulary) to bytes (token bytes).
- `merges: list[tuple[bytes, bytes]]` A list of BPE merges produced from training. Each list item is a tuple of bytes (`<token1>`, `<token2>`), representing that `<token1>` was merged with `<token2>`. The merges should be ordered by order of creation.

To test your BPE training function against our provided tests, you will first need to implement the test adapter at `adapters.run_train_bpe`. Then, run `uv run pytest tests/test_train_bpe.py`. Your implementation should be able to pass all tests. Optionally (this could be a large time-investment), you can implement the key parts of your training method using some systems language, for instance C++ (consider cppyy or nanobind) or Rust (using PyO3). If you do this, be aware of which operations require copying vs reading directly from Python memory, and make sure to leave build instructions, or make sure it builds using only `pyproject.toml`. Also note that the GPT-2 regex is not well-supported in most regex engines and will be too slow in most that do. We have verified that Oniguruma is reasonably fast and supports negative lookahead, but the regex package in Python is, if anything, even faster.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (train_bpe_tinystories): BPE Training on TinyStories (2 points)

**(a)** Train a byte-level BPE tokenizer on the TinyStories dataset, using a maximum vocabulary size of 10,000. Make sure to add the TinyStories `<|endoftext|>` special token to the vocabulary. Serialize the resulting vocabulary and merges to disk for further inspection. How much time and memory did training take? What is the longest token in the vocabulary? Does it make sense?

Resource requirements: ≤ 30 minutes (no GPUs), ≤ 30 GB RAM

Hint: You should be able to get under 2 minutes for BPE training using multiprocessing during pre-tokenization and the following two facts:

(a) The `<|endoftext|>` token delimits documents in the data files.
(b) The `<|endoftext|>` token is handled as a special case before the BPE merges are applied.

Deliverable: A one-to-two sentence response.

**答案 (a)：**

```
```

**(b)** Profile your code. What part of the tokenizer training process takes the most time?

Deliverable: A one-to-two sentence response.

**答案 (b)：**

```
```

---

### Problem (train_bpe_expts_owt): BPE Training on OpenWebText (2 points)

**(a)** Train a byte-level BPE tokenizer on the OpenWebText dataset, using a maximum vocabulary size of 32,000. Serialize the resulting vocabulary and merges to disk for further inspection. What is the longest token in the vocabulary? Does it make sense?

Resource requirements: ≤ 12 hours (no GPUs), ≤ 100 GB RAM

Deliverable: A one-to-two sentence response.

**答案 (a)：**

```
```

**(b)** Compare and contrast the tokenizer that you get training on TinyStories versus OpenWebText.

Deliverable: A one-to-two sentence response.

**答案 (b)：**

```
```

---

### Problem (tokenizer): Implementing the tokenizer (15 points)

Deliverable: Implement a Tokenizer class that, given a vocabulary and a list of merges, encodes text into integer IDs and decodes integer IDs into text. Your tokenizer should also support user-provided special tokens (appending them to the vocabulary if they aren’t already there). We recommend the following interface:

```python
def __init__(self, vocab, merges, special_tokens=None)
```

Construct a tokenizer from a given vocabulary, list of merges, and (optionally) a list of special tokens. This function should accept the following parameters:

- `vocab: dict[int, bytes]`
- `merges: list[tuple[bytes, bytes]]`
- `special_tokens: list[str] | None = None`

```python
def from_files(cls, vocab_filepath, merges_filepath, special_tokens=None)
```

Class method that constructs and returns a Tokenizer from a serialized vocabulary and list of merges (in the same format that your BPE training code output) and (optionally) a list of special tokens. This method should accept the following additional parameters:

- `vocab_filepath: str`
- `merges_filepath: str`
- `special_tokens: list[str] | None = None`

```python
def encode(self, text: str) -> list[int]
```

Encode an input text into a sequence of token IDs.

```python
def encode_iterable(self, iterable: Iterable[str]) -> Iterator[int]
```

Given an iterable of strings (e.g., a Python file handle), return a generator that lazily yields token IDs. This is required for memory-efficient tokenization of large files that we cannot directly load into memory.

```python
def decode(self, ids: list[int]) -> str
```

Decode a sequence of token IDs into text.

To test your Tokenizer against our provided tests, you will first need to implement the test adapter at `adapters.get_tokenizer`. Then, run `uv run pytest tests/test_tokenizer.py`. Your implementation should be able to pass all tests.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (tokenizer_experiments): Experiments with tokenizers (4 points)

**(a)** Sample 10 documents from TinyStories and OpenWebText. Using your previously-trained TinyStories and OpenWebText tokenizers (10K and 32K vocabulary size, respectively), encode these sampled documents into integer IDs. What is each tokenizer’s compression ratio (bytes/token)?

Deliverable: A one-to-two sentence response.

**答案 (a)：**

```
```

**(b)** What happens if you tokenize your OpenWebText sample with the TinyStories tokenizer? Compare the compression ratio and/or qualitatively describe what happens.

Deliverable: A one-to-two sentence response.

**答案 (b)：**

```
```

**(c)** Estimate the throughput of your tokenizer (e.g., in bytes/second). How long would it take to tokenize the Pile dataset (825GB of text)?

Deliverable: A one-to-two sentence response.

**答案 (c)：**

```
```

**(d)** Using your TinyStories and OpenWebText tokenizers, encode the respective training and development datasets into a sequence of integer token IDs. We’ll use this later to train our language model. We recommend serializing the token IDs as a NumPy array of datatype `uint16`. Why is `uint16` an appropriate choice?

Deliverable: A one-to-two sentence response.

**答案 (d)：**

```
```

---

## 3 Transformer Language Model Architecture

### Problem (linear): Implementing the linear module (1 point)

Deliverable: Implement a Linear class that inherits from `torch.nn.Module` and performs a linear transformation. Your implementation should follow the interface of PyTorch’s built-in `nn.Linear` module, except for not having a bias argument or parameter. We recommend the following interface:

```python
def __init__(self, in_features, out_features, device=None, dtype=None)
```

Construct a linear transformation module. This function should accept the following parameters:

- `in_features: int` final dimension of the input
- `out_features: int` final dimension of the output
- `device: torch.device | None = None` Device to store the parameters on
- `dtype: torch.dtype | None = None` Data type of the parameters

```python
def forward(self, x: torch.Tensor) -> torch.Tensor
```

Apply the linear transformation to the input.

Make sure to:

- subclass `nn.Module`
- call the superclass constructor
- construct and store your parameter as $W$ (not $W^\top$), putting it in an `nn.Parameter`
- of course, don’t use `nn.Linear` or `nn.functional.linear`

For initializations, use the settings from above along with `torch.nn.init.trunc_normal_` to initialize the weights.

To test your Linear module, implement the test adapter at `adapters.run_linear`. The adapter should load the given weights into your Linear module. You can use `Module.load_state_dict` for this purpose. Then, run `uv run pytest -k test_linear`.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (embedding): Implement the embedding module (1 point)

Deliverable: Implement the Embedding class that inherits from `torch.nn.Module` and performs an embedding lookup. Your implementation should follow the interface of PyTorch’s built-in `nn.Embedding` module. We recommend the following interface:

```python
def __init__(self, num_embeddings, embedding_dim, device=None, dtype=None)
```

Construct an embedding module. This function should accept the following parameters:

- `num_embeddings: int` Size of the vocabulary
- `embedding_dim: int` Dimension of the embedding vectors, i.e., $d_{\mathrm{model}}$
- `device: torch.device | None = None` Device to store the parameters on
- `dtype: torch.dtype | None = None` Data type of the parameters

```python
def forward(self, token_ids: torch.Tensor) -> torch.Tensor
```

Lookup the embedding vectors for the given token IDs.

Make sure to:

- subclass `nn.Module`
- call the superclass constructor
- initialize your embedding matrix as an `nn.Parameter`
- store the embedding matrix with the `d_model` being the final dimension
- of course, don’t use `nn.Embedding` or `nn.functional.embedding`

Again, use the settings from above for initialization, and use `torch.nn.init.trunc_normal_` to initialize the weights.

To test your implementation, implement the test adapter at `adapters.run_embedding`. Then, run `uv run pytest -k test_embedding`.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (rmsnorm): Root Mean Square Layer Normalization (1 point)

Deliverable: Implement RMSNorm as a `torch.nn.Module`. We recommend the following interface:

```python
def __init__(self, d_model: int, eps: float = 1e-5, device=None, dtype=None)
```

Construct the RMSNorm module. This function should accept the following parameters:

- `d_model: int` Hidden dimension of the model
- `eps: float = 1e-5` Epsilon value for numerical stability
- `device: torch.device | None = None` Device to store the parameters on
- `dtype: torch.dtype | None = None` Data type of the parameters

```python
def forward(self, x: torch.Tensor) -> torch.Tensor
```

Process an input tensor of shape `(batch_size, sequence_length, d_model)` and return a tensor of the same shape.

Note: Remember to upcast your input to `torch.float32` before performing the normalization (and later downcast to the original dtype), as described above.

To test your implementation, implement the test adapter at `adapters.run_rmsnorm`. Then, run `uv run pytest -k test_rmsnorm`.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (positionwise_feedforward): Implement the position-wise feed-forward network (2 points)

Deliverable: Implement the SwiGLU feed-forward network, composed of a SiLU activation function and a GLU.

Note: in this particular case, you should feel free to use `torch.sigmoid` in your implementation for numerical stability.

You should set $d_{\mathrm{ff}}$ to approximately $\frac{8}{3} \times d_{\mathrm{model}}$ in your implementation, while ensuring that the dimensionality of the inner feed-forward layer is a multiple of 64 to make good use of your hardware. To test your implementation against our provided tests, you will need to implement the test adapter at `adapters.run_swiglu`. Then, run `uv run pytest -k test_swiglu` to test your implementation.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (rope): Implement RoPE (2 points)

Deliverable: Implement a class `RotaryPositionalEmbedding` that applies RoPE to the input tensor.

The following interface is recommended:

```python
def __init__(self, theta: float, d_k: int, max_seq_len: int, device=None)
```

Construct the RoPE module and create buffers if needed.

- `theta: float` $\Theta$ value for the RoPE
- `d_k: int` dimension of query and key vectors
- `max_seq_len: int` Maximum sequence length that will be input
- `device: torch.device | None = None` Device to store the buffer on

```python
def forward(self, x: torch.Tensor, token_positions: torch.Tensor) -> torch.Tensor
```

Process an input tensor of shape `(..., seq_len, d_k)` and return a tensor of the same shape. Note that you should tolerate $x$ with an arbitrary number of batch dimensions. You should assume that the token positions are a tensor of shape `(..., seq_len)` specifying the token positions of $x$ along the sequence dimension.

You should use the token positions to slice your (possibly precomputed) cos and sin tensors along the sequence dimension.

To test your implementation, complete `adapters.run_rope` and make sure it passes `uv run pytest -k test_rope`.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (softmax): Implement softmax (1 point)

Deliverable: Write a function to apply the softmax operation on a tensor. Your function should take two parameters: a tensor and a dimension $i$, and apply softmax to the $i$-th dimension of the input tensor. The output tensor should have the same shape as the input tensor, but its $i$-th dimension will now have a normalized probability distribution. Use the trick of subtracting the maximum value in the $i$-th dimension from all elements of the $i$-th dimension to avoid numerical stability issues.

To test your implementation, complete `adapters.run_softmax` and make sure it passes `uv run pytest -k test_softmax_matches_pytorch`.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (scaled_dot_product_attention): Implement scaled dot-product attention (5 points)

Deliverable: Implement the scaled dot-product attention function. Your implementation should handle keys and queries of shape `(batch_size, ..., seq_len, d_k)` and values of shape `(batch_size, ..., seq_len, d_v)`, where `...` represents any number of other batch-like dimensions (if provided). The implementation should return an output with the shape `(batch_size, ..., seq_len, d_v)`. See Section 3.2 for a discussion on batch-like dimensions. Your implementation should also support an optional user-provided boolean mask of shape `(seq_len, seq_len)`. The attention probabilities of positions with a mask value of `True` should collectively sum to 1, and the attention probabilities of positions with a mask value of `False` should be zero.

To test your implementation against our provided tests, you will need to implement the test adapter at `adapters.run_scaled_dot_product_attention`. `uv run pytest -k test_scaled_dot_product_attention` tests your implementation on third-order input tensors, while `uv run pytest -k test_4d_scaled_dot_product_attention` tests your implementation on fourth-order input tensors.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (multihead_self_attention): Implement causal multi-head self-attention (5 points)

Deliverable: Implement causal multi-head self-attention as a `torch.nn.Module`. Your implementation should accept (at least) the following parameters:

- `d_model: int` Dimensionality of the Transformer block inputs.
- `num_heads: int` Number of heads to use in multi-head self-attention.

Following A. Vaswani et al. [8], set $d_k = d_v = d_{\mathrm{model}} / h$. To test your implementation against our provided tests, implement the test adapter at `adapters.run_multihead_self_attention`. Then, run `uv run pytest -k test_multihead_self_attention` to test your implementation.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (transformer_block): Implement the Transformer block (3 points)

Implement the pre-norm Transformer block as described in Section 3.4 and illustrated in Figure 2. Your Transformer block should accept (at least) the following parameters.

- `d_model: int` Dimensionality of the Transformer block inputs.
- `num_heads: int` Number of heads to use in multi-head self-attention.
- `d_ff: int` Dimensionality of the position-wise feed-forward inner layer.

To test your implementation, implement the adapter `adapters.run_transformer_block`. Then run `uv run pytest -k test_transformer_block` to test your implementation.

Deliverable: Transformer block code that passes the provided tests.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (transformer_lm): Implementing the Transformer LM (3 points)

Time to put it all together! Implement the Transformer language model as described in Section 3.1 and illustrated in Figure 1. At minimum, your implementation should accept all the aforementioned construction parameters for the Transformer block, as well as these additional parameters:

- `vocab_size: int` The size of the vocabulary, necessary for determining the dimensionality of the token embedding matrix.
- `context_length: int` The maximum context length, necessary for determining the dimensionality of the RoPE sin and cos buffer.
- `num_layers: int` The number of Transformer blocks to use.

To test your implementation against our provided tests, you will first need to implement the test adapter at `adapters.run_transformer_lm`. Then, run `uv run pytest -k test_transformer_lm` to test your implementation.

Deliverable: A Transformer LM module that passes the above tests.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (transformer_accounting): Transformer LM resource accounting (5 points)

**(a)** Consider a GPT-2 XL-sized model using our assignment architecture, which has the following configuration:

- `vocab_size`: 50,257
- `context_length`: 1,024
- `num_layers`: 48
- `d_model`: 1,600
- `num_heads`: 25
- `d_ff`: 4,288 (the nearest multiple of 64 to $\frac{8}{3} \times 1{,}600$)

Suppose we constructed our model using this configuration. How many trainable parameters would our model have? Assuming each parameter is represented using single-precision floating point, how much memory is required to just load this model?

Deliverable: A one-to-two sentence response.

**答案 (a)：**

```
```

**(b)** Identify the matrix multiplies required to complete a forward pass of our GPT-2 XL-shaped model. How many FLOPs do these matrix multiplies require in total? Assume that our input sequence has `context_length` tokens.

Deliverable: A list of matrix multiplies (with descriptions), and the total number of FLOPs required.

**答案 (b)：**

```
```

**(c)** Based on your analysis above, which parts of the model require the most FLOPs?

Deliverable: A one-to-two sentence response.

**答案 (c)：**

```
```

**(d)** Repeat your analysis with GPT-2 small (12 layers, 768 `d_model`, 12 heads), GPT-2 medium (24 layers, 1024 `d_model`, 16 heads), and GPT-2 large (36 layers, 1280 `d_model`, 20 heads). As the model size increases, which parts of the Transformer LM take up proportionally more or less of the total FLOPs?

Deliverable: For each model, provide a breakdown of model components and its associated FLOPs (as a proportion of the total FLOPs required for a forward pass). In addition, provide a one-to-two sentence description of how varying the model size changes the proportional FLOPs of each component.

**答案 (d)：**

```
```

**(e)** Take GPT-2 XL and increase the context length to 16,384. How does the total FLOPs for one forward pass change? How does the relative contribution of FLOPs of the model components change?

Deliverable: A one-to-two sentence response.

**答案 (e)：**

```
```

---

## 4 Training a Transformer LM

### Problem (cross_entropy): Implement cross-entropy (1 point)

Deliverable: Write a function to compute the cross-entropy loss, which takes in predicted logits ($o_i$) and targets ($x_{i+1}$) and computes the cross-entropy $\ell_i = -\log \mathrm{softmax}(o_i)[x_{i+1}]$. Your function should handle the following:

- Subtract the largest element for numerical stability.
- Cancel out log and exp whenever possible.
- Handle any additional batch dimensions and return the average across the batch. As with Section 3.2, we assume batch-like dimensions always come first, before the vocabulary size dimension.

Implement `adapters.run_cross_entropy`, then run `uv run pytest -k test_cross_entropy` to test your implementation.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (learning_rate_tuning): Tuning the learning rate (1 point)

As we will see, one of the hyperparameters that affects training the most is the learning rate. Let’s see that in practice in our toy example. Run the SGD example above with three other values for the learning rate: `1e1`, `1e2`, and `1e3`, for just 10 training iterations. What happens with the loss for each of these learning rates? Does it decay faster, slower, or does it diverge (i.e., increase over the course of training)?

Deliverable: A one-to-two sentence response with the behaviors you observed.

**答案：**

```
```

---

### Problem (adamw): Implement AdamW (2 points)

Deliverable: Implement the AdamW optimizer as a subclass of `torch.optim.Optimizer`. Your class should take the learning rate $\alpha$ in `__init__`, as well as the $\beta$, $\varepsilon$ and $\lambda$ hyperparameters. To help you keep state, the base Optimizer class gives you a dictionary `self.state`, which maps `nn.Parameter` objects to a dictionary that stores any information you need for that parameter (for AdamW, this would be the moment estimates). Implement `adapters.get_adamw_cls` and make sure it passes `uv run pytest -k test_adamw`.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (adamw_accounting): Resource accounting for training with AdamW (2 points)

Let us compute how much memory and compute running AdamW requires. Assume we are using float32 for every tensor.

**(a)** How much peak memory does running AdamW require? Decompose your answer based on the memory usage of the parameters, activations, gradients, and optimizer state. Express your answer in terms of the `batch_size` and the model hyperparameters (`vocab_size`, `context_length`, `num_layers`, `d_model`, `num_heads`). Assume $d_{\mathrm{ff}} = \frac{8}{3} \times d_{\mathrm{model}}$.

For simplicity, when calculating memory usage of activations, consider only the following components:

- Transformer block
  - RMSNorm(s)
  - Multi-head self-attention sublayer: $QKV$ projections, $QK^\top$ matrix multiply, softmax, weighted sum of values, output projection.
  - Position-wise feed-forward (SwiGLU): $W_1$, $W_2$, SiLU on the gate branch, element-wise product, $W_3$
- final RMSNorm
- output embedding
- cross-entropy on logits

Deliverable: An algebraic expression for each of parameters, activations, gradients, and optimizer state, as well as the total.

**答案 (a)：**

```
```

**(b)** Instantiate your answer for a GPT-2 XL-shaped model to get an expression that only depends on the `batch_size`. What is the maximum batch size you can use and still fit within 80GB memory?

Deliverable: An expression that looks like $a \cdot \mathrm{batch\_size} + b$ for numerical values $a$, $b$, and a number representing the maximum batch size.

**答案 (b)：**

```
```

**(c)** How many FLOPs does running one step of AdamW take?

Deliverable: An algebraic expression, with a brief justification.

**答案 (c)：**

```
```

**(d)** Model FLOPs utilization (MFU) is defined as the ratio of observed throughput (tokens per second) relative to the hardware’s theoretical peak FLOP throughput [A. Chowdhery et al., 2022]. An NVIDIA H100 GPU has a theoretical peak of 495 teraFLOP/s for “float32” (actually TensorFloat-32, which in reality is “bfloat19”) operations. Assuming you are able to get 50% MFU, how long would it take to train a GPT-2 XL for 400K steps and a batch size of 1024 on a single H100? Following J. Kaplan et al. [25] and J. Hoffmann et al. [26], assume that the backward pass has twice the FLOPs of the forward pass.

Deliverable: The number of hours training would take, with a brief justification.

**答案 (d)：**

```
```

---

### Problem (learning_rate_schedule): Implement cosine learning rate schedule with warmup (1 point)

Write a function that takes $t$, $\alpha_{\max}$, $\alpha_{\min}$, $T_w$ and $T_c$, and returns the learning rate $\alpha_t$ according to the scheduler defined above. Then implement `adapters.get_lr_cosine_schedule` and make sure it passes `uv run pytest -k test_get_lr_cosine_schedule`.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (gradient_clipping): Implement gradient clipping (1 point)

Write a function that implements gradient clipping. Your function should take a list of parameters and a maximum $\ell_2$-norm. It should modify each parameter gradient in place. Use $\varepsilon = 10^{-6}$ (the PyTorch default). Then, implement the adapter `adapters.run_gradient_clipping` and make sure it passes `uv run pytest -k test_gradient_clipping`.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

## 5 Training loop

### Problem (data_loading): Implement data loading (2 points)

Deliverable: Write a function that takes a numpy array $x$ (integer array with token IDs), a `batch_size`, a `context_length` and a PyTorch device string (e.g., `'cpu'` or `'cuda:0'`), and returns a pair of tensors: the sampled input sequences and the corresponding next-token targets. Both tensors should have shape `(batch_size, context_length)` containing token IDs, and both should be placed on the requested device. To test your implementation against our provided tests, you will first need to implement the test adapter at `adapters.run_get_batch`. Then, run `uv run pytest -k test_get_batch` to test your implementation.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (checkpointing): Implement model checkpointing (1 point)

Implement the following two functions to load and save checkpoints:

```python
def save_checkpoint(model, optimizer, iteration, out)
```

should dump all the state from the model, optimizer and iteration into the file-like object `out`. You can use the `state_dict` method of both the model and the optimizer to get their relevant states and use `torch.save(obj, out)` to dump `obj` into `out` (PyTorch supports either a path or a file-like object here). A typical choice is to have `obj` be a dictionary, but you can use whatever format you want as long as you can load your checkpoint later.

This function expects the following parameters:

- `model: torch.nn.Module`
- `optimizer: torch.optim.Optimizer`
- `iteration: int`
- `out: str | os.PathLike | typing.BinaryIO | typing.IO[bytes]`

```python
def load_checkpoint(src, model, optimizer)
```

should load a checkpoint from `src` (path or file-like object), and then recover the model and optimizer states from that checkpoint. Your function should return the iteration number that was saved to the checkpoint. You can use `torch.load(src)` to recover what you saved in your `save_checkpoint` implementation, and the `load_state_dict` method in both the model and optimizer to return them to their previous states.

This function expects the following parameters:

- `src: str | os.PathLike | typing.BinaryIO | typing.IO[bytes]`
- `model: torch.nn.Module`
- `optimizer: torch.optim.Optimizer`

Implement the `adapters.run_save_checkpoint` and `adapters.run_load_checkpoint` adapters, and make sure they pass `uv run pytest -k test_checkpointing`.

**完成情况：**

- Adapter: `[ ]`
- Tests: `[ ]`
- Code location:
- Notes:

```
```

---

### Problem (training_together): Put it together (4 points)

Deliverable: Write a script that runs a training loop to train your model on user-provided input. In particular, we recommend that your training script allow for (at least) the following:

- Ability to configure and control the various model and optimizer hyperparameters.
- Memory-efficient loading of large training and validation datasets with `np.memmap`.
- Serializing checkpoints to a user-provided path.
- Periodically logging training and validation performance (e.g., to console and/or an external service like Weights and Biases).

**完成情况：**

- Script location:
- Notes:

```
```

---

## 6 Generating text

### Problem (decoding): Decoding (3 points)

Deliverable: Implement a function to decode from your language model. We recommend that you support the following features:

- Generate completions for a user-provided prompt (i.e., take in some $x_{1\ldots t}$ and sample a completion until you hit an `<|endoftext|>` token).
- Allow the user to control the maximum number of generated tokens.
- Given a desired temperature value, apply softmax temperature scaling to the predicted next-token distributions before sampling.
- Top-$p$ sampling ([A. Holtzman et al., 2020] also referred to as nucleus sampling), given a user-specified threshold value.

**完成情况：**

- Code location:
- Notes:

```
```

---

## 7 Experiments

### Problem (experiment_log): Experiment logging (3 points)

For your training and evaluation code, create experiment tracking infrastructure that allows you to track your experiments and loss curves with respect to gradient steps and wall-clock time.

Deliverable: Logging infrastructure code for your experiments and an experiment log (a document of all the things you tried) for the assignment problems below in this section.

**答案：**

```
```

---

### Problem (learning_rate): Tune the learning rate (2 B200 hrs) (3 points)

The learning rate is one of the most important hyperparameters to tune. Taking the base model you’ve trained, answer the following questions:

**(a)** Perform a hyperparameter sweep over the learning rates and report the final losses (or note divergence if the optimizer diverges).

Deliverable: Learning curves associated with multiple learning rates. Explain your hyperparameter search strategy.

Deliverable: A model with validation loss (per-token) on TinyStories of at most 1.45

**答案 (a)：**

```
```

**(b)** Folk wisdom is that the best learning rate is “at the edge of stability.” Investigate how the point at which learning rates diverge is related to your best learning rate.

Deliverable: Learning curves of increasing learning rate which include at least one divergent run and an analysis of how this relates to convergence rates.

**答案 (b)：**

```
```

---

### Problem (batch_size_experiment): Batch size variations (1 B200 hr) (1 point)

Vary your batch size all the way from 1 to the GPU memory limit. Try at least a few batch sizes in between, including typical sizes like 64 and 128.

Deliverable: Learning curves for runs with different batch sizes. The learning rates should be optimized again if necessary.

Deliverable: A few sentences discussing your findings on batch sizes and their impacts on training.

**答案：**

```
```

---

### Problem (generate): Generate text (1 point)

Using your decoder and your trained checkpoint, report the text generated by your model. You may need to manipulate decoder parameters (temperature, top-p, etc.) to get fluent outputs.

Deliverable: Text dump of at least 256 tokens of text (or until the first `<|endoftext|>` token), and a brief comment on the fluency of this output and at least two factors which affect how good or bad this output is.

**答案：**

```
```

---

### Problem (layer_norm_ablation): Remove RMSNorm and train (0.5 B200 hrs) (1 point)

Remove all of the RMSNorms from your Transformer and train. What happens at the previous optimal learning rate? Can you get stability by using a lower learning rate?

Deliverable: A learning curve for when you remove RMSNorms and train, as well as a learning curve for the best learning rate.

Deliverable: A few sentences of commentary on the impact of RMSNorm.

**答案：**

```
```

---

### Problem (pre_norm_ablation): Implement post-norm and train (0.5 B200 hrs) (1 point)

Modify your pre-norm Transformer implementation into a post-norm one. Train with the post-norm model and see what happens.

Deliverable: A learning curve for a post-norm Transformer, compared to the pre-norm one.

**答案：**

```
```

---

### Problem (no_pos_emb): Implement NoPE (0.5 B200 hrs) (1 point)

Modify your Transformer implementation with RoPE to remove the position embedding information entirely, and see what happens.

Deliverable: A learning curve comparing the performance of RoPE and NoPE.

**答案：**

```
```

---

### Problem (swiglu_ablation): SwiGLU vs. SiLU (0.5 B200 hrs) (1 point)

Deliverable: A learning curve comparing the performance of SwiGLU and SiLU feed-forward networks, with approximately matched parameter counts.

Deliverable: A few sentences discussing your findings.

**答案：**

```
```

---

### Problem (main_experiment): Experiment on OWT (2 B200 hrs) (2 points)

Train your language model on OpenWebText with the same model architecture and total training iterations as TinyStories. How well does this model do?

Deliverable: A learning curve of your language model on OpenWebText. Describe the difference in losses from TinyStories – how should we interpret these losses?

Deliverable: Generated text from OpenWebText LM, in the same format as the TinyStories outputs. How is the fluency of this text? Why is the output quality worse even though we have the same model and compute budget as TinyStories?

**答案：**

```
```

---

### Problem (leaderboard): Leaderboard (10 B200 hrs) (6 points)

You will train a model under the leaderboard rules above with the goal of minimizing the validation loss of your language model within 0.75 B200-hours.

Deliverable: The final validation loss that was recorded, an associated learning curve that clearly shows a wall-clock-time x-axis that is less than 45 minutes, and a description of what you did. We expect a leaderboard submission to beat at least the naive baseline of a 5.0 loss. Submit to the leaderboard here: https://github.com/stanford-cs336/assignment1-basics-leaderboard

**答案：**

```
```
