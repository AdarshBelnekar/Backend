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
# Payloads 

## for bogie-checksheet.
-  Api used /api/forms/bogie-checksheet
```bash
{
  "bmbcChecksheet": {
    "adjustingTube": "DAMAGED",
    "cylinderBody": "WORN OUT",
    "pistonTrunnion": "GOOD",
    "plungerSpring": "GOOD"
  },
  "bogieChecksheet": {
    "axleGuide": "Worn",
    "bogieFrameCondition": "Good",
    "bolster": "Good",
    "bolsterSuspensionBracket": "Cracked",
    "lowerSpringSeat": "Good"
  },
  "bogieDetails": {
    "bogieNo": "BG1234",
    "dateOfIOH": "2025-07-01",
    "deficitComponents": "None",
    "incomingDivAndDate": "NR / 2025-06-25",
    "makerYearBuilt": "RDSO/2018"
  },
  "formNumber": "BOGIE-2025-007",
  "inspectionBy": "user_id_456",
  "inspectionDate": "2025-07-03"
}
```

# Output will be
```bash 
{
    "data": {
        "formNumber": "BOGIE-2025-007",
        "inspectionBy": "user_id_456",
        "inspectionDate": "2025-07-03",
        "status": "Saved"
    },
    "message": "Bogie checksheet submitted successfully.",
    "success": true
}
```

# for wheel specificaton
## Api Used 
- /api/forms/wheel-specifications
```bash
{
  "fields": {
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "condemningDia": "825 (800-900)",
    "intermediateWWP": "20 TO 28",
    "lastShopIssueSize": "837 (800-900)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "treadDiameterNew": "915 (900-1000)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "wheelDiscWidth": "127 (+4/-0)",
    "wheelGauge": "1600 (+2,-1)",
    "wheelProfile": "29.4 Flange Thickness"
  },
  "formNumber": "WHEEL-2025-007",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03"
}
```
# output
```bash
{
    "data": {
        "formNumber": "WHEEL-2025-007",
        "submittedBy": "user_id_123",
        "submittedDate": "2025-07-03",
        "status": "Saved"
    },
    "message": "Wheel specification submitted successfully.",
    "success": true
}
```
