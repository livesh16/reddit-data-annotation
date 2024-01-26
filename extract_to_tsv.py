from pathlib import Path
import json
import random
import csv
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", required=True, help="Output tsv file")
    parser.add_argument("input_file", help="Input json file")
    parser.add_argument("num_posts_to_output", help="Number of posts to output")

    args = parser.parse_args()

    output_file = args.output
    input_file = args.input_file
    num_posts_to_output = int(args.num_posts_to_output)

    fpath = Path(input_file)

    with open(fpath, "r") as f:
        data = json.load(f)

    data = data["data"]["children"]

    if num_posts_to_output < len(data):
        # Generate a list of unique n random integers
        random_integers = random.sample(range(0, len(data)), num_posts_to_output)
        new_data = []
        for i in random_integers:
            new_data.append(data[i])
        data = new_data

    names_titles = [] # A 2D list. The inner list is of the form [name, title] except the first element which is the header
    names_titles.append(["Name", "Title", "Coding"])

    for d in data:
        new_element = [d["data"]["name"], d["data"]["title"]]
        names_titles.append(new_element)

    print(names_titles)


    # Open the file in write mode with newline='' to prevent extra newline characters
    with open(output_file, 'w', newline='', encoding='utf-8') as tsvfile:
        # Create a CSV writer with tab as the delimiter
        writer = csv.writer(tsvfile, delimiter='\t')

        # Write the data to the TSV file
        writer.writerows(names_titles)



if __name__ == "__main__":
    main()

# python3 extract_to_tsv.py -o annotated_mcgill.tsv mcgill.json 50