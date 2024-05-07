from GPT import query

# Load advbench dataset
with open("data/advbench.txt", "r") as f:
    advbench_list = f.readlines()

for i in range(len(advbench_list)):
    advbench_list[i] = advbench_list[i].strip()


if __name__ == "__main__":

    model = "gpt-3.5-turbo-0125"

    for harmfull_context in advbench_list:
        context = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": harmfull_context}
            ]

        message, completion_tokens, prompt_tokens, input_price, output_price = query(context=context, model=model)

        final_message = f"{model}:{completion_tokens}:{prompt_tokens}:{input_price}:{output_price}:{message}".replace('\n', ' ')

        advbench_result = f"{harmfull_context}:{message}".replace('\n', ' ')

        with open(f"data/GPT_results.txt", "a", encoding="utf-8") as f:
            f.write(f"{final_message}\n")

        with open(f"data/advbench_w_GPT_answers.txt", "a", encoding="utf-8") as f:
            f.write(f"{advbench_result}\n")