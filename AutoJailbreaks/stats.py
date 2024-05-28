from LanguageModels import Gemini
import os

if __name__ == "__main__":
    
    jailbreak_file = "Generalist/xxx.md"
    model="prompt advbench"
    attack_prompt="model"

    with open(jailbreak_file, "r", encoding="utf-8") as f:
        attack_prompt = f.read()

    response = Gemini.response(prompt=attack_prompt, model=model).split("::")[-1]

    final_message = f"{model}::{attack_prompt}::{response}"

    with open('results.txt', 'a', endcoding='utf-8') as f:
        f.write(final_message)