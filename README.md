# NLP-LLM-Jailbreaks

# A Faire / Objectifs

# TODO
- Implémenter TAP et le faire fonctionner avec gpt comme LLMs ( voir si on peut en utiliser d'autres) **HUGO/REMI**
    --> Mettre à jour les fonctions qui appellent l'api chatgpt, et ajouter des modeles **HUGO**

- Implémenter l'appel API de Llama 2/3 **REMI**
    --> L'implémenter pour le evaluator
    --> Query les jailbreaks avec d'autres IA

- Implémenter l'appel à des IA Locales

- Implémenter query avec navigateur **HUGO**

- Faire deux cafés **JAMES**

- Implémenter TAP avec d'autres IA

# DONE
- Utiliser le GPT evaluator
- Tester les Jailbreak Prompts avec les 5 premiers 
    - Lancer 10 fois chaque prompt de Prompts, logger question::response::jailbreak
    - Faire un graph du score moyen de chaque jailbreak sur les différents thèmes de questions

# RESULTS
- Evaluator GPT marche que en GPT4 mais cher
- TAP coutre tres cher en query
- Les jailbreaks API marchent tres rarement (pas avec 3.5 turbo)