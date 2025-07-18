# 🧠 Smart Meeting Summarizer Agent
> GPT-powered Notion → JSON → Google Calendar automation

Turns messy meeting notes into structured JSON and creates calendar events—hands-off.

---

## 🚀 What It Does
1. Pulls meeting notes from a Notion page
2. Sends the text to GPT (via OpenRouter)
3. GPT returns structured JSON
4. Events are automatically added to Google Calendar

   <pre> ### 🗂 Folder Structure ``` smart-meeting-summarizer/ ├── main.py # Entry point for running the summarizer ├── calendar_auth.py # Handles Google Calendar auth ├── notion_fetcher.py # Pulls meeting notes from Notion ├── json_parser.py # Converts raw notes to structured JSON ├── calendar_uploader.py # Adds events to Google Calendar ├── docs/ │ └── img/ # Screenshots for README │ └── placeholder.txt # (Can be deleted after uploading images) ├── README.md ``` </pre>

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




Done ✅

You’ve now written a professional, clean README file for your project.  
Let me know once you're done, and I’ll show you how to push screenshots or link your Replit.

