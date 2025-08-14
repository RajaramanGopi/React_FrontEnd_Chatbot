# Code Citations

## License: unknown
https://github.com/lasfito/tutoriales/tree/22d7b9ac2ddc14676857b202e2063855449091e3/42-email-firebase/src/main.jsx

```
React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode
```


## License: unknown
https://github.com/DavidBennet/React-challenge-1/tree/263bbd41c9f014c7e004f210153e13671058a698/src/main.jsx

```
ReactDOM from 'react-dom/client';
import App from './App';
import './styles.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </
```

## License: unknown
https://github.com/yourusername/yourproject/blob/main/main.py

```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    # Dummy response
    return {"response": f"You said: {user_message}"}
```

