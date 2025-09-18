# Running the project in PyCharm (step-by-step)

## Backend (FastAPI)
1. Open PyCharm and choose **Open** -> select the `backend` folder inside the project.
2. Create a new Python interpreter (virtual environment):
   - Settings -> Project -> Python Interpreter -> Add -> Virtualenv Environment.
   - Set Base interpreter to Python 3.9+ and create the venv in the project (e.g., `backend/.venv`).
3. Install dependencies:
   - Open Terminal in PyCharm (bottom pane) and run:
     ```bash
     source .venv/bin/activate   # or .venv\\Scripts\\activate on Windows
     pip install -r requirements.txt
     ```
4. Create a Run Configuration to start the backend:
   - Run -> Edit Configurations -> Add -> Python.
   - Name: `uvicorn (dev)`
   - Script path: the `uvicorn` executable inside the venv (e.g., `backend/.venv/bin/uvicorn`), or use the module option:
     - Module name: `uvicorn`
     - Parameters: `app.main:app --reload --port 8000 --host 0.0.0.0`
     - Working directory: `<project>/backend`
     - Environment variables: (optional) `USE_REAL_CAPTURE=1` to enable real capture
   - Apply and Run the configuration. PyCharm will start the backend and show logs.

## Frontend (React)
1. Open a new PyCharm window/project and open the `frontend` folder (or use the same project and create a new Node.js run configuration).
2. Ensure Node.js is installed on your machine.
3. Install dependencies:
   - Open Terminal and run `npm install` in the `frontend` folder.
4. Create a new **npm** run configuration or simply use the terminal:
   - `npm start` will run the dev server (http://localhost:3000).

Now open the browser at `http://localhost:3000` to view the dashboard; API calls go to `http://localhost:8000`.

