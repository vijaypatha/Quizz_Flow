# Requirements for Quiz App

## User Journey / Experience 
1. A user will be prompted with series of true or false questions
2. User responds with true or false 
3. User gets a feedback if the response is correct or incorrect
4. User also gets a feedback on what the correct answer is
5. Upon completion of quiz, user is provided with total score

## What do I Need? 
1. I need questions and answers, a free resource on the internet. 
   * Let's call this as a data
    * Based on the data, I have to build objects 
    
2. To limit the scope, I will build this app for a User/ I will
not store multiple user data.
   

## How do you know which classes and objects to create?

``From the User Jouney.`` 
``1) What does the App have (attributes)`` 
``2) what should it do? ``

### Classes
1. QuizBrain: A class that asks the questions, validates, and scores
2. Not so obvious one: Object for a question. You model the question.
   Right now the data is in a list. Data has two attributes: question and an 
answer. 

### Methods
1. TODO: A user will be prompted with series of true or false questions
   * Two Smaller TODO: 1) Ask a Question 2) Keep asking until all questions are answered.
   
2. TODO: Check if the answer is correct.
   * user_answer == correct_answer
   
### Attributes
1. Question Text
2. Questions Answer
3. Combination of Text and Answer == List of questions