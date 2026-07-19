import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure
PROMPTS_FILE = Path(__file__).parent.parent / "prompts/bug_to_user_story_v2.yml"


def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

PROMPTS = load_prompts(PROMPTS_FILE)    

class TestPrompts:
    @pytest.mark.parametrize("name,prompt", PROMPTS.items())
    def test_prompt_has_system_prompt(self, name, prompt):
        system_prompt = prompt.get("system_prompt", "")
        assert system_prompt.strip(), f"{name}: system_prompt vazio"

    @pytest.mark.parametrize("name,prompt", PROMPTS.items())
    def test_prompt_has_role_definition(self, name, prompt):
        text = prompt["system_prompt"].lower()

        assert any(x in text for x in [
            "você é",
            "atue como",
            "assuma o papel"
        ]), f"{name}: persona não encontrada"

    @pytest.mark.parametrize("name,prompt", PROMPTS.items())
    def test_prompt_mentions_format(self, name, prompt):
        text = prompt["system_prompt"].lower()

        assert any(x in text for x in [
            "markdown",
            "user story",
            "como <",
            "critérios de aceite",
            "given",
            "when",
            "then",
            "dado que",
            "quando",
            "então",
        ]), f"{name}: formato de saída não encontrado"

    @pytest.mark.parametrize("name,prompt", PROMPTS.items())
    def test_prompt_has_few_shot_examples(self, name, prompt):
        text = prompt["system_prompt"].lower()

        assert (
            "exemplo 1" in text
            or "entrada:" in text
            or "saída:" in text
        ), f"{name}: exemplos few-shot não encontrados"

    @pytest.mark.parametrize("name,prompt", PROMPTS.items())
    def test_prompt_no_todos(self, name, prompt):
        assert "[TODO]" not in prompt["system_prompt"]
        assert "TODO" not in prompt["system_prompt"]

    @pytest.mark.parametrize("name,prompt", PROMPTS.items())
    def test_minimum_techniques(self, name, prompt):
        tags = prompt.get("tags", [])

        # considera tags que representam técnicas de prompting
        techniques = {
            "few-shot",
            "role-prompting",
            "chain-of-thought",
            "skeleton-of-thought",
            "zero-shot",
            "instruction",
        }

        count = len(set(tags) & techniques)

        assert count >= 2, (
            f"{name}: possui apenas {count} técnicas de prompting."
        )

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])