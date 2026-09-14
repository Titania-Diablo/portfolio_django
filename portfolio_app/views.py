from django.shortcuts import render

# Views are Python functions that handle page requests.
# Each view prepares data and sends it to an HTML template.


def home(request):
    """Render the landing page with overview content and featured projects."""
    # ------------------------------------------------------------------
    # EDITABLE SECTION: homepage project cards
    # Update the titles, summaries, tech stacks, and links below for your own portfolio.
    # ------------------------------------------------------------------
    featured_projects = [
        {
            "title": "Portfolio Website",
            "category": "Personal Brand",
            "summary": "A clean portfolio experience focused on clarity, thoughtful design, and easy navigation.",
            "technologies": "Python, Django, HTML, CSS",
            "link": "https://example.com",
        },
        {
            "title": "Task Tracker",
            "category": "Productivity",
            "summary": "A simple tool for organizing work, priorities, and progress in a focused workflow.",
            "technologies": "Django, SQLite, Bootstrap",
            "link": "https://example.com",
        },
        {
            "title": "Learning Log",
            "category": "Growth",
            "summary": "A personal space for notes, milestones, and reflection while building new skills.",
            "technologies": "Python, Django, Templates",
            "link": "https://example.com",
        },
    ]

    # ------------------------------------------------------------------
    # EDITABLE SECTION: homepage stats
    # Change values like years, project count, or focus to match your own story.
    # ------------------------------------------------------------------
    stats = [
        {"label": "Years learning", "value": "2+"},
        {"label": "Projects built", "value": "8"},
        {"label": "Focus", "value": "Clean"},
    ]

    # This dictionary passes data into the template.
    context = {
        "page_title": "Home",
        "featured_projects": featured_projects,
        "stats": stats,
    }

    # The render() function combines the template with the data and sends the result to the browser.
    return render(request, "portfolio_app/home.html", context)


def profile(request):
    """Render the profile page that summarizes the person behind the portfolio."""
    # ------------------------------------------------------------------
    # EDITABLE SECTION: profile information
    # Change your name, title, location, summary, and highlights here.
    # ------------------------------------------------------------------
    profile_data = {
        "name": "Your Name",
        "role": "Developer • Builder • Problem Solver",
        "location": "Available for new opportunities",
        "summary": (
            "I build practical digital products with a focus on clarity, usability, and thoughtful execution. "
            "I enjoy turning ideas into simple, useful experiences that people can actually use."
        ),
        "highlights": [
            "Builds clean and useful web experiences.",
            "Turns ideas into working software.",
            "Improves through iteration and learning.",
        ],
    }

    # The view sends the profile dictionary to the profile template.
    return render(request, "portfolio_app/profile.html", {"page_title": "Profile", "profile": profile_data})


def skills(request):
    """Render the skills page grouped by technology area."""
    # ------------------------------------------------------------------
    # EDITABLE SECTION: skills
    # Update the categories, descriptions, and technology items below.
    # ------------------------------------------------------------------
    skill_groups = [
        {
            "name": "Frontend",
            "description": "Clean interfaces and responsive user experiences.",
            "items": ["HTML5", "CSS3", "JavaScript", "Responsive Design", "Django Templates"],
        },
        {
            "name": "Backend",
            "description": "Application logic and data-driven functionality.",
            "items": ["Python", "Django", "REST APIs", "SQLite", "Problem Solving"],
        },
        {
            "name": "Working Style",
            "description": "How I approach learning and building.",
            "items": ["Debugging", "Version Control", "Testing", "Documentation", "Iteration"],
        },
    ]

    # The template loops through each group and displays its skills in cards.
    return render(request, "portfolio_app/skills.html", {"page_title": "Skills", "skill_groups": skill_groups})


def projects(request):
    """Render the projects overview page."""
    # ------------------------------------------------------------------
    # EDITABLE SECTION: project list
    # Replace these entries with your own projects and technology stacks.
    # ------------------------------------------------------------------
    projects_list = [
        {
            "title": "Portfolio Website",
            "category": "Personal Brand",
            "summary": "A polished site for showcasing skills, work, and projects with a modern, easy-to-read layout.",
            "technologies": "Django, HTML, CSS, Python",
        },
        {
            "title": "Task Tracker",
            "category": "Productivity",
            "summary": "A simple productivity dashboard that organizes tasks, deadlines, and personal goals in one place.",
            "technologies": "Python, Django, SQLite, Bootstrap",
        },
        {
            "title": "Learning Log",
            "category": "Growth",
            "summary": "A journal-style application that helps capture lessons learned, project notes, and technical progress.",
            "technologies": "Django, Templates, CSS, JavaScript",
        },
        {
            "title": "Client Intake Tool",
            "category": "Operations",
            "summary": "A lightweight form-driven tool for collecting requests, organizing incoming work, and reducing manual admin.",
            "technologies": "Django, Forms, SQLite, Python",
        },
    ]

    # A template can loop over this list and generate a project row for each item.
    return render(request, "portfolio_app/projects.html", {"page_title": "Projects", "projects": projects_list})


def learning(request):
    """Render a beginner learning page that shows how Django concepts work in practice."""
    concepts = [
        {
            "title": "URL routing",
            "description": "A URL like /learning/ points to a Python function, which decides what the page should show.",
        },
        {
            "title": "Views",
            "description": "Views prepare data and pass it to the template. This is the logic layer of Django.",
        },
        {
            "title": "Templates",
            "description": "Templates display the data using HTML and Django template tags like {{ name }} and {% for %}.",
        },
        {
            "title": "Models",
            "description": "Models define the database structure for records like projects, skills, or blog posts.",
        },
    ]

    checklist = [
        "Create a route in urls.py",
        "Write a view function in views.py",
        "Add a template file in templates",
        "Pass data from Python to the template",
        "Loop through data with {% for %}",
    ]

    return render(
        request,
        "portfolio_app/learning.html",
        {
            "page_title": "Learning",
            "concepts": concepts,
            "checklist": checklist,
        },
    )
