"""AI tutor backed by the Anthropic API, with an offline fallback for local dev."""
import anthropic
from django.conf import settings

TUTOR_SYSTEM_PROMPT = """You are the AI Tutor for AI 101 Academy, a beginner-friendly AI course
for the local community in the Cayman Islands. Students are non-technical: hospitality workers,
bankers, accountants, teachers, small business owners, and students.

Your job:
- Explain AI concepts simply, with analogies and everyday examples (use Cayman context when natural:
  tourism, restaurants, banks in George Town, dive shops, etc.).
- Help with prompt engineering: show concrete before/after prompt examples.
- Create practice exercises and evaluate student answers with structured, encouraging feedback.
- Keep answers short and skimmable: a few sentences or a short list, unless asked for more depth.
- Never assume programming knowledge. Stay on the topic of AI, its tools, and its applications.
"""


def offline_reply(message):
    """Rule-based fallback so the tutor is useful without an API key."""
    text = message.lower()
    if any(w in text for w in ("prompt", "prompting", "ask better")):
        return (
            "Great question about prompting! A strong prompt has four parts:\n\n"
            "1. **Role** — tell the AI who to be: \"You are an experienced hotel concierge…\"\n"
            "2. **Task** — say exactly what you want: \"…write a warm reply to this guest review.\"\n"
            "3. **Context** — paste the details it needs (the review, your hotel's name, tone).\n"
            "4. **Format** — say how you want the answer: \"Keep it under 100 words, friendly but professional.\"\n\n"
            "Try rewriting one of your everyday requests with those four parts — "
            "the difference in quality is usually dramatic.\n\n"
            "*(I'm running in offline mode. Add an ANTHROPIC_API_KEY in the .env file for the full live AI tutor.)*"
        )
    if any(w in text for w in ("what is ai", "what's ai", "artificial intelligence", "how does ai work", "llm", "language model")):
        return (
            "Think of a large language model (like ChatGPT or Claude) as an extremely well-read "
            "autocomplete. It has read a huge portion of the internet and learned patterns in how "
            "people write and reason. When you ask it something, it predicts the most helpful "
            "continuation — word by word.\n\n"
            "That's why it's brilliant at drafting emails, summarizing documents, and brainstorming, "
            "but why you should always fact-check names, numbers, and dates: it predicts, it doesn't "
            "look things up (unless connected to search).\n\n"
            "*(I'm running in offline mode. Add an ANTHROPIC_API_KEY in the .env file for the full live AI tutor.)*"
        )
    if any(w in text for w in ("hospitality", "hotel", "restaurant", "tourism", "guest")):
        return (
            "AI is a great fit for hospitality here in Cayman. A few quick wins:\n\n"
            "- **Guest replies** — draft responses to TripAdvisor/Google reviews in seconds.\n"
            "- **Menus & promos** — generate seasonal menu descriptions or social posts.\n"
            "- **Multilingual help** — translate guest messages naturally.\n"
            "- **Rota planning** — summarize booking patterns to plan staffing.\n\n"
            "Check Module 4 for the full hospitality walkthrough with ready-to-use prompts.\n\n"
            "*(I'm running in offline mode. Add an ANTHROPIC_API_KEY in the .env file for the full live AI tutor.)*"
        )
    if any(w in text for w in ("bank", "accounting", "audit", "finance", "kyc")):
        return (
            "For banking and accounting work, AI shines at the reading-and-writing heavy tasks:\n\n"
            "- Summarizing long policy documents or regulations into plain English.\n"
            "- Drafting client emails and engagement letters.\n"
            "- Explaining spreadsheet formulas, or writing new ones from a description.\n"
            "- Turning meeting notes into action lists.\n\n"
            "One golden rule: never paste confidential client data into public AI tools — "
            "Module 4 covers safe-use policies in detail.\n\n"
            "*(I'm running in offline mode. Add an ANTHROPIC_API_KEY in the .env file for the full live AI tutor.)*"
        )
    return (
        "Thanks for your question! Here's a tip while I'm in offline mode: the fastest way to get "
        "value from AI tools is to treat them like a smart new colleague — give them context, an "
        "example of what \"good\" looks like, and clear instructions, then iterate on their draft.\n\n"
        "Try asking me about **prompting**, **how AI works**, or **AI in hospitality or banking** "
        "for more specific guidance, and work through the course modules for the full picture.\n\n"
        "*(I'm running in offline mode. Add an ANTHROPIC_API_KEY in the .env file for the full live AI tutor.)*"
    )


def get_tutor_reply(user, message, history, lesson=None):
    """Return the tutor's reply. Uses the Anthropic API when configured."""
    if not settings.ANTHROPIC_API_KEY:
        return offline_reply(message)

    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    system = TUTOR_SYSTEM_PROMPT
    if lesson is not None:
        system += (
            f"\nThe student is currently on the lesson \"{lesson.title}\" "
            f"in {lesson.module}. Relate answers to it when helpful."
        )

    messages = [{"role": m.role, "content": m.content} for m in history]
    messages.append({"role": "user", "content": message})

    try:
        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=1024,
            system=system,
            messages=messages,
        )
        parts = [block.text for block in response.content if block.type == "text"]
        return "\n".join(parts) if parts else "Sorry, I couldn't generate a reply — please try again."
    except anthropic.AuthenticationError:
        return "The AI tutor API key appears to be invalid. Falling back to offline mode:\n\n" + offline_reply(message)
    except anthropic.RateLimitError:
        return "The AI tutor is very busy right now — please try again in a minute."
    except anthropic.APIError:
        return "The AI tutor hit a temporary error. Please try again.\n\n" + offline_reply(message)
