# StackOverflowTagger

## Introduction:
This is a toy model using BERT-base to predict tags for a StackOverflow question. Ideally ModernBert is a better option for the task but due to local setup constraints, BERT-base

## Why BERT over n-shot GPT for this task:
- High Task Specificity: The classification heads are finetuned over specific labels, reducing risk of hallucination 
- High Computationally Efficiency (for discriminative tasks): BERT-base has 110M parameters, while earlier GPT, e.g. LLaMA1, has a minimum of 1B parameters. SOTA GPT models can reach parameter size of at least 7B
- Fewer Overheads: do not require prompting skill

## Cons of BERT over GPT for this task:
Finetuning is required for BERT(/ModernBert); while SOTA GPT can perform n-shot predictions without finetuning.

## Content:
This repository includes:
- main.py: Endpoint for prediction
- SQL.txt: The SQL query for the dataset
- requirements.py: Library requirements for main.py
- StackOverflowTagger.ipynb: Training workbook and eval statistics

## How to use it:
```
cd the/directory/to/this/folder
python ./main.py --query "your_questions"
 
```
