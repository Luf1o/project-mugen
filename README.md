Project Mugen V1.0

Install Commands
 1. virtualenv ./
 2. mugen\Scripts\activate
 3. cd mugen
 4. Test working: - python app.py
 
// ERRORS Found

{% csrf_token %} error might cause error

// Environment variables need to be initiated in a .env file in mugen folder. Make your own keys for groq and tavily

Model Setup
 1. Use pip install -r requirements.txt to install the requirements
 2. Run the program using uvicorn main:app --reload
 3. Go to /docs of the website by typing it in the address bar
 4. Go to post/ask-japan
 5. Click try it out and edit the question key value to infer the model
 6. The model response will be given below in answer key
