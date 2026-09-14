from django.shortcuts import render


def home(request):
    """Render the landing page with overview content and featured projects."""
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

    stats = [
        {"label": "Years learning", "value": "2+"},
        {"label": "Projects built", "value": "8"},
        {"label": "Focus", "value": "Clean"},
    ]

    context = {
        "page_title": "Home",
        "featured_projects": featured_projects,
        "stats": stats,
    }

    return render(request, "portfolio_app/home.html", context)


def profile(request):
    """Render the profile page that summarizes the person behind the portfolio."""
    profile_data = {
        "name": "Troy Thai",
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

    return render(request, "portfolio_app/profile.html", {"page_title": "Profile", "profile": profile_data})


def skills(request):
    """Render the skills page grouped by technology area."""
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

    return render(request, "portfolio_app/skills.html", {"page_title": "Skills", "skill_groups": skill_groups})


def projects(request):
    """Render the projects overview page."""
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

    return render(request, "portfolio_app/projects.html", {"page_title": "Projects", "projects": projects_list})
