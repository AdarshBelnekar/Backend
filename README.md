#  FastAPI + PostgreSQL with Docker Compose

This project sets up a FastAPI backend and a PostgreSQL database using Docker Compose.

---

 ## Create and Activate a Virtual Environment
 ```bash
python3 -m venv venv
```
>On windows only
```bash
venv\Scripts\activate
```
## Install dependencies 
```bash
pip install -r requirements.txt
```
##  Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/)
- `.env` file with credentials (see below)

---

## ⚙️ Setup Instructions

### 1. Create `.env` file

>  **Important:** Do **not** commit this file to GitHub.

Create a `.env` file in the root folder:

```env
POSTGRES_DB=your database name
POSTGRES_USER=your user name
POSTGRES_PASSWORD=your password
DATABASE_URL=postgresql:your data base url 
```
## Run the application
```bash
docker-compose up --build
```

