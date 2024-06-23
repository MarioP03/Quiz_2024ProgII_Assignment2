import os
import sys

# Code that sets entrypoint in a django project. Running this file (executing from command line) starts the server
# on localhost, or otherwise prints an error message that lets the user know, they have no Django installed,
# or venv activated.
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()