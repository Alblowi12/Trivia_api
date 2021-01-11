# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

API Reference
Getting Started
Backend Base URL: http://localhost:5000/ OR http://127.0.0.1:5000/
Frontend Base URL:http://localhost:3000 OR http://127.0.0.1:3000/
Authentication: Authentication or API keys are not used in the project yet.
Error Handling
Errors are returned in the following json format:

      {
        "success": "False",
        "error": 422,
        "message": "Unprocessable entity",
      }
The error codes currently returned are:

400 – bad request
404 – resource not found
422 – unprocessable
500 – internal server error
Endpoints
GET /category
General:

Returns all the categories.
Sample:  http://127.0.0.1:5000/category

    {
        "categories": {
            "1": "Science", 
            "2": "Art", 
            "3": "Geography", 
            "4": "History", 
            "5": "Entertainment", 
            "6": "Sports"
        }, 
        "success": true
    }
GET /question
General:

Returns all questions
questions are in a paginated.
pages could be requested by a query string
Sample: curl http://127.0.0.1:5000/question

{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 25
}

DELETE /question/int:id\
General:

Deletes a question by id form the url parameter.
Sample: curl http://127.0.0.1:5000/question/33 -X DELETE
{
  "deleted": "33", 
  "success": true
}
POST /question
General:

Creates a new question based on a payload.
Sample: curl http://127.0.0.1:5000/question -X POST -H "Content-Type: application/json" -d '{"question":"What Is The CPU", "answer":"Central Unit Process", "category":1, "difficulty":4}'
{
  "Question is Added": 34, 
  "Success": true
}
POST /question/search
General:

returns questions that has the search substring
Sample: curl http://127.0.0.1:5000/question/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": "CPU"}'
{
  "current_category": null, 
  "questions": [
    {
      "answer": "Central Unit Process", 
      "category": 1, 
      "difficulty": 4, 
      "id": 34, 
      "question": "What Is The CPU"
    }
  ], 
  "success": true, 
  "total_questions": 1
}

GET /category/int:id\/question
General:
Gets questions by category using the id from the url parameter.
Sample: curl http://127.0.0.1:5000/category/5/question
{
  "current_category": [
    "Entertainment"
  ], 
  "question": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "ENT", 
      "category": 5, 
      "difficulty": 1, 
      "id": 30, 
      "question": "ENT"
    }
  ], 
  "success": true, 
  "total_questions": 4
}
POST /quiz
General

Takes the category and previous questions in the request.
Return random question not in previous questions.
Sample: curl http://127.0.0.1:5000/quiz -X POST -H "Content-Type: application/json" -d '{"previous_questions": [3, 3], "quiz_category": {"type": "Science", "id": "1"}}'
{
  "question": {
    "answer": "Central Unit Process", 
    "category": 1, 
    "difficulty": 4, 
    "id": 34, 
    "question": "What Is The CPU"
  }, 
  "success": true
}

Authors
Hatem Alblowi:
my part was Complete the code, editing endpoints and test The endpoints  

Udacity:
provided the starter files  which include backend and frontend folders 