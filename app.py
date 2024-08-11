from flask import Flask, render_template, request
import google.generativeai as palm
import re
from resume_analysis import analyze_resume

app = Flask(__name__)

# Google AI Studio API key (replace with your own key)
palm.configure(api_key='AIzaSyA2v6FZWoM4UgNYVzFYjRCqOmph5NxmsQs')
def generate_feedback_and_score(resume, job_description):
    prompt = f"Resume: {resume}\nJob Description: {job_description}\nProvide personalized feedback and a score out of 100:"
    response = palm.chat(messages=[{"content": prompt}])
    result = response.last

    # Debugging step to print the result
    print(f"Result from AI API: {result}")

    # Initialize score with a default value
    score = 0

    # Extract score using regex (update pattern if needed)
    score_match = re.search(r'(?i)score.*?(\d+)', result)
    if score_match:
        score = int(score_match.group(1))
    else:
        print("No score found in the result")  # Print message for debugging

    # Extract feedback by removing the score part
    feedback_start = result.find("**Overall Score:**")
    feedback = result[:feedback_start].strip() if feedback_start != -1 else result

    print(f"Extracted Score: {score}")  # Print score for debugging
    print(f"Extracted Feedback: {feedback}")

    return feedback, score




    return feedback, score


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        resume = request.form['resume']
        job_description = request.form['job_description']
        feedback, score = generate_feedback_and_score(resume, job_description)
        
        # Analyze resume and generate plot
        plot_url = analyze_resume(resume, job_description)
        
        return render_template('result.html', feedback=feedback, score=score, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
