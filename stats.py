from ArtPrompt.main_ArtPrompt import main

def main(prompt_ascii,prompt_tap,prompt_autojailbreak):
    
    data = {
            'prompt': [],
            'response': [],
            'evaluator_response': [],
            'attack_mode': [],
            'chosen_prompt': [],
            'ascii_word': [],
            'model_name': [],
            'evaluator': [],  
        }
    
    df = pd.DataFrame(data)
    df = ascii(df,prompt_ascii)
    df = tap(df,prompt_tap)
    df = autojailbreak(df,prompt_autojailbreak)
    
    return df

def tap(df,prompt_tap):
    break

def autojailbreak(df, prompt_autojailbreak):
    break

def ascii(df, prompts : list):
    for prompt,word in prompts:
        response = Artprompt.main(prompt)[1]
        score = GTP_evaluator.get_score(question=prompt, response=response)
        
        new_row = {
            'prompt': prompt,
            'response': response,
            'evaluator_response': score,
            'attack_mode': 'ArtPrompt',
            'chosen_prompt': None,
            'ascii_word': word,
            'model_name': "chatgpt-3.5-turbo",
            'evaluator': "chatgpt-3.5-turbo",
        }
        df.loc[len(df)] = new_row
    
    return df
    

      
      
if __name__ == "__main__":

    df = main(prompt_ascii=None,prompt_tap=None,prompt_autojailbreak=None)
    
    t = time.time() 

    wandb.init(project='NLP')
    wandb.log({f"stats_{prompt.lower().replace(' ','')}{t}": wandb.Table(dataframe=df)})
    wandb.finish()

