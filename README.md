Project Purpose

This repository serves as a practical demonstration of building a production-grade CI/CD pipeline from scratch. Rather than just theory, this project showcases real-world DevOps practices through incremental, documented commits that tell the story of building automated workflows.
Why this project exists:

To demonstrate understanding of modern CI/CD workflows
To show practical DevOps skills applicable to real-world scenarios
To practice building reliable, automated deployment pipelines
To maintain a portfolio piece that reflects current industry standards

What This Pipeline Does

Current Features

Automated Linting: Runs flake8 on every push to catch code quality issues
Automated Testing: Executes pytest test suite to ensure code correctness
Continuous Integration: Validates all pull requests before merging
Multi-stage Workflow: Demonstrates proper CI pipeline structure

Roadmap

 Docker Build: Containerize the application and validate Dockerfile
 Image Registry: Push built images to Docker Hub
 Deployment Simulation: Demonstrate deployment workflow (or actual deployment to free tier hosting)
 Versioning & Tagging: Implement semantic versioning for releases
 Status Notifications: Add Slack/Discord notifications for build status
 Security Scanning: Integrate container vulnerability scanning

Tech Stack

CI/CD: GitHub Actions
Containerization: Docker
Language: Python 3.9
Testing: pytest, pytest-flask
Code Quality: flake8
Framework: Flask (simple web app)

Pipeline Workflow

mermaidgraph LR

    A[Push to GitHub] --> B[Checkout Code]
    B --> C[Setup Python]
    C --> D[Install Dependencies]
    D --> E[Lint with flake8]
    E --> F[Run pytest Tests]
    F --> G{Tests Pass?}
    G -->|Yes| H[Build Docker Image]
    G -->|No| I[Pipeline Fails]
    H --> J[Push to Registry]
    J --> K[Deploy/Notify]

Project Structure

ci-pipeline-demo/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions workflow
├── tests/
│   └── test_app.py         # Application tests
├── app.py                  # Simple Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container definition (coming soon)
└── README.md              # This file

Local Development

Prerequisites

Python 3.9+
pip

Setup
bash# Clone the repository
git clone https://github.com/gomezf2/ci-pipeline-demo.git
cd ci-pipeline-demo

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run linter
flake8 .

# Run the application
python app.py
Current Status
Phase: Building CI Foundation (Complete)
Next Step: Docker Integration
This project is being built incrementally with clear, descriptive commits to demonstrate:

Problem-solving process
Debugging CI/CD issues
Best practices in workflow design
Documentation and communication skills

Learning Objectives
Through this project, I'm demonstrating knowledge of:

CI/CD Fundamentals

Pipeline design and implementation
Automated testing and validation
Build automation


DevOps Practices

Infrastructure as Code (GitHub Actions YAML)
Containerization with Docker
Environment management


Software Engineering

Test-driven development
Code quality enforcement
Version control best practices



Key Learnings & Decisions

Problem: pytest ImportError in CI
Solution: Added PYTHONPATH environment variable to workflow
Lesson: CI environments require explicit Python path configuration
Decision: Single requirements.txt
Rationale: Simplicity for demo project; would split for production
Trade-off: Installs dev dependencies in all environments
(More learnings will be documented as the project progresses)
Contributing
While this is primarily a personal learning project, suggestions and feedback are welcome! Feel free to:

Open an issue for discussion
Suggest improvements to the pipeline
Share similar projects or resources

License

MIT License - feel free to use this as a template for your own CI/CD learning projects.
Connect

GitHub: gomezf2
LinkedIn:  https://www.linkedin.com/in/francis-gomez0801/
