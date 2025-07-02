import csv
from unsloth import FastLanguageModel
from peft import PeftModel
import torch
from google.colab import files
import os
import zipfile

# Simulate cache for concept descriptions
description_cache = {}
model_name = "finetuned_phi4"
model_type = "unsloth/Phi-4"

def generate_elaborate_prompt(context: str) -> str:
  print("starting model")
  prompt = f"### Instruction:\n{context.strip()}\n### Response:\n"
  print("prompt")
  inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
  with torch.no_grad():  # Avoids unnecessary gradient tracking
    outputs = model.generate(**inputs, max_new_tokens=100)
  full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
  return full_output.split("### Response:")[-1].strip()

def cache_description(concept: str, prompt: str):
  description_cache[concept] = prompt

def get_cached_description(concept: str) -> str:
  return description_cache.get(concept)

def get_all_cached_descriptions() -> dict:
  return description_cache

def load_cache_from_csv(file_path: str):
  with open(file_path, newline='', encoding='utf-8') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          concept = row["input"]
          prompt = row["finetuned_model_answer"]
          if concept and prompt:
              cache_description(concept, prompt)



def load_model():
  global model, tokenizer
  model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=model_type,
    max_seq_length=2048,
    load_in_4bit=True,         # Use this if your GPU supports 4-bit
    device_map="auto",         # or {"": "cuda"} for single-GPU
    dtype=None,
    )
  model = PeftModel.from_pretrained(model, model_name)
  model.eval()
  tokenizer = tokenizer.from_pretrained(model_name)