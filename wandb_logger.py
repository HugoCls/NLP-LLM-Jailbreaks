import wandb
import pandas as pd
import time
import logging as logg

logg.basicConfig(filename="data/console.log", level=logg.INFO, format="%(asctime)s [%(levelname)s] %(name)s:%(filename)s - %(message)s")

def log_(args, attack_prompt, response, score):
    wandb.init(project='NLP', entity='hugocls')

    data = {
        'prompt': [args.prompt],
        'attack_prompt': [attack_prompt],
        'attack_mode': [args.attack_mode],
        'model_name': [args.model_name],
        'response': [response],
        'evaluator': [args.evaluator],
        'evaluator_response': [score],
        'expected_result': [args.expected_result],
        'chosen_prompt': [args.chosen_prompt],
        'ascii_word': [args.ascii_word],
    }

    for arg_name, arg_value in data.items():
        logg.log(level=logg.INFO, msg=f"{arg_name}: {arg_value[0]}")
    
    df = pd.DataFrame(data)

    t = time.time()

    wandb.log({f"run_{t}": wandb.Table(dataframe=df)})
    wandb.finish()