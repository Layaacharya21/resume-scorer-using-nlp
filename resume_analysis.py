import matplotlib.pyplot as plt
import io
import base64

def analyze_resume(resume, job_description):
    # Placeholder for analysis logic (e.g., keyword matching, etc.)
    keywords = ['Python', 'Flask', 'NLP', 'AI']
    resume_keywords = {kw: resume.count(kw) for kw in keywords}
    job_keywords = {kw: job_description.count(kw) for kw in keywords}

    # Create a plot
    fig, ax = plt.subplots()
    index = range(len(keywords))
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, resume_keywords.values(), bar_width,
                     alpha=opacity, color='b', label='Resume')

    rects2 = plt.bar([p + bar_width for p in index], job_keywords.values(), bar_width,
                     alpha=opacity, color='g', label='Job Description')

    plt.xlabel('Keywords')
    plt.ylabel('Count')
    plt.title('Keyword Analysis')
    plt.xticks([p + bar_width / 2 for p in index], keywords)
    plt.legend()

    # Save plot to a string in base64 format
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    plt.close(fig)
    return 'data:image/png;base64,{}'.format(plot_url)
