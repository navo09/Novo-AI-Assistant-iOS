# Novo-AI-Assistant-iOS 🚀

An intelligent AI voice assistant named **Novo**, built using Python and Apple Shortcuts. This assistant leverages the power of GitHub's Model Inference API (Azure AI) to provide smart responses and even read the latest news for you.

## 🛠 Features
- **Voice Recognition:** Integrated with Google Speech Recognition.
- **AI Powered:** Uses `gpt-4o-mini` via GitHub Models for fast and accurate responses.
- **Multilingual Support:** Can speak and read news in both **English** and **Bangla**.
- **News Integration:** Fetches real-time headlines using NewsAPI.
- **Music Control:** Custom library to play your favorite tracks.

## ⚙️ Setup & Installation

To run this project, you need to add your own API credentials in the code:

1. **GitHub Token:** 
   - Generate your token from [GitHub Settings](https://github.com/settings/tokens).
   - In `test2for ios Ai assistant.py`, replace the placeholder with your token:
     ```python
     GITHUB_TOKEN = "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN_HERE"
News API Key:

Get your free key from newsapi.org.

Replace the key in the code:
NEWS_API_KEY = "YOUR_NEWS_API_KEY_HERE"
finally before you code run kindly install this.....
3. **Install Dependencies:**
   ```bash
   pip install speech_recognition requests gtts pygame pyttsx3 deep_translator azure-ai-inference


📱 iOS Integration
You can use this with Apple Shortcuts by sending a POST request to the inference endpoint. Make sure to pass your Dictated Text as a JSON body.

👨‍💻 Developer
NAVOJIT BAIDYA

CSE Student at Daffodil International University (DIU).

Aspiring Tech Entrepreneur.
