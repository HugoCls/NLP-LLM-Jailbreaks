from openai import OpenAI
from dotenv import load_dotenv
import os
import logging as log
import datetime

from LanguageModels.GPT import response


# Plan TAP 
# Get the first prompt
# Give it to 2 attacker llms along with the sentence associated
# For each attacker do :
# Separate the improvement part from the actual new prompt
# Give the new prompt to the evaluator at the same time with the on topic sentence and get the result
# Give it to the target and get the result
# Then give the target answer to the evaluator to see if its jailbreak
# If not, get the best evalutor answer (random if the same) and get the associated prompt to the top to create 2 new attacker prompts
