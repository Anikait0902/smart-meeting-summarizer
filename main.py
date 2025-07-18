import requests
import json
import os

import requests
import os

PAGE_ID = "23431568ec1a807fa484d2fb4e8298d4"


def get_meeting_notes_from_notion():
    url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"
    headers = {
        "Authorization": f"Bearer {os.environ['NOTION_API_KEY']}",
        "Notion-Version": "2022-06-28"
    }

    res = requests.get(url, headers=headers)
    data = res.json()

    blocks = data.get("results", [])
    text = ""

    for block in blocks:
        if "paragraph" in block and block["paragraph"]["rich_text"]:
            for rt in block["paragraph"]["rich_text"]:
                text += rt.get("plain_text", "") + " "
        text += "\n"

    return text.strip()


api_key = os.environ["OPENROUTER_API_KEY"]

meeting_notes = get_meeting_notes_from_notion()
print("🔍 Meeting Notes from Notion:\n", meeting_notes)

prompt = f"""
You are a meeting summarization agent.

Your task: Convert raw meeting notes into a JSON object.

RULES:
- Respond ONLY with a JSON object, nothing else.
- No explanations, no markdown, no extra text.

The JSON should include:
- summary (3-4 lines)
- decisions (as a list)
- action_items (list of task, assignee, deadline)
- attendees (list)
- next_meeting_date (if mentioned)

Meeting Notes:
\"\"\"
{meeting_notes}
\"\"\"
"""

response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                         headers={
                             "Authorization": f"Bearer {api_key}",
                             "HTTP-Referer": "https://yourdomain.com",
                             "X-Title": "Meeting Summarizer Agent"
                         },
                         json={
                             "model": "openai/gpt-3.5-turbo",
                             "messages": [{
                                 "role": "user",
                                 "content": prompt
                             }],
                             "temperature": 0.2
                         })

try:
    raw_output = response.json()["choices"][0]["message"]["content"]

    parsed = json.loads(raw_output)
    print("🧠 GPT Output (JSON):\n", json.dumps(parsed, indent=2))

    # 🔁 CALENDAR LOGIC STARTS HERE
    from calendar_auth import authenticate_calendar
    from datetime import datetime

    service = authenticate_calendar()

    for item in parsed.get("action_items", []):
        task = item.get("task")
        assignee = item.get("assignee")
        deadline_str = item.get("deadline")

        if not task or not deadline_str or deadline_str.lower() == "tbd":
            continue  # skip if missing or TBD

        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
        except ValueError:
            print(f"⚠️ Skipping invalid date: {deadline_str}")
            continue

        event = {
            'summary': f"{task} - {assignee}",
            'start': {
                'date': deadline_str,
                'timeZone': 'Asia/Kolkata'
            },
            'end': {
                'date': deadline_str,
                'timeZone': 'Asia/Kolkata'
            },
        }

        created_event = service.events().insert(calendarId='primary',
                                                body=event).execute()
        print(
            f"✅ Event created: {created_event.get('summary')} on {deadline_str}"
        )

except json.JSONDecodeError:
    print("⚠️ GPT returned non-JSON response. Here's the raw output:\n")
    print(raw_output)
