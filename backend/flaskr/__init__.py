import os
from flask import Flask, request, abort, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random, json


from models import setup_db, Question, Category 

QUESTIONS_PER_PAGE = 10
def paginate_questions(request, ques):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    que = [question.format() for question in ques]
    cur_que = que[start:end]

    return cur_que
    
QUESTIONS_PER_CATG = 10
def paginate_categories(request, cat):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_CATG
    end = start + QUESTIONS_PER_CATG

    catg = [catg.type for catg in cat]
    cur_cat = catg[start:end]

    return cur_cat   

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  app.config['JSON_SORT_KEYS'] = True 
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response


  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/category', methods=['GET'])
  def get_cat():
        catg = Category.query.order_by(Category.id).all()
        return jsonify({
            'success':True,
            'categories': {catg2.id: catg2.type for catg2 in catg}

        })

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  @app.route('/question', methods=['GET'])
  def retrieve_question():
        ques = Question.query.order_by(Question.id).all()
        cur = paginate_questions(request, ques)

        cat = Category.query.order_by(Category.type).all()
  
        if len(cur) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': cur,
            'total_questions': len(ques),
            'categories': {c.id: c.type for c in cat},
            'current_category': None
        })
  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  @app.route('/question', methods=['POST'])
  def add_ques():
      body = request.get_json()
      try:
            if ('question' in body and 'answer' in body and 'difficulty' in body and 'category' in body):
                  qn = body.get('question')
                  an = body.get('answer')
                  dif = body.get('difficulty')
                  cat = body.get('category')

                  que = Question(question=qn, answer=an,difficulty=dif, category=cat)
                  que.insert()

                  return jsonify({
                         'Success': True,
                         'Question is Added': que.id
                    })
            else:
                   return abort(404)
      except:
               abort(422)




  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''

  @app.route('/category/<int:category_id>/question', methods=['GET'])
  def get_ct(category_id):
      ct = Category.query.filter(Category.id == category_id).all()
      qe = Question.query.filter(Question.category==category_id).all()
      cnt = paginate_categories(request, ct)
      q = paginate_questions(request, qe)
      if len(cnt) == 0:
            abort(404)                      
      else:          
            return jsonify({
            'success':True,
            'total_questions': len(qe),
            'question': [qs.format() for qs in qe],
            'current_category': cnt
            })
  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(400)
  def bad_request(error):
        return jsonify ({
              "success": False,
              "error": 400,
              "message": "Bad Request"
        }), 400

  @app.errorhandler(404)
  def not_found(error):
        return jsonify ({
              "success": False,
              "error": 404,
              "message": "Not Found"
        }), 404

  @app.errorhandler(405)
  def method_not_allowed(error):
        return jsonify({
              "success": False,
              "error": 405,
              "message": "Method Is Not Allowed"
        }), 405


  @app.errorhandler(422)
  def unprocessable(error):
        return jsonify({
              "success": False,
              "error": 422,
              "message": "Cannot be Process"
        }), 422
          



   
  return app

    