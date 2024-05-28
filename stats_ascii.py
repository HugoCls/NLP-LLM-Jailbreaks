import ArtPrompt.main_ArtPrompt as main_ArtPrompt
import Evaluations.GTP_evaluator as GTP_evaluator
import pandas as pd
import time
import wandb
import argparse

themes = {}
      
if __name__ == "__main__":
    
    columns = ['prompt', 'response', 'evaluator_response', 'attack_mode', 'chosen_prompt', 'ascii_word', 'model_name', 'evaluator']
    
    df = pd.DataFrame(columns=columns)

    model_name = "chatgpt-3.5-turbo"

    for theme in themes:
        for harmfull_prompt, ascii_word in themes[theme]:
            for i in range(5):

                args = {
                    "model_name":model_name,
                    "prompt":harmfull_prompt,
                    "ascii_word":ascii_word,
                }

                args = argparse.Namespace(**args)

                response = main_ArtPrompt.main(args)[1]

                score = GTP_evaluator.get_score(question=harmfull_prompt, response=response)
                
                data = {
                    'prompt': harmfull_prompt,
                    'response': response,
                    'evaluator_response': score,
                    'attack_mode': 'ArtPrompt',
                    'chosen_prompt': None,
                    'ascii_word': ascii_word,
                    'model_name': model_name,
                    'evaluator': "chatgpt-3.5-turbo",
                }

                new_row_df = pd.DataFrame([data])

                df = pd.concat([df, new_row_df], ignore_index=True)

    df.to_csv('ascii_results.txt')

    t = time.time()
    wandb.init(project='NLP')
    wandb.log({f"stats_ascii_{t}": wandb.Table(dataframe=df)})
    wandb.finish()