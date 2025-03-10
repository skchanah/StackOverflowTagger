import argparse
from transformers import pipeline

def my_function(query):
    option = str(query).lower()
    clf = pipeline("text-classification",model="eugeneskchan/stackoverflow_tagger_bert")
    result = clf(query, top_k=6)
    output = [r['label'] for r in result if r['score'] > 0.8]
    print(output)

def main():
    parser = argparse.ArgumentParser(description="Process some options.")
    parser.add_argument('--query', type=str, help='An option to pass to the function')
    
    args = parser.parse_args()
    try:
        #print(args.query)
        my_function(args.query)
    except AttributeError:
        print("Please enter a single line question.")

if __name__ == "__main__":
    main()