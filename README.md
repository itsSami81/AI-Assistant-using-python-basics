# 🤖 ALEXA - Python AI Assistant

A simple command-line AI assistant built in Python as part of my learning journey. ALEXA can tell the time, do calculations, fetch live weather updates, crack jokes, play games, and respond to custom voice-like commands.

## 📌 Features

- 🕒 **Tell Time** — Displays the current time
- 🧮 **Calculator** — Performs basic arithmetic (+, -, *, /)
- 🌦 **Weather Report** — Fetches live weather data for any city using OpenWeatherMap API
- 😄 **Jokes** — Tells a random joke using the `pyjokes` library
- 🎮 **Number Guessing Game** — A simple 1–10 guessing game
- 🌐 **Open YouTube** — Opens YouTube directly from the command line
- 💬 **Custom Commands** — Responds to greetings and custom queries

## 🛠 Tech Stack

- **Python 3**
- **Colorama** — for colored terminal output
- **Requests** — for API calls
- **Pyjokes** — for random jokes
- **python-dotenv** — for securely managing API keys

## ⚙️ Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. Install the required libraries
   ```bash
   pip install colorama requests pyjokes python-dotenv
   ```

3. Create a `.env` file in the project folder and add your OpenWeatherMap API key
   ```
   WEATHER_API_KEY=your_api_key_here
   ```

4. Run the assistant
   ```bash
   python alexa.py
   ```

## 💻 Example Commands

| Command                  | Action                          |
|---------------------------|----------------------------------|
| `hello`                   | Greets the user                 |
| `introduce yourself`      | Introduces ALEXA                |
| `tell me time right now`  | Shows current time              |
| `run calculator`          | Opens the calculator             |
| `tell me weather`         | Fetches weather for a city      |
| `make a joke`             | Tells a random joke             |
| `lets play a game`        | Starts number guessing game     |
| `open youtube`            | Opens YouTube in the browser    |
| `exit`                    | Closes the assistant            |

## 📖 What I Learned

- Functions and control flow (if/elif/else, loops)
- Working with external APIs
- Basic error handling
- Handling user input
- Using third-party Python libraries

## 🚀 Future Improvements

- Add voice input/output
- Add more commands and features
- Convert into a GUI-based app
- Deploy as a web app

---

Built as part of my Python learning journey. More projects coming soon! 🚀
