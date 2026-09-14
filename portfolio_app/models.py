from django.db import models

# Models define the tables in the database.
# Each class below represents a database table, and each attribute is a column.


class Project(models.Model):
    """Represents a featured project in the portfolio."""

    # A short title for the project.
    title = models.CharField(max_length=120)

    # Example: "SaaS Dashboard" or "Workflow Automation"
    category = models.CharField(max_length=80)

    # Longer description of what the project does.
    summary = models.TextField()

    # A list of technologies used, stored as a simple text string.
    technologies = models.CharField(max_length=200)

    # Optional link to a project page or case study.
    link = models.URLField(blank=True)

    # Flag to mark a project as featured or not.
    featured = models.BooleanField(default=False)

    # Automatically adds the current date/time when the record is first created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SkillCategory(models.Model):
    """Represents a grouping of skills for display on the skills page."""

    # Example: "Frontend", "Backend", or "Operations"
    name = models.CharField(max_length=80)

    # A short description of the category.
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Individual skill item associated with a category."""

    # This links each skill to a category.
    # One category can have many skills, but each skill belongs to only one category.
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")

    # The actual skill name, such as "Python" or "Django".
    name = models.CharField(max_length=80)

    # A label such as "Advanced" or "Intermediate".
    proficiency = models.CharField(max_length=30, default="Advanced")

    def __str__(self):
        return self.name
