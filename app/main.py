import threading
import uvicorn

from api import app
from generator import init_generate_frames

threading.Thread(target=init_generate_frames, daemon=True).start()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
