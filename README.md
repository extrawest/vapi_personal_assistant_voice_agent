# 🤖 Vapi Personal Assistant Voice Agent

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]()
[![Maintainer](https://img.shields.io/static/v1?label=Yevhen%20Ruban&message=Maintainer&color=red)](mailto:yevhen.ruban@extrawest.com)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)]()
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![GitHub release](https://img.shields.io/badge/release-v1.0.0-blue)

A FastAPI-based backend service for a personal assistant voice agent integrated with Vapi AI. 
This project demonstrates how to build a structured API that handles todo lists, reminders, and calendar events through voice commands processed by AI.




https://github.com/user-attachments/assets/56214fbe-6429-4d97-9695-ecccc34d0a71


### Phone call demo




https://github.com/user-attachments/assets/5859b32b-7c49-487b-84c7-7647eb0d860a




## 🌟 Features

- **📝 Todo Management**: Create, list, complete, and delete todo items
- **⏰ Reminders**: Set and manage reminders with importance levels
- **📅 Calendar**: Schedule and track events with start and end times
- **📞 Call Initiation**: Trigger outbound calls via Vapi AI API
- **🔄 Vapi AI Integration**: Process natural language commands into structured API calls
- **🔧 Clean Architecture**: Follows best practices with proper separation of concerns
- **🧠 Persistent Memory** *(optional)*: Semantic memory across sessions via [General Intellect](https://github.com/General-Intellect/general-intellect)

### Memory setup

Two new Vapi tools are available — `recallMemory` and `remember` — that your assistant can call to retrieve and store context across sessions.

To enable, start the memory server and set `GI_URL`:

```bash
docker run -p 8000:8000 generalintelect/gi-server
export GI_URL=http://localhost:8000
```

If `GI_URL` is not set, the tools still respond correctly — they simply return an empty context. No breaking changes.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Pip package manager
- Vapi AI account and API key (for call functionality)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/extrawest/vapi_personal_assistant_voice_agent.git
cd vapi_personal_assistant_voice_agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Copy the example environment file
cp src/.env.example .env

# Edit the .env file with your Vapi API key
# Replace 'your_vapi_api_key_here' with your actual API key
```

4. Run the application:
```bash
uvicorn src.main:app --reload
```

5. Access the API documentation:
```
http://localhost:8000/docs
```

## 🔌 Vapi AI Integration

This service is designed to work with Vapi AI's voice assistant platform. The integration enables:

1. **Natural Language Processing**: Convert voice commands to structured API calls
2. **Context Awareness**: Maintain conversation context for follow-up commands
3. **Tool-Based Execution**: Execute specific functions based on user intent
4. **Outbound Calls**: Initiate calls to customers using Vapi's telephony infrastructure

### Example Voice Commands

- "Add a new todo to buy groceries"
- "Remind me to call mom tomorrow at 5 PM"
- "Schedule a meeting with the team on Friday from 2 to 3 PM"
- "Call customer John at +1-202-555-0123"

## 🛠️ Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM for database operations
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for running the application
- **SQLite**: Lightweight disk-based database
- **Requests**: HTTP library for making API calls to Vapi

Developed by [extrawest](https://extrawest.com/). Software development company
