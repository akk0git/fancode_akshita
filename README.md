# FanCode User Statistics API

A Flask application that fetches and analyzes user statistics from the JSONPlaceholder API for users in the city **"FanCode."**

* Task : To Automate the Below Scenario.
* Scenario : All the users of City `FanCode` should have more than half of their todos task completed.
* Given User has the todo tasks
* And User belongs to the city FanCode
* Then User Completed task percentage should be greater than 50%

## Features
- *Calculate completed todo percentages*
- *Count posts, comments, albums, and photos for each user*

## Requirements
- **Python 3.12** or similar version
- **Flask**
- **requests**

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/akk0git/fancode_akshita.git
   cd fancode_akshita
##

## Create and Activate a Virtual Environment
2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate 
##


## Install Dependencies
3. **Install requirements from requirements.txt**
   ```bash
   pip install -r requirements.txt
##

## Run the Application
4. **Run application to start Flask**
   ```bash
   python app.py
   
Access at http://127.0.0.1:5000.
##


## Usage
**Fetch user statistics**
   ```bash
   sample curl =>
   curl -X GET http://127.0.0.1:5000/user_statistics
   
   sample response =>
    [
        {
            "album_count": 10,
            "comment_count": 50,
            "completed_percentage": 55.00000000000001,
            "id": 1,
            "name": "Leanne Graham",
            "photo_count": 500,
            "post_count": 10,
            "status": "PASSED"
        },
        {
            "album_count": 10,
            "comment_count": 50,
            "completed_percentage": 60.0,
            "id": 5,
            "name": "Chelsey Dietrich",
            "photo_count": 500,
            "post_count": 10,
            "status": "PASSED"
        },
        {
            "album_count": 10,
            "comment_count": 50,
            "completed_percentage": 60.0,
            "id": 10,
            "name": "Clementina DuBuque",
            "photo_count": 500,
            "post_count": 10,
            "status": "PASSED"
        }
    ]
