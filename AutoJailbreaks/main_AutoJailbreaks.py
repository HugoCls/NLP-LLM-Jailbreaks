from LanguageModels import GPT
import os

prompt_files = []
# Walk through the directory and its subdirectories
for root, dirs, files in os.walk("AutoJailbreaks"):
    # Check each file in the current directory
    for file in files:
        # Check if the file has a .md extension
        if file.endswith('.md'):
            # Construct the full path of the file
            file_path = os.path.join(root, file)
            # Append the file path to the list
            prompt_files.append(file_path)

def main(args):
    
    jailbreak_file = None

    for prompt_file in prompt_files:
        if args.chosen_prompt in prompt_file:
            jailbreak_file = prompt_file

    if jailbreak_file:
        with open(jailbreak_file, "r", encoding="utf-8") as f:
            attack_prompt = f.read()

        attack_prompt = attack_prompt.replace('""', f'"{args.prompt}"')

        response = GPT.response(prompt=attack_prompt, model=args.model_name).split("::")[-1]

        return attack_prompt, response
    
    else:
        raise ValueError("Wrong prompt chosen")