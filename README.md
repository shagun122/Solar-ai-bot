# ☀️ Solar Industry AI Assistant  

This is an **AI-powered assistant** that provides expert insights on solar energy, including **solar panel technology, installation, maintenance, cost analysis, regulations, and market trends**.  **https://huggingface.co/spaces/shrishagun/solar-ai-assistant**

🚀 **Powered by OpenRouter API** with **Gemini Flash Lite 2.0 (Free).**  

---

## **🛠 Features**
- 🌞 Provides accurate information about **solar energy**  
- ⚡ Uses **OpenRouter AI (Gemini 2.0 Flash Lite - Free)**  
- 🛡 Secure API key handling with **dotenv**  
- 🎨 Interactive UI with **Streamlit**  

---

## **📌 Installation & Setup (Localhost)**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/solar-ai-assistant.git
cd solar-ai-assistant
```

### **2️⃣ Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
```
Activate the virtual environment:  
- **Windows**:  
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:  
  ```bash
  source venv/bin/activate
  ```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up API Key**
1. Create a **`.env`** file in the project root.  
2. Add your **OpenRouter API Key** inside `.env`:  
   ```bash
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

### **5️⃣ Run the Application**
```bash
streamlit run app.py
```

The app will launch in your browser at **`http://localhost:8501/`** 🎉  

---

## **🚀 Deployment**
### **Deploy on Hugging Face Spaces**
1. Go to **[Hugging Face Spaces](https://huggingface.co/spaces)**  
2. Create a new **Streamlit** space  
3. Upload the following files:
   - `app.py`
   - `requirements.txt`
4. **Set API Key** in **Settings → Secrets**  
5. Restart the space, and it’s live! 🚀  

---

## **🛡 Security Best Practices**
- ✅ **DO NOT** commit your `.env` file  
- ✅ Add `.env` to `.gitignore`:
  ```
  .env
  ```

---

## **👨‍💻 Contributing**
Feel free to fork and submit **pull requests**! Contributions are welcome.  

---

## **📧 Contact**
For issues or suggestions, create a **GitHub Issue** or email **awareindia12@gmail.com**.  

---

🎯 **Now, you're all set to build and deploy your AI-powered Solar Assistant!** ☀️🚀  
