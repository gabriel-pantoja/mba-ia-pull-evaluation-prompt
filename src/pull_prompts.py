import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langsmith import Client
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()
client = Client()

PROMPT_NAME = "bug_to_user_story_v1"
OUTPUT_PATH = Path("prompts") / f"{PROMPT_NAME}.yml"

def pull_prompts_from_langsmith():
    prompt = client.pull_prompt(PROMPT_NAME)
    serialized_prompt = prompt.dict()

    return serialized_prompt

def main():
    """Função principal"""

    print_section_header("LangSmith Prompt Pull")

    provider = os.getenv("LLM_PROVIDER", "openai")
    llm_model = os.getenv("LLM_MODEL", "gpt-4o-mini")
    eval_model = os.getenv("EVAL_MODEL", "gpt-4o")

    print(f"Provider: {provider}")
    print(f"Modelo Principal: {llm_model}")
    print(f"Modelo de Avaliação: {eval_model}\n")

    required_vars = ["LANGSMITH_API_KEY", "LLM_PROVIDER"]
    if provider == "openai":
        required_vars.append("OPENAI_API_KEY")
    elif provider in ["google", "gemini"]:
        required_vars.append("GOOGLE_API_KEY")

    if not check_env_vars(required_vars):
        return 1
    
    try:
        prompt_data = pull_prompts_from_langsmith()

        # Garante que a pasta existe
        OUTPUT_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        # Salva como YAML
        save_yaml(
            prompt_data,
            OUTPUT_PATH
        )

        print(
            f"\nPrompt salvo com sucesso em: {OUTPUT_PATH}"
        )

        return 0

    except Exception as e:
        print(
            f"Erro ao baixar prompt: {e}"
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
