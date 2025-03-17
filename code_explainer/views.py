from django.shortcuts import render
import ast
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def code_explainer(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        try:
            # Parse the code to ensure it's valid Python
            ast.parse(code)

            # Use Gemini API to generate an explanation
            explanation = generate_explanation(code)
            return render(request, 'explainer.html', {'code': code, 'explanation': explanation})
        except SyntaxError:
            return render(request, 'explainer.html', {'error': 'Invalid Python code'})
    return render(request, 'explainer.html')

def analyze_code(tree):
    explanations = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            explanations.append(f"Assignment: {ast.unparse(node)}")
        elif isinstance(node, ast.For):
            explanations.append(f"For loop: {ast.unparse(node)}")
        elif isinstance(node, ast.If):
            explanations.append(f"If statement: {ast.unparse(node)}")
        elif isinstance(node, ast.FunctionDef):
            explanations.append(f"Function definition: {ast.unparse(node)}")
    return explanations

def generate_explanation(code):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-lite')
        prompt = f"""
        Analyze the following Python code and provide a detailed and easy-to-understand explanation in the following JSON format (starts with {{ and ends with }}):

        {{
          "overview": "A brief overview of what the code does.",
          "components": [
            {{
              "type": "component_type",
              "description": "A detailed description of this component.",
              "code_snippet": "The relevant part of the code, written as 1 single string preserving any tabs and newlines."
            }},
            // Add more components as needed
          ]
        }}

        Code:
        {code}

        Explanation:
        """
        response = model.generate_content(prompt)
        explanation = response.text
        explanation = re.sub(r'^```json\s*|\s*```$', '', explanation, flags=re.MULTILINE)
        explanation = explanation.strip()

        print(explanation)
        # Parse the JSON-like output into a Python dictionary
        try:
            explanation_dict = json.loads(explanation)
            return explanation_dict
        except json.JSONDecodeError:
            return {"error": "Failed to parse explanation."}
    except Exception as e:
        return {"error": f"Failed to generate explanation: {str(e)}"}