# src/app.py
import os

def main():
    
    environment = os.environ.get("ENVIRONMENT", "unknown")
    print(f"Hello, I'm running from the {environment} environment!!")

if __name__ == "__main__":
    main()
