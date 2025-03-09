import argparse

def my_function(option):
    print(f"Function called with option: {option}")

def main():
    parser = argparse.ArgumentParser(description="Process some options.")
    parser.add_argument('option', type=str, help='An option to pass to the function')
    
    args = parser.parse_args()
    
    my_function(args.option)

if __name__ == "__main__":
    main()