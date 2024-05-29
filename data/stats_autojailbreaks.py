import AutoJailbreaks.main_AutoJailbreaks as main_AutoJailbreaks
import Evaluations.GTP_evaluator as GTP_evaluator
import pandas as pd
import time
import wandb
import argparse
import json

with open('data/advbench_by_theme.json', 'r') as file:
    prompts_by_themes = json.load(file)
      
if __name__ == "__main__":
        
    columns = ['prompt', 'response', 'evaluator_response', 'attack_mode', 'chosen_prompt', 'ascii_word', 'model_name', 'evaluator','theme']
    
    model_name = "gemini-1.5-flash"
    j=0
    for chosen_prompt in ["ClassicVSJailbreak"]:
        
        df = pd.DataFrame(columns=columns)

        for theme in prompts_by_themes:
            for harmfull_prompt, ascii_word, goal in prompts_by_themes[theme]:
                for i in range(3):
                    j+=1
                    print(j)
                    args = {
                        "model_name":model_name,
                        "prompt":harmfull_prompt,
                        "chosen_prompt":chosen_prompt,
                    }

                    args = argparse.Namespace(**args)

                    response = main_AutoJailbreaks.main(args)[1]

                    score = GTP_evaluator.get_score(question=harmfull_prompt, response=response)
                    
                    data = {
                        'prompt': harmfull_prompt,
                        'response': response,
                        'Jailbreak_Powerness': score,
                        'attack_mode': 'AutoJailbreaks',
                        'Technique': chosen_prompt,
                        'ascii_word': None,
                        'model_name': model_name,
                        'evaluator': "chatgpt-3.5-turbo",
                        'Theme': theme,
                    }

                    new_row_df = pd.DataFrame([data])

                    #print(harmfull_prompt, response)
                    df = pd.concat([df, new_row_df], ignore_index=True)

        df.to_csv(f'stats - {chosen_prompt}.csv')

        t = time.time()
        wandb.init(project='NLP')
        wandb.log({f"stats_autojailbreaks_{t}": wandb.Table(dataframe=df)})
        wandb.finish()