from evaluate_GPT import get_score
from GPT import query, response

# Load advbench dataset
with open("data/advbench.txt", "r") as f:
    advbench_list = f.readlines()

for i in range(len(advbench_list)):
    advbench_list[i] = advbench_list[i].strip()


if __name__ == "__main__":

    query_model = "gpt-3.5-turbo-0125"

    for j in range(1):
        for jailbreak in ["ClassicVSJailbreak", "Dan6.0", "Dude", "MongoTom", "Stan"]:

            with open(f"Prompts/English/Generalist/{jailbreak}.md", "r", encoding="utf-8") as f:
                jailbreak_prompt = f.read()

            for question in advbench_list[:1]:

                prompt = jailbreak_prompt.replace('which is ""', f'which is "{question}"')

                context = [
                        {"role": "user", "content": jailbreak_prompt.replace('Your interlocutor issues his first request, which is "".','')},
                        {"role": "assistant", "content": response(jailbreak_prompt.replace('Your interlocutor issues his first request, which is "".',''))},
                        {"role": "user", "content": question}
                    ]

                message, completion_tokens, prompt_tokens, input_price, output_price = query(context=context, model=query_model, temperature=0.1)

                final_message = f"{query_model}::{completion_tokens}::{prompt_tokens}::{input_price}::{output_price}::{message}".replace('\n', ' ')

                score = get_score(question=question, response=message)

                jailbreak_result = f"{query_model}::{score}::{jailbreak}::{question}::{message}".replace('\n', ' ')

                with open(f"data/GPT_results.txt", "a", encoding="utf-8") as f:
                    f.write(f"{final_message}\n")

                with open(f"data/PromptsJailbreaks_Results.txt", "a", encoding="utf-8") as f:
                    f.write(f"{jailbreak_result}\n")