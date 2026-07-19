import os
import sys
from dotenv import load_dotenv
from langsmith import Client
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header

load_dotenv()

def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    try:
        client = Client()

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", prompt_data["system_prompt"]),
                ("human", prompt_data["user_prompt"]),
            ]
        )

        client.push_prompt(
            prompt_name,
            object=prompt,
            description=prompt_data.get(
                "description",
                "Prompt otimizado automaticamente.",
            ),
            tags=prompt_data.get(
                "tags",
                ["optimization", "bug-to-user-story"],
            )
        )   

        print(f"✅ Prompt '{prompt_name}' publicado com sucesso.")
        return True

    except Exception as e:
        print(f"❌ Erro ao publicar '{prompt_name}':")
        print(f"   {e}")
        return False


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    errors = []

    if not isinstance(prompt_data, dict):
        errors.append("Prompt deve ser um dicionário.")
        return False, errors

    return len(errors) == 0, errors



def main():
    print_section_header("Push de Prompts para o LangSmith")

    check_env_vars(
        [
            "LANGSMITH_API_KEY",
        ]
    )

    prompts = load_yaml("prompts/bug_to_user_story_v2.yml")

    if not prompts:
        print("❌ Nenhum prompt encontrado.")
        return 1

    success = 0
    failed = 0

    for prompt_name, prompt_data in prompts.items():

        print(f"\n📌 Validando: {prompt_name}")

        valid, errors = validate_prompt(prompt_data)

        if not valid:
            print("❌ Prompt inválido:")

            for error in errors:
                print(f"   • {error}")

            failed += 1
            continue

        print("✅ Estrutura válida.")

        if push_prompt_to_langsmith(prompt_name, prompt_data):
            success += 1
        else:
            failed += 1

    print_section_header("Resumo")

    print(f"✅ Publicados: {success}")
    print(f"❌ Falhas: {failed}")

    return 0 if failed == 0 else 1



if __name__ == "__main__":
    sys.exit(main())
