# 🧠 Smart Meeting Summarizer Agent
> GPT-powered Notion → JSON → Google Calendar automation

Turns messy meeting notes into structured JSON and creates calendar events—hands-off.

---

## 🚀 What It Does
1. Pulls meeting notes from a Notion page
2. Sends the text to GPT (via OpenRouter)
3. GPT returns structured JSON
4. Events are automatically added to Google Calendar

---




## ⚙️ How To Use

```bash
git clone https://github.com/YOUR-USERNAME/smart-meeting-summarizer.git
cd smart-meeting-summarizer
pip install -r requirements.txt

export OPENROUTER_API_KEY="your-openrouter-key"
export NOTION_API_KEY="your-notion-secret"
python main.py
```

---


🛠 Tech Stack
| Layer        | Tool                      |
| ------------ | ------------------------- |
| LLM          | GPT-3.5 via OpenRouter    |
| Notes Source | Notion API                |
| Calendar     | Google Calendar API       |
| Runtime      | Python 3 (tested on 3.11) |
| Platform     | Replit + GitHub           |

---

📄 Prompt Format (Zero-Hallucination)

You are “MeetingSummarizer‑v2”...
RULES:
- Do NOT invent data.
- Use only dates that are explicitly present.
<<<
{meeting_notes}
>>>


---


📅 Sample Output (Example)

{
  "summary": "Project timeline set. Tasks assigned. Next meeting scheduled.",
  "decisions": ["Assign tasks", "Set deadlines"],
  "action_items": [
    {
      "task": "Write onboarding doc",
      "assignee": "Dev",
      "deadline": "2025-06-20"
    }
  ],
  "attendees": ["Anikait", "Riya", "Dev"],
  "next_meeting_date": "2025-06-25"
}


---


📖 License
MIT

---

## ✅ Step 3: Paste it into GitHub

1. Go back to GitHub  
2. In the big editor box, paste everything you copied (Ctrl+V or Cmd+V)

---

## ✅ Step 4: Commit

1. Scroll to the bottom
2. Leave the default commit message (`Create README.md`)
3. Click the green **Commit new file** button

Done ✅

You’ve now written a professional, clean README file for your project.  
Let me know once you're done, and I’ll show you how to push screenshots or link your Replit.

