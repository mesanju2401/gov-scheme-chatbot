# 🏛️ Government Scheme Chatbot

A simple AI-powered chatbot to help users find information about government schemes, eligibility criteria, and application processes.

## 📁 Project Structure

```
gov-scheme-chatbot/
├── backend/              # Flask API backend
│   ├── app.py           # Main backend application
│   ├── requirements.txt # Python dependencies
│   └── .env            # Backend environment variables
├── frontend/            # Frontend application
│   └── chatbot.html    # Single-file complete frontend
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🚀 Quick Start

### Backend Setup

1. **Install Python dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file in the `backend` folder:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Run the backend:**
   ```bash
   python app.py
   ```
   Backend runs at: `http://localhost:5000`

### Frontend Setup

1. **Open `frontend/chatbot.html` in a text editor**

2. **Update the API URL (Line 187):**
   ```javascript
   const API_URL = 'http://localhost:5000/api/chat';  // For local testing
   ```

3. **Test locally:**
   - Double-click `chatbot.html` to open in browser
   - Or open with Live Server in VS Code

## 🌐 Deployment

### Deploy Backend to Render

1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Root Directory:** `backend`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add environment variable: `OPENAI_API_KEY`
6. Click "Deploy"
7. Copy your backend URL (e.g., `https://your-app.onrender.com`)

### Deploy Frontend

#### Option 1: Netlify Drop (Easiest - No Account Needed!)

1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag and drop `frontend/chatbot.html`
3. Get instant live URL!
4. **Important:** Update the API URL in `chatbot.html` to your Render backend URL before uploading

#### Option 2: GitHub Pages

1. **Update API URL in `chatbot.html`:**
   ```javascript
   const API_URL = 'https://your-backend.onrender.com/api/chat';
   ```

2. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/gov-scheme-chatbot.git
   git push -u origin main
   ```

3. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from branch `main`
   - Folder: `/ (root)`
   - Save

4. **Access your site:**
   ```
   https://yourusername.github.io/gov-scheme-chatbot/frontend/chatbot.html
   ```

#### Option 3: Vercel

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   cd frontend
   vercel
   ```

3. Follow the prompts and get your live URL!

## 🔧 Configuration

### Update Backend URL

Before deploying frontend, update the API URL in `frontend/chatbot.html` (line 187):

```javascript
// For local development
const API_URL = 'http://localhost:5000/api/chat';

// For production (after deploying backend)
const API_URL = 'https://your-backend.onrender.com/api/chat';
```

### CORS Configuration

If you get CORS errors, make sure your backend has CORS enabled for your frontend URL:

```python
from flask_cors import CORS

CORS(app, origins=[
    "http://localhost:3000",
    "https://your-frontend-url.netlify.app"
])
```

## 🛠️ Technologies Used

**Backend:**
- Python 3.x
- Flask
- OpenAI API
- Flask-CORS

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript
- No frameworks or build tools needed!

## 📝 API Endpoints

### POST `/api/chat`

Send a message to the chatbot.

**Request:**
```json
{
  "message": "What is PM-KISAN scheme?"
}
```

**Response:**
```json
{
  "response": "PM-KISAN is a government scheme that provides..."
}
```

## 🐛 Troubleshooting

### Frontend can't connect to backend
- ✅ Check if backend is running
- ✅ Verify API URL in `chatbot.html` is correct
- ✅ Check browser console for errors
- ✅ Ensure CORS is enabled on backend

### CORS Error
- ✅ Add your frontend URL to CORS origins in backend
- ✅ Restart backend after changes

### Backend not responding
- ✅ Check if OpenAI API key is set correctly
- ✅ Check backend logs for errors
- ✅ Verify requirements are installed

## 📄 License

MIT License - Feel free to use this project for your needs!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

If you have any questions or issues, please open an issue on GitHub.

---

Made with ❤️ for better government scheme accessibility
