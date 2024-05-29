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

        
    df = pd.DataFrame(columns=columns)

    for theme in prompts_by_themes:
        for harmfull_prompt, ascii_word, goal in prompts_by_themes[theme]:
            j+=1
            print(j)
            args = {
                "model_name":model_name,
                "prompt":harmfull_prompt,
                "chosen_prompt":None,
            }

            args = argparse.Namespace(**args)

            if "gpt" in args.model_name.lower():
                from LanguageModels import GPT as AI

            elif "mistral" in args.model_name.lower():
                from LanguageModels import Mistral as AI

            elif "gemini" in args.model_name.lower():
                from LanguageModels import Gemini as AI
                
            else:
                from LanguageModels import Replicate as AI


            response = AI.response(prompt=harmfull_prompt, model_name=args.model_name).split("::")[-1]

            score = GTP_evaluator.get_score(question=harmfull_prompt, response=response)
            
            data = {
                'prompt': harmfull_prompt,
                'response': response,
                'Jailbreak_Powerness': score,
                'attack_mode': None,
                'Technique': None,
                'ascii_word': None,
                'model_name': model_name,
                'evaluator': "chatgpt-3.5-turbo",
                'Theme': theme,
            }

            new_row_df = pd.DataFrame([data])

            df = pd.concat([df, new_row_df], ignore_index=True)

        df.to_csv(f'stats - None.csv')

        t = time.time()
        wandb.init(project='NLP')
        wandb.log({f"stats_None_{t}": wandb.Table(dataframe=df)})
        wandb.finish()