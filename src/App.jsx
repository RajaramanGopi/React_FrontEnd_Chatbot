import React, { useState, useRef, useEffect } from 'react';
import Chatbot from './components/Chatbot';

export default function App() {
  return (
    <div className="app-bg">
      <header className="app-header">
        <h1>Krishna Chatbot</h1>
        <p className="subtitle">Netflix-style AI Assistant</p>
      </header>
      <main>
        <Chatbot />
      </main>
    </div>
  );
}
