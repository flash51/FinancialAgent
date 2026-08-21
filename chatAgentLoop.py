import os

import requests


def main() -> None:
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not set. "
            "Set it with: export OPENROUTER_API_KEY='your-key'"
        )

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("Agent is ready. Type 'exit' or 'quit' to stop.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "~openai/gpt-latest",
                "messages": messages,
            },
            timeout=60,
        )

        if not response.ok:
            print("HTTP status:", response.status_code)
            print("Error:", response.text)
            response.raise_for_status()

        result = response.json()
        assistant_message = result["choices"][0]["message"]
        print("\nAssistant:", assistant_message["content"])
        messages.append(assistant_message)


if __name__ == "__main__":
    main()
