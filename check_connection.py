"""Verify the Gemini connection without starting Gradio."""

from openai import OpenAI

from config import load_settings
from research_manager import GEMINI_OPENAI_BASE_URL


def main() -> int:
    settings = load_settings()
    if not settings.api_key:
        print("FAILED: Add GOOGLE_API_KEY or GEMINI_API_KEY to .env first.")
        return 1

    print(f"Testing model: {settings.model}")
    print("Connection route: OpenAI-compatible Gemini endpoint")
    client = OpenAI(
        base_url=GEMINI_OPENAI_BASE_URL,
        api_key=settings.api_key,
        timeout=30.0,
        max_retries=0,
    )
    try:
        response = client.chat.completions.create(
            model=settings.model,
            messages=[{"role": "user", "content": "Reply with exactly: CONNECTION_OK"}],
        )
        answer = (response.choices[0].message.content or "").strip()
        if not answer:
            print("FAILED: Gemini returned an empty response.")
            return 1
        print(f"Gemini response: {answer}")
        print("CONNECTION TEST PASSED")
        return 0
    except Exception as error:
        message = str(error).replace(settings.api_key, "[REDACTED]")
        print(f"FAILED: {type(error).__name__}: {message}")
        return 1
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
