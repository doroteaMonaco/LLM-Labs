# Large Language Models for Software Engineering - Lab Series

This repository contains a comprehensive series of laboratory exercises exploring the application of **Large Language Models (LLMs)** to software engineering tasks. The labs progress from foundational concepts to advanced multi-agent scenarios.

---

## 📚 Table of Contents

1. [Lab 01](#lab-01--transformer-architectures)
2. [Lab 02](#lab-02--attention-mechanisms)
3. [Lab 03](#lab-03--transformer-based-models)
4. [Lab 04](#lab-04--language-model-fine-tuning)
5. [Lab 05](#lab-05--model-optimization)
6. [Lab 06](#lab-06--prompt-engineering--rag)
7. [Lab 07](#lab-07--fine-tuning-on-domain-data)
8. [Lab 08](#lab-08--routing-and-model-selection)
9. [Lab 09](#lab-09--code-generation)
10. [Lab 10](#lab-10--test-generation)

---

## Lab 01 – Transformer Architectures

**Objective:** Understand the foundational architecture of Transformer models and their key components.

**Key Topics:**
- Transformer architecture overview
- Self-attention mechanisms
- Multi-head attention
- Feed-forward networks
- Positional encodings
- Layer normalization

**Hands-On Activities:**
- Implement basic Transformer components
- Analyze attention patterns
- Study model scaling effects

**Deliverables:**
- `solution.ipynb` - Complete implementation and analysis
- `text.ipynb` - Guided exercises with explanations

---

## Lab 02 – Attention Mechanisms

**Objective:** Deep dive into attention mechanisms and their variations.

**Key Topics:**
- Scaled dot-product attention
- Multi-head attention computation
- Query, Key, Value (QKV) framework
- Attention visualization
- Cross-attention vs Self-attention
- Attention variants (sparse, linear, etc.)

**Exercises:**
1. **T5-Based Attention** (`solution-01-t5.ipynb`)
   - Sequence-to-sequence attention
   - Encoder-decoder architecture
   - Attention weight analysis

2. **Advanced Attention** (`solution-02-attention.ipynb`)
   - Custom attention implementations
   - Efficiency improvements
   - Attention head visualization

**Outputs:**
- Attention heatmaps
- Performance comparisons
- Architecture diagrams

---

## Lab 03 – Transformer-Based Models

**Objective:** Explore pre-trained Transformer models (BERT, GPT-2) and their applications.

**Key Topics:**
- BERT architecture and bidirectional context
- GPT-2 autoregressive modeling
- Tokenization strategies
- Embedding layers
- Model fine-tuning basics

**Exercises:**
1. **BERT Analysis** (`solution-01-bert.ipynb`)
   - Token embeddings and attention patterns
   - Classification head adaptation
   - Contextual representation analysis

2. **GPT-2 Exploration** (`solution-02-gpt2.ipynb`)
   - Text generation patterns
   - Temperature and sampling effects
   - Prompt sensitivity analysis

**Results Saved:** `results/` directory

---

## Lab 04 – Language Model Fine-Tuning

**Objective:** Learn to adapt pre-trained models to specific domains through fine-tuning.

**Key Topics:**
- Transfer learning principles
- Fine-tuning strategies
- Causal Language Modeling (CLM)
- Domain adaptation
- Evaluation metrics for language models

**Exercises:**
1. **Causal Language Modeling (CLM)** (`solution-01-clm.ipynb`)
   - Next token prediction
   - Fine-tuning on custom datasets
   - Perplexity computation

2. **Advanced LLM Fine-Tuning** (`solution-02-llms.ipynb`)
   - Large language model adaptation
   - Multi-step fine-tuning
   - Domain-specific optimization

**Artifacts:**
- `gpt2-medical-finetuned/` - Fine-tuned model checkpoint

---

## Lab 05 – Model Optimization

**Objective:** Implement techniques to reduce model size and improve inference efficiency.

**Key Topics:**
- Model quantization (INT8, FP16)
- LoRA (Low-Rank Adaptation)
- Parameter-efficient fine-tuning
- Memory and computational efficiency
- Inference optimization

**Exercises:**
1. **Quantization** (`solution-01-quantization.ipynb`)
   - 8-bit quantization
   - Mixed precision training
   - Inference speed vs accuracy trade-offs

2. **LoRA Fine-Tuning** (`solution-02-LoRA.ipynb`)
   - Low-rank decomposition
   - Parameter reduction
   - Training efficiency improvements

**Checkpoints:** `results/checkpoint-63/`

---

## Lab 06 – Prompt Engineering & RAG

**Objective:** Master advanced prompting techniques and Retrieval-Augmented Generation (RAG).

**Key Topics:**
- Prompt engineering best practices
- Few-shot learning
- Chain-of-thought reasoning
- Retrieval-Augmented Generation (RAG)
- Vector embeddings and similarity search

**Exercises:**
- Prompt design optimization
- RAG pipeline implementation
- Context retrieval strategies
- Evaluation of generated responses

**Skills Developed:**
- Effective prompt construction
- Integration of external knowledge
- Grounding LLM outputs with factual data

---

## Lab 07 – Fine-Tuning on Domain Data

**Objective:** Adapt LLMs to specific domains using domain-specific datasets.

**Content:**
- `stories.csv` - Dataset of narrative texts
- Story-based fine-tuning
- Domain adaptation evaluation

**Key Activities:**
- Data preprocessing and tokenization
- Fine-tuning on story generation
- Evaluation of domain-specific outputs
- Comparison with base models

---

## Lab 08 – Routing and Model Selection

**Objective:** Implement intelligent routing mechanisms to select optimal models for different tasks.

**Key Topics:**
- Multi-model systems
- Routing algorithms
- Task-specific model selection
- Cost-performance optimization
- Load balancing

**Exercises:**
- Design efficient routing policies
- Implement multi-model inference
- Evaluate routing effectiveness
- Optimize resource utilization

---

## Lab 09 – Code Generation

**Objective:** Use LLMs to automatically generate code from natural language specifications.

**Architecture Overview:**

```
Requirement Specification
    ↓
[Multiple LLM Agents]
├── GPT (Reference)
├── CodeLlama (7B)
├── Phi-2 (2.7B)
└── StarCoder (6.7B)
    ↓
Code Generation
    ↓
Parsing & Cleaning
    ↓
Test Suite Execution
    ↓
[Quality Metrics]
├── Functional Correctness (Pass Rate)
├── Cyclomatic Complexity (CC)
├── Maintainability Index (MI)
├── Lines of Code (LOC)
└── Code Comments
    ↓
Comparative Analysis & Visualization
```

**Key Components:**

### Step 1: Define Requirements
Specify software requirements (e.g., "compute average grade excluding best and worst")

### Step 2: Create Test Suite
Design comprehensive test cases covering:
- Valid inputs (normal cases, boundary values)
- Invalid inputs (type errors, constraint violations)
- Edge cases (all same values, empty lists, etc.)

**Example Test Case:**
```python
def test_compute_average_valid():
    assert compute_average([18, 25, 30, 33, 22, 28]) == 26.25
    
def test_compute_average_invalid_length():
    with pytest.raises(ValueError):
        compute_average([18, 25, 30])
```

### Step 3: Generate Code with LLMs
Use different models to generate implementations:
- Prompt: Structured requirement + examples + function signature
- Models: GPT, CodeLlama, Phi-2, StarCoder
- Output: Raw generated code with potential artifacts

### Step 4: Parse Generated Code
Extract clean Python functions from model output (remove markdown, explanations, duplicates):
```python
clean_code = code.replace("```python", "").replace("```", "").strip()
```

### Step 5: Execute Tests
Run test suite against generated code:
- Count passing tests
- Calculate functional correctness ratio
- Record failures and errors

### Step 6: Quality Analysis with Radon
Compute static code quality metrics:
- **Cyclomatic Complexity:** Measures code branching complexity
- **Maintainability Index:** Overall maintainability score (0-100)
- **Lines of Code:** Code length
- **Comment Density:** Proportion of comments

### Step 7: Comparative Analysis
Compare models on:
- Functional correctness (% of tests passing)
- Code quality metrics
- Model efficiency (inference time, memory)
- Code readability and style

**Exercise 1 Example:**
```
Model          Correctness    CC    MI     LOC    Comments
─────────────────────────────────────────────────────────
GPT            100%           2     95.2   24     3
CodeLlama      85%            1     77.2   5      0
Phi-2          80%            1     81.5   6      1
```

### Step 8: Visualization
Generate comparative bar charts for:
- Cyclomatic Complexity
- Maintainability Index
- Lines of Code
- Functional Correctness

### Exercise 2: Multi-Model Comparison
Compare additional models:
- Qwen, Mistral, LLaMA variants
- Analyze trade-offs between accuracy and efficiency

### Exercise 3: Complex Functions
Apply methodology to more complex requirements:
1. **Railway Pricing Function**
   - Multi-condition logic
   - Group eligibility rules
   - Price calculations

2. **Bike Race Timing Function**
   - Conditional time multipliers
   - Speed-based thresholds
   - Category-dependent rules

**Insights:**
- How model accuracy decreases with requirement complexity
- Impact of code length on generation quality
- Importance of clear specifications and examples

---

## Lab 10 – Test Generation

**Objective:** Use LLMs to automatically generate comprehensive test cases for existing code.

**Key Difference from Lab 09:**
- Lab 09: Generate code from specs, test with existing tests
- Lab 10: Generate tests from existing code

**Workflow:**

```
Existing Reference Implementation
    ↓
[Multiple LLM Agents]
├── CodeLlama
├── GPT
├── Phi-2
└── Other Models
    ↓
Test Case Generation
    ↓
Test Execution
    ↓
[Quality Metrics]
├── Pass Rate (% of passing tests)
├── Code Coverage
├── Mutation Score
└── Test Quality
    ↓
Comparative Analysis
```

**Key Concepts:**

### Step 1: Reference Code
Start with validated reference implementation (e.g., `racer_disqualified` function)

### Step 2: Manual Test Baseline
Define reference test cases with pytest:
```python
def test_valid_racer():
    assert not racer_disqualified([120, 110, 90], [100, 100, 100], 2, [20, 10])

def test_disqualified_excessive_time():
    assert racer_disqualified([160, 200, 90], [100, 100, 100], 4, [50, 60, 70, 10])
```

### Step 3: Compute Baseline Metrics

**Pass Rate:**
- Ratio of passing tests to total tests
- Measure: Do generated tests correctly validate the code?

**Code Coverage:**
- Tool: `coverage` library
- Measures: % of code lines/branches executed
- Target: ≥90% coverage for quality test suites

```python
coverage run -m pytest test_file.py
coverage report -m
```

### Step 4: Mutation Testing

**Concept:** Introduce intentional bugs (mutations) to verify test quality

**Example Mutations:**
```python
# Original:
if penalty > 100:
    disqualified = True

# Mutant 1 - Change operator:
if penalty < 100:
    disqualified = True

# Mutant 2 - Change value:
if penalty > 50:
    disqualified = True

# Mutant 3 - Remove condition:
# (skip the entire check)
```

**Mutation Analysis:**
- **Killed Mutant:** Test detected the bug (test failed) ✅
- **Survived Mutant:** Test missed the bug (test passed) ❌

**Mutation Score:** Killed Mutants / Total Mutants

Example Results:
```
Mutant 1 (penalty < 100) → KILLED (test caught the change)
Mutant 2 (penalty > 50)  → KILLED (test caught the change)
Mutant 3 (remove check)  → KILLED (test caught the change)
─────────────────────────────────────────────────────
Mutation Score: 3/3 = 100% (excellent test quality)
```

### Step 5: LLM Test Generation
Generate test suites using different LLMs:
- Provide: Function signature, requirements, example test
- Output: Complete test file
- File names: `test_function_01_gpt.py`, `test_function_01_llama.py`

### Step 6: Evaluate Generated Tests

For each LLM-generated test suite:
1. **Execute tests** - Are they syntactically correct?
2. **Calculate pass rate** - Do tests actually test the code?
3. **Measure coverage** - What % of code is covered?
4. **Run mutation analysis** - What mutation score?

### Step 7: Comparative Analysis

```
Model      Tests    Pass Rate    Coverage    Mutation Score    Quality
──────────────────────────────────────────────────────────────────────
Reference  14       100%         95%         100%              Excellent
GPT        18       94%          92%         85%               Very Good
CodeLlama  12       100%         78%         60%               Fair
Phi-2      15       88%          85%         70%               Good
```

**Key Metrics:**
- **Test Effectiveness:** Do generated tests catch bugs?
- **Coverage Adequacy:** Do tests exercise all code paths?
- **Efficiency:** Number of tests to achieve good coverage

**Insights:**
- Which LLM generates highest-quality tests?
- Trade-off between test count and quality
- Cost-benefit of automated test generation
- Impact of code complexity on test generation

---

## 🛠️ Technology Stack

### Core Libraries
- **PyTorch** 2.7.1+cu118 - Deep learning framework
- **Transformers** 4.57.1 - HuggingFace model library
- **CUDA** 11.8 - GPU acceleration

### Testing & Analysis
- **pytest** 9.0.1 - Test framework
- **ipytest** 0.14.2 - Jupyter-integrated testing
- **coverage** - Code coverage measurement
- **radon** - Code quality metrics
  - Cyclomatic Complexity
  - Maintainability Index
  - Raw metrics (LOC, comments)

### Utilities
- **matplotlib** - Visualization
- **numpy** - Numerical computing
- **pandas** - Data manipulation

---

## 🚀 Getting Started

### Prerequisites
```bash
# Python 3.11+
python --version

# GPU setup (CUDA 11.8)
nvidia-smi
```

### Installation
```bash
# Clone repository
git clone <repo_url>
cd LLM-Labs

# Install dependencies
pip install -r requirements.txt

# Or install individually:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers pytest ipytest coverage radon matplotlib numpy pandas
```

### Running Labs
```bash
# Navigate to lab directory
cd lab09  # or lab10, etc.

# Open Jupyter notebook
jupyter notebook text-09-code-generation.ipynb

# Or use VS Code with Jupyter extension
code text-09-code-generation.ipynb
```

---

## 📊 Key Findings & Insights

### Lab 09 - Code Generation Insights

1. **Model Trade-offs:**
   - Larger models (13B) → Higher accuracy but more memory
   - Smaller models (2-7B) → Efficient but potentially less accurate
   - Specialized models (CodeLlama) > General models for code

2. **Code Quality:**
   - LLM-generated code often lacks error checking
   - Comments and documentation vary significantly
   - Functional correctness ≠ High-quality code

3. **Requirement Complexity:**
   - Simple functions: >90% accuracy across models
   - Complex functions: Large variance in model performance
   - Clear examples and specifications improve results

### Lab 10 - Test Generation Insights

1. **Test Quality:**
   - LLM-generated tests often miss edge cases
   - Manual tests cover more mutation scenarios
   - Combination of manual + generated = optimal

2. **Coverage vs Mutation Score:**
   - High coverage ≠ High mutation score
   - Generated tests may have high coverage but low kill rate
   - Need both metrics for comprehensive evaluation

3. **LLM Effectiveness:**
   - Varies significantly by model and code complexity
   - Benefit from few-shot examples (reference tests)
   - Better for simple, well-defined functions

---

## 📈 Performance Benchmarks

### Hardware
- **GPU:** NVIDIA GeForce RTX 4060 (8GB VRAM)
- **Memory:** 8GB VRAM typical for Phi-2, StarCoder
- **CPU:** For optimization techniques (quantization, LoRA)

### Typical Metrics
- **CodeLlama-7B:** 14GB inference memory (use 8-bit quantization)
- **Phi-2:** 5GB inference memory (fits easily in 8GB)
- **StarCoder-6.7B:** 13GB inference memory (use device_map="auto")

---

## 🔗 Related Resources

- [Hugging Face Model Hub](https://huggingface.co/models)
- [PyTorch Documentation](https://pytorch.org/docs)
- [Transformers Library](https://huggingface.co/docs/transformers)
- [pytest Documentation](https://docs.pytest.org)
- [Coverage.py Guide](https://coverage.readthedocs.io)

---

## 📝 Lab Assignments Summary

| Lab | Topic | Focus | Deliverable |
|-----|-------|-------|-------------|
| 01 | Transformers | Architecture | Components analysis |
| 02 | Attention | Mechanisms | Visualization & optimization |
| 03 | BERT/GPT-2 | Pre-trained models | Fine-tuning exploration |
| 04 | Fine-tuning | Domain adaptation | Medical domain checkpoint |
| 05 | Optimization | Efficiency | Quantization & LoRA comparison |
| 06 | Prompting & RAG | Knowledge integration | RAG pipeline |
| 07 | Domain data | Specialization | Story generation models |
| 08 | Routing | Model selection | Multi-model system |
| 09 | Code generation | LLM for coding | Comparative analysis |
| 10 | Test generation | Automated QA | Test quality metrics |

---

## 📄 License

This laboratory series is part of the Politecnico di Torino Master's program in Computer Science.

---

**Last Updated:** December 2025
**Version:** 1.0
