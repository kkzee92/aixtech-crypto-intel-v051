"""Paper-only crypto intel demo entrypoint."""
import argparse
from .core.demo import run_demo

def main():
    parser = argparse.ArgumentParser(description="AIxTech crypto intel v0.51 (paper-only)")
    parser.add_argument("command", choices=["demo", "scan"], default="demo")
    args = parser.parse_args()
    if args.command == "demo":
        run_demo()

if __name__ == "__main__":
    main()
