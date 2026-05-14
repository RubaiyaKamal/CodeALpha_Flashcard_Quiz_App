"""
Contentiq — Professional AI Content Writing Assistant
Powered by Chainlit + OpenAI GPT-4o
"""

import os

import chainlit as cl
from chainlit.input_widget import Select
from dotenv import load_dotenv
from openai import APIError, AsyncOpenAI, AuthenticationError, RateLimitError

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are Contentiq, a professional AI content writing assistant. You write clear, engaging, and audience-focused content. You always ask for the target audience and purpose before writing if not provided. You avoid filler words, keep sentences sharp, and structure output for readability. You adapt tone and format based on user commands.

You specialize in:
- Blog posts and long-form articles (SEO articles, how-to guides, thought leadership)
- Social media content (Instagram captions, LinkedIn posts, Twitter/X threads)
- Marketing copy (landing page copy, ad copy, taglines, CTAs)
- Email campaigns (newsletters, cold outreach, follow-up sequences)
- Product descriptions and Amazon listings
- Business writing (proposals, bios, company descriptions, pitches)
- Fiverr gig copy (titles, descriptions, package copy, FAQs)

Always produce clean, professional content with clear structure. Use headings, spacing, and formatting to maximize readability."""

TONES = {
    "Professional": "Use formal, authoritative, and precise language. Maintain a confident expert voice.",
    "Casual": "Write in a relaxed, conversational tone. Be approachable, natural, and easy-going.",
    "Persuasive": "Use compelling, action-driven language with emotional triggers, strong CTAs, and urgency.",
    "Friendly": "Be warm, encouraging, and inclusive. Use positive language and a supportive tone.",
}

FORMATS = {
    "Paragraph": "Write in well-structured paragraphs with natural flow and smooth transitions.",
    "Bullet Points": "Organize all key information using clear bullet points (•) for easy scanning.",
    "Numbered List": "Use a numbered list format, ideal for step-by-step instructions or ranked items.",
}

DEFAULT_TONE = "Professional"
DEFAULT_FORMAT = "Paragraph"


@cl.on_chat_start
async def on_chat_start():
    """Initialize session, mount sidebar settings panel, show welcome screen."""
    cl.user_session.set("history", [{"role": "system", "content": SYSTEM_PROMPT}])
    cl.user_session.set("last_prompt", None)

    if not os.getenv("OPENAI_API_KEY"):
        await cl.Message(
            content=(
                "⚠️ **API Key Missing!**\n\n"
                "Create a `.env` file in the project root with:\n"
                "```\nOPENAI_API_KEY=sk-your-key-here\n```\n"
                "Then restart the app."
            )
        ).send()
        return

    # Mount the left sidebar settings panel — opens via the ⚙️ icon
    settings = await cl.ChatSettings(
        [
            Select(
                id="tone",
                label="Writing Tone",
                values=list(TONES.keys()),
                initial_value=DEFAULT_TONE,
            ),
            Select(
                id="format",
                label="Output Format",
                values=list(FORMATS.keys()),
                initial_value=DEFAULT_FORMAT,
            ),
        ]
    ).send()

    # Seed session from initial sidebar values
    cl.user_session.set("tone", settings["tone"])
    cl.user_session.set("format", settings["format"])

    starter_actions = [
        cl.Action(name="starter_blog", payload={"value": "Write a blog post"}, label="✍️ Write a blog post"),
        cl.Action(name="starter_social", payload={"value": "Create social media captions"}, label="📱 Social media captions"),
        cl.Action(name="starter_product", payload={"value": "Write a product description"}, label="🛍️ Product description"),
        cl.Action(name="starter_email", payload={"value": "Draft an email campaign"}, label="📧 Email campaign"),
    ]

    await cl.Message(
        content=(
            "# Welcome to **Contentiq** ✨\n\n"
            "Your AI-powered writing partner — fast, clean, and professional.\n\n"
            "**What I write:**\n"
            "• Blog posts & SEO articles\n"
            "• Social media captions & threads\n"
            "• Marketing copy & landing pages\n"
            "• Email campaigns & newsletters\n"
            "• Product descriptions & listings\n"
            "• Business proposals & bios\n\n"
            "> Use the **⚙️ Settings panel** on the left to switch tone and format anytime.\n\n"
            "**Pick a content type or describe what you need:**"
        ),
        actions=starter_actions,
    ).send()


@cl.on_settings_update
async def on_settings_update(settings: dict) -> None:
    """Called whenever the user changes a value in the left sidebar settings panel."""
    tone = settings["tone"]
    fmt = settings["format"]
    cl.user_session.set("tone", tone)
    cl.user_session.set("format", fmt)
    await cl.Message(
        content=f"⚙️ **Settings updated** — Tone: `{tone}` · Format: `{fmt}`"
    ).send()


async def _generate(user_prompt: str, from_action: bool = False) -> None:
    """Stream a GPT-4o response with injected tone and format instructions."""
    tone = cl.user_session.get("tone")
    fmt = cl.user_session.get("format")
    history = cl.user_session.get("history")

    if not from_action:
        cl.user_session.set("last_prompt", user_prompt)

    # Append tone and format directives to every request
    augmented_prompt = (
        f"{user_prompt}\n\n"
        f"[Tone: {tone} — {TONES[tone]}]\n"
        f"[Format: {fmt} — {FORMATS[fmt]}]"
    )
    history.append({"role": "user", "content": augmented_prompt})
    cl.user_session.set("history", history)

    response_msg = cl.Message(content="")
    await response_msg.send()

    full_response = ""

    try:
        stream = await client.chat.completions.create(
            model="gpt-4o",
            messages=history,
            stream=True,
            temperature=0.75,
            max_tokens=2048,
        )
        async for chunk in stream:
            token = chunk.choices[0].delta.content
            if token:
                full_response += token
                await response_msg.stream_token(token)

    except AuthenticationError:
        full_response = "⚠️ **Authentication Error:** Invalid API key. Check your `.env` file."
        await response_msg.stream_token(full_response)

    except RateLimitError:
        full_response = "⚠️ **Rate Limit Reached:** Too many requests. Wait a moment and try again."
        await response_msg.stream_token(full_response)

    except APIError as e:
        full_response = f"⚠️ **API Error:** The AI service encountered an issue. Please try again.\n\n`{e}`"
        await response_msg.stream_token(full_response)

    except Exception:
        full_response = (
            "⚠️ **Unexpected Error:** Something went wrong. "
            "Use `/reset` to start a fresh session."
        )
        await response_msg.stream_token(full_response)

    await response_msg.update()

    history.append({"role": "assistant", "content": full_response})
    cl.user_session.set("history", history)

    # Post-generation action buttons
    await cl.Message(
        content="",
        actions=[
            cl.Action(name="action_regenerate", payload={}, label="🔄 Regenerate"),
            cl.Action(name="action_shorter", payload={}, label="✂️ Make it shorter"),
        ],
    ).send()


# ── Starter Button Callbacks ──────────────────────────────────────────────────

@cl.action_callback("starter_blog")
async def on_starter_blog(action: cl.Action):
    await _generate(action.payload["value"])


@cl.action_callback("starter_social")
async def on_starter_social(action: cl.Action):
    await _generate(action.payload["value"])


@cl.action_callback("starter_product")
async def on_starter_product(action: cl.Action):
    await _generate(action.payload["value"])


@cl.action_callback("starter_email")
async def on_starter_email(action: cl.Action):
    await _generate(action.payload["value"])


# ── Post-Generation Action Callbacks ─────────────────────────────────────────

@cl.action_callback("action_regenerate")
async def on_regenerate(action: cl.Action):
    """Re-run the last user prompt, dropping the previous assistant response."""
    last_prompt = cl.user_session.get("last_prompt")
    if not last_prompt:
        await cl.Message(content="Nothing to regenerate yet.").send()
        return
    history = cl.user_session.get("history")
    if len(history) >= 3 and history[-1]["role"] == "assistant":
        history = history[:-2]
        cl.user_session.set("history", history)
    await _generate(last_prompt, from_action=True)


@cl.action_callback("action_shorter")
async def on_make_shorter(action: cl.Action):
    """Ask the model to condense the last generated content."""
    await _generate(
        "Rewrite the previous content to be significantly shorter and more concise. "
        "Keep the essential points but remove all padding and redundancy.",
        from_action=True,
    )


# ── Main Message Handler ──────────────────────────────────────────────────────

@cl.on_message
async def on_message(message: cl.Message) -> None:
    """Route incoming user messages to command handlers or content generation."""
    content = message.content.strip()

    # /reset — wipe history and restore defaults
    if content.lower().startswith("/reset"):
        cl.user_session.set("history", [{"role": "system", "content": SYSTEM_PROMPT}])
        cl.user_session.set("last_prompt", None)
        tone = cl.user_session.get("tone") or DEFAULT_TONE
        fmt = cl.user_session.get("format") or DEFAULT_FORMAT
        await cl.Message(
            content=(
                f"🔄 **Session reset.** History cleared.\n\n"
                f"**Tone:** `{tone}` · **Format:** `{fmt}`\n\n"
                "What would you like to write?"
            )
        ).send()
        return

    await _generate(content)
