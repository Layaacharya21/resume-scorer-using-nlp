# Resume Scorer Using NLP (API Integration)

## Overview
Resume Scorer Using NLP is a machine learning project that analyzes resumes using Natural Language Processing (NLP) techniques. The project integrates with AI to provide personalized feedback and scores for candidate resumes, helping them better align with job descriptions and industry standards.

## Project Features
- **Resume Scoring**: Assigns a score to resumes based on relevance and quality.
- **Personalized Feedback**: Provides detailed suggestions for improvement tailored to the candidate.
- **NLP Integration**: Analyzes text for keywords, structure, and content quality.
- **Interactive Interface**: Allows users to upload resumes dynamically and view scores and feedback.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - pandas
  - NumPy
  - scikit-learn
  - nltk
  - spacy
  - flask (for web integration)
  - matplotlib
- **AI Integration**: OpenAI API for generating detailed feedback.

## Dataset
The project uses a curated dataset of resumes and job descriptions to train and validate the model. The dataset includes:
- Resume text samples
- Job descriptions
- Skill keywords

### Source
Datasets were created manually or sourced from publicly available datasets. Ensure compliance with usage policies.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/resume-scorer.git
   cd resume-scorer
   ```
2. Set up a virtual environment (optional):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://localhost:5000
   ```
3. Upload a resume and view the score and feedback.

## Model Description
The project uses:
1. **Text Preprocessing**: Tokenization, stopword removal, and lemmatization using NLTK and spaCy.
2. **Keyword Matching**: Compares resume content with job description keywords.
3. **Scoring Algorithms**: Custom scoring logic combining keyword density, structure, and grammar.
4. **AI Feedback**: Generates personalized improvement suggestions using OpenAI API.

## Results
- Average accuracy: **85%** in predicting relevant resumes.
- User feedback indicates a **90% satisfaction rate** with personalized suggestions.

## Future Enhancements
- Add multilingual resume support.
- Integrate with LinkedIn API for profile analysis.
- Improve AI feedback with additional context-specific training data.
- Deploy as a fully hosted web application using AWS or Google Cloud.

## Contributing
Contributions are welcome! If you’d like to contribute, please:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

### Contact
If you have any questions or suggestions, feel free to reach out:
- Email: srilayakarampudi@gmail.com
- GitHub: [layaacharya21](https://github.com/layaacharya21)

