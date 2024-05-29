import argparse
import json
import os
import sys

with open('data/advbench_by_theme.json', 'r') as file:
    prompts_by_themes = json.load(file)

sys.path.append(f"{os.getcwd()}/TAP")

os.chdir('./TAP')

import TAP.main_TAP as main_TAP

if __name__ == "__main__":
        
    j=0
    for theme in prompts_by_themes:
        for harmfull_prompt, ascii_word, harmfull_goal in prompts_by_themes[theme]:
           
            j+=1
            print(j)

            # Define a dictionary with the argument values
            TAP_args_dict = {
                "attack_model": "gpt-3.5-turbo",
                "attack_max_n_tokens": 500,
                "max_n_attack_attempts": 5,
                "target_model": 'gpt-3.5-turbo',
                "target_max_n_tokens": 500,
                "evaluator_model": 'gpt-4-0125-preview',
                "evaluator_max_n_tokens": 10,
                "evaluator_temperature": 0.0,
                "index": 0,
                "category": "jailbreaks",
                "iter_index": -1,
                "store_folder": "./result_folder/",
                "branching_factor": 1,
                "width": 10,
                "depth": 10,
                "n_streams": 1,
                "keep_last_n": 3,
                "goal": harmfull_prompt,
                "target_str": harmfull_goal,
            }

            # Create a Namespace object from the dictionary
            TAP_args = argparse.Namespace(**TAP_args_dict)

            # Now pass the args to the main function
            main_TAP.main(TAP_args)