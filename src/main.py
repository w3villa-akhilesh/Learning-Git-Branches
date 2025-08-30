#!/usr/bin/env python3
"""
Sample Python application demonstrating Git branching workflow.

This simple application showcases how to structure a project
and demonstrates the importance of using branches for development.
"""

def greet_user(name: str) -> str:
    """
    Generate a personalized greeting message.
    
    Args:
        name (str): The name of the user to greet
        
    Returns:
        str: A formatted greeting message
    """
    return f"Hello, {name}! Welcome to the Git Branching Demo!"


def display_project_info():
    """Display information about this Git branching demonstration."""
    print("=" * 50)
    print("Git Branching Workflow Demonstration")
    print("=" * 50)
    print("This project demonstrates:")
    print("• Creating feature branches")
    print("• Making meaningful commits")
    print("• Using pull requests for code review")
    print("• Maintaining clean project history")
    print("=" * 50)


def main():
    """Main application entry point."""
    display_project_info()
    
    # Get user input
    user_name = input("Enter your name: ").strip()
    
    if user_name:
        greeting = greet_user(user_name)
        print(f"\n{greeting}")
        print("Thank you for exploring Git branching best practices!")
    else:
        print("No name provided. Have a great day learning Git!")


if __name__ == "__main__":
    main()
