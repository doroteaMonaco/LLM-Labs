# LLM Labs — Large Language Models for Software Engineering

This repository contains laboratory materials for the course "Large Language Models for Software Engineering". Each lab includes educational notebooks (`text-*.ipynb`), solutions (`solution-*.ipynb`), and resources (images, test files). The goal is to provide a practical path from fundamentals (computational graphs, backpropagation) to advanced LLM techniques (quantization, LoRA, RAG).

## Lab Structure and Main Topics

- **lab01/** — Fundamentals: Computational graphs and backpropagation. Includes `text.ipynb` and explanatory images (`computational_graph.png`, `backpropagation.png`).
- **lab02/** — Transformer Basics: Encoder/decoder, attention mechanism. Notebooks: `text-01-t5.ipynb`, `text-02-attention.ipynb`, solutions, and images (`encoder.png`, `decoder.png`, `transformer_encoder.png`).
- **lab03/** — BERT & GPT-2: Experiments with pre-trained models and fine-tuning (`solution-01-bert.ipynb`, `solution-02-gpt2.ipynb`).
- **lab04/** — Language Modeling and LLMs: Practical examples on causal language modeling and LLM usage (`solution-01-clm.ipynb`, `solution-02-llms.ipynb`).
- **lab05/** — Quantization and LoRA: Model compression experiments and Low-Rank Adaptation (`solution-01-quantization.ipynb`, `solution-02-LoRA.ipynb`).
- **lab06/** — Prompt Engineering and RAG: Prompting techniques and retrieval-augmented generation (`solution-06-prompt-engineering-rag.ipynb`). Includes reference papers in the folder.
- **lab07/** — Story Generation: Story generation, example dataset (`stories.csv`), and notebooks with exercises and solutions.
- **lab08/** — ROC / Router Design: System design and analysis (`solution-08-roc-router-design.ipynb`).
- **lab09/** — Code Generation: Exercises on code generation and associated tests (`solution-09-code-generation.ipynb`, `test_cases_01.py`).
- **lab10/** — Test Generation: Examples of automatic test generation and test scripts (`function_01.py`, `test_function_01_copilot.py`, `test_function_01_gpt.py`, `test_function_01_qwen.py`).

Each folder may contain multiple text (educational) and solution notebooks: check `text-*.ipynb` and `solution-*.ipynb` files for detailed content.

## General Requirements

- Python 3.8+ (recommended 3.10/3.11)
- Jupyter / JupyterLab
- pip

Useful base packages (quick install):
```bash
pip install jupyterlab notebook numpy pandas matplotlib torch torchvision torchaudio transformers datasets
```

Note: Some experiments (especially in `lab05` and those using large models) may require optional libraries and/or GPU. Examples:
- `lab05` (Quantization / LoRA): `accelerate`, `bitsandbytes`, `peft` — install if you plan to reproduce GPU experiments.
- Using larger Hugging Face models: `transformers`, `datasets`, optionally `accelerate`.

Install additional dependencies only as needed for specific labs. Check the first cells of each notebook where required libraries are often listed.

## Running the Notebooks

1. Open a terminal in the repository root.
2. (Recommended) Create and activate a virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1    # PowerShell
```
3. Install base requirements (see General Requirements section).
4. Launch JupyterLab:
```bash
jupyter lab
```
5. Open the desired notebook and run cells in order.

## Running Tests and Quick Examples

- `lab09` contains `test_cases_01.py` — you can run the test to validate code generation examples:
```bash
python lab09/test_cases_01.py
```
- `lab10` contains `function_01.py` and various test versions (`test_function_01_*.py`). To run tests:
```bash
python lab10/test_function_01_copilot.py
python lab10/test_function_01_gpt.py
python lab10/test_function_01_qwen.py
```

Tests are simple Python scripts; if preferred, you can integrate them into a test framework (pytest) by creating appropriate `test_*.py` files.

## Running on GPU / Colab

If you don't have a local GPU, you can use Google Colab. For Colab:
1. Open the corresponding notebook on Colab (upload the `.ipynb` file in Colab UI or link the GitHub repository).
2. Set Runtime > Change runtime type > GPU.
3. Ensure dependencies are installed at the beginning of the notebook (cells with `pip install`).

Notes for local GPUs:
- Verify `torch.cuda.is_available()` returns True.
- For heavy loads and quantization, install `bitsandbytes` and `accelerate` and follow official instructions if using GPUs with limited memory.

## Practical Tips

- Run introductory notebooks first (`lab01`, `lab02`) if new to Transformers.
- Read comments in the first cells: they often contain a list of optional packages needed for that experiment.
- When working with large models, save checkpoints and limit batch size to fit GPU memory.


