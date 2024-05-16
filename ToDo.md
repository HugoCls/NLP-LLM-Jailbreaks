# NLP-LLM-Jailbreaks

# A Faire / Objectifs

# TODO
P1:
- Appel API: Llama 2/3, Gemini, Palm, Vicuna, Mistral..
  
- Evaluator
  - Améliorer les Prompts Evaluator
  - Tester les Prompts sur d'autres IA

- Combiner TAP & Prompts de jailbreak

 - Lancer TAP sur dataset advbench
    
P2:
- IA Locales (Llama?.. )
- Regarder les méthodes de DRA implémentées en ligne


P5:
- Implémenter TAP et le faire fonctionner avec gpt comme LLMs ( voir si on peut en utiliser d'autres)
    --> Mettre à jour les fonctions qui appellent l'api chatgpt, et ajouter des modeles

- Implémenter query avec navigateur




# DONE
- Utiliser le GPT evaluator
- Tester les Jailbreak Prompts avec les 5 premiers 
    - Lancer 10 fois chaque prompt de Prompts, logger question::response::jailbreak
    - Faire un graph du score moyen de chaque jailbreak sur les différents thèmes de questions

# RESULTS
- Evaluator GPT marche que en GPT4 mais cher
- TAP coutre tres cher en query
- Les jailbreaks API marchent tres rarement (pas avec 3.5 turbo)

