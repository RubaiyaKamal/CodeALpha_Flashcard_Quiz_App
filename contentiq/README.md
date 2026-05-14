# Contentiq — AI Content Writing Assistant

> A professional AI writing partner built with Chainlit and OpenAI GPT-4o.

Contentiq writes fast, clean, and structured content for any audience or platform — blog posts, social media, marketing copy, emails, product descriptions, and more.

---

## Features

- **Streaming responses** — Real-time token streaming for a fluid chat experience
- **Full conversation memory** — Multi-turn context awareness across the entire session
- **4 writing tones** — Professional, Casual, Persuasive, Friendly
- **3 output formats** — Paragraph, Bullet Points, Numbered List
- **Quick-start buttons** — Jump directly into common content types on launch
- **Regenerate & Shorten** — Action buttons after every response to iterate quickly
- **Slash commands** — `/tone`, `/format`, `/reset`
- **Async error handling** — Friendly messages for auth errors, rate limits, and API failures

---

## Tech Stack

| Technology | Version | Purpose |
|---|---|---|
| Python | 3.11+ | Runtime |
| Chainlit | >=1.0.0 | Chat UI framework |
| OpenAI SDK | >=1.30.0 | GPT-4o integration |
| python-dotenv | >=1.0.0 | Environment variable management |

---

## Project Structure

```
contentiq/
├── app.py           # Main Chainlit application
├── .env             # Your API key (create this — do not commit)
├── .env.example     # Template for environment variables
├── requirements.txt # Python dependencies
├── chainlit.md      # Chainlit welcome panel content
└── README.md        # This file
```

---

## Setup

### Prerequisites

- Python 3.11 or higher
- An OpenAI API key — [get one here](https://platform.openai.com/api-keys)

### 1. Navigate to the project

```bash
cd contentiq
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Open `.env` and replace the placeholder:

```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### 5. Run Contentiq

```bash
chainlit run app.py -w
```

The `-w` flag enables auto-reload during development. Open your browser to **http://localhost:8000**.

---

## Usage

### Quick-Start Buttons

On launch, four starter buttons appear to jump directly into common content types:

| Button | Triggers |
|---|---|
| ✍️ Write a blog post | Blog post generation |
| 📱 Social media captions | Caption/thread writing |
| 🛍️ Product description | Product copy |
| 📧 Email campaign | Email writing |

### Slash Commands

| Command | Description |
|---|---|
| `/reset` | Clear history and reset tone/format to defaults |
| `/tone` | Show current tone and available options |
| `/tone Professional` | Switch to Professional tone |
| `/tone Casual` | Switch to Casual tone |
| `/tone Persuasive` | Switch to Persuasive tone |
| `/tone Friendly` | Switch to Friendly tone |
| `/format` | Show current format and available options |
| `/format Paragraph` | Paragraph format |
| `/format Bullet Points` | Bullet point format |
| `/format Numbered List` | Numbered list format |

### Post-Response Action Buttons

After every generated response, two buttons appear:

| Button | Action |
|---|---|
| 🔄 Regenerate | Rewrites the content from scratch |
| ✂️ Make it shorter | Condenses the content, keeps key points |

### Example Prompts

```
Write a 500-word SEO blog post about remote work productivity for freelancers

Write 5 Instagram captions for a specialty coffee shop targeting millennials

Create a compelling Amazon product description for wireless noise-canceling headphones

Draft a cold outreach email targeting HR managers for a B2B SaaS tool

Write a LinkedIn post about lessons learned from launching my first startup
```

---

## Content Types

| Type | Examples |
|---|---|
| Blog & Articles | Long-form posts, SEO articles, how-to guides, thought leadership |
| Social Media | Instagram captions, LinkedIn posts, Twitter/X threads |
| Marketing Copy | Landing pages, ad copy, taglines, CTAs |
| Email Campaigns | Newsletters, cold outreach, follow-up sequences |
| Product Content | Product descriptions, feature highlights, Amazon listings |
| Business Writing | Proposals, bios, company descriptions, investor pitches |
| Fiverr Gigs | Gig titles, descriptions, package copy, FAQs |

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `OPENAI_API_KEY` | Yes | Your OpenAI API key |

---

## Error Handling

Contentiq handles API errors gracefully with user-friendly messages:

| Error | Message shown |
|---|---|
| Invalid API key | Authentication error with `.env` fix instructions |
| Rate limit hit | Friendly retry message |
| OpenAI API error | Service issue message with error details |
| Unexpected error | General fallback with `/reset` suggestion |

---

## Development Notes

- The conversation history includes the system prompt at `history[0]` — never removed on regenerate
- Tone and format directives are appended to every user message before sending to GPT-4o
- The `/reset` command resets tone and format to defaults in addition to clearing history
- `from_action=True` in `_generate()` prevents overwriting `last_prompt` for Regenerate/Shorten calls
