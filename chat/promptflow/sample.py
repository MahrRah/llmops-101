import os
from pathlib import Path

from dotenv import load_dotenv
from promptflow.core import Prompty

BASE_DIR = Path(__file__).absolute().parent


def chat(question: str = "Do other Azure AI services support this too?") -> str:
    """Flow entry function."""

    if "OPENAI_API_KEY" not in os.environ and "AZURE_OPENAI_API_KEY" not in os.environ:
        load_dotenv(dotenv_path=BASE_DIR.parent.parent / ".env")

    prompty = Prompty.load(source=BASE_DIR / "chat.prompty")
    history = [
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {
            "role": "assistant",
            "content": "Yes, customer managed keys are supported by Azure OpenAI.",
        },
    ]

    output = prompty(question=question, history=history)
    return output
