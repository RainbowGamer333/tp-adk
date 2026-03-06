"""
coordinator_agent/callbacks.py

Callbacks pour le coordinator_agent
"""


def french_response_callback(callback_context, llm_request):
    """
    Callback qui force les réponses en français
    
    Ce callback s'exécute AVANT chaque appel au LLM.
    Il modifie la demande pour ajouter une instruction en français.
    
    Args:
        callback_context: CallbackContext
            - callback_context.agent_name: Nom de l'agent ("SupportCoordinator")
            - callback_context.state: État de la session (dict mutable)
            - Autres infos sur l'exécution
        
        llm_request: La demande LLM
            - llm_request.system_instruction: Le prompt système
            - llm_request.contents: Le contenu de la demande
    
    Returns:
        None: Continue normalement avec la demande modifiée
        LlmResponse: Retourne une réponse sans appeler le LLM
    """
    
    # Instruction pour forcer le français
    french_instruction = """

[INSTRUCTION IMPORTANTE]:
- Vous DEVEZ répondre UNIQUEMENT en français
- Pas un mot en anglais
- Pas d'autre langue
- Grammaire française correcte
- Style professionnel et courtois"""
    
    # Modifier la demande en ajoutant l'instruction
    llm_request.config.system_instruction += french_instruction
    print("[CALLBACK] french_response_callback: Modifié la demande pour forcer le français.")
    # Retourner None = continuer avec la demande modifiée
    return None


def logging_callback(callback_context, llm_response):
    """
    Callback qui logge les réponses du LLM
    
    Ce callback s'exécute APRÈS chaque réponse du LLM.
    Il logge la réponse pour le suivi et le debugging.
    
    Args:
        callback_context: CallbackContext
            - callback_context.agent_name: Nom de l'agent ("SupportCoordinator")
            - callback_context.state: État de la session (dict mutable)
            - Autres infos sur l'exécution
        llm_response: La réponse du LLM
            - llm_response.text: Le texte de la réponse
            - llm_response.metadata: Métadonnées sur la réponse
    Returns:
        None: Continue normalement
    """
    print(f"[CALLBACK] logging_callback: Réponse du LLM pour {callback_context.agent_name}: {llm_response.content}")
    # Vous pouvez aussi logguer dans un fichier ou une base de données ici
    return None