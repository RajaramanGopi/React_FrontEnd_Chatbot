# Krishna Netflix-Style Chatbot UI (React + Vite)

This is a modern, Netflix-inspired chatbot UI built with React and Vite. It connects to your FastAPI backend at `/chat` for AI chat functionality.

sample

## Features
- Beautiful, responsive Netflix-style design
- Chatbot interface with message history
- Connects to FastAPI backend for chat responses

## Getting Started
1. **Install Node.js** (if not already installed)
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Run the app:**
   ```bash
   npm run dev
   ```
4. **Open** [http://localhost:5173](http://localhost:5173) in your browser.

## Configuration
- The backend API URL is set in `src/components/Chatbot.jsx` as `API_URL`. Change it if your FastAPI server runs elsewhere.

## Project Structure
- `src/` - React source code
- `src/components/Chatbot.jsx` - Main chatbot UI logic
- `src/styles.css` - Netflix-style theme

---

**Note:** This UI is ready to connect to your FastAPI backend. Make sure your backend is running and accessible from the frontend.
