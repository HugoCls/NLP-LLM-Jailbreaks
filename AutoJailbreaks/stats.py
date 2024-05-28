from LanguageModels import Gemini
import os

if __name__ == "__main__":
    
    jailbreak_file = "Generalist/ClassicVSJailbreak.md"
    model_name="gemini-1.5-flash"
    attack_prompt="AutoJailbreaks/data/advbench.txt"

    with open(jailbreak_file, "r", encoding="utf-8") as f:
        attack_prompt = f.read()

    response = Gemini.response(prompt=attack_prompt, model_name=model_name).split("::")[-1]

    final_message = f"{model_name}::{attack_prompt}::{response}"

    with open('results.txt', 'a', endcoding='utf-8') as f:
        f.write(final_message)
