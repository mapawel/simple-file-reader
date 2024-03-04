### to start:
(being in project root folder)
* create virtual environment:
`python3 -m venv files-api-venv`
* activate venv:
`.\files-api-venv\Scripts\activate` (windows) or `source files-api-venv/bin/activate` (mac)
* install packages:
`pip install -r requirements.txt`
* run server:
`cd src`, `uvicorn main:app --reload`