
import json

if __name__ == "__main__":
    # Read the dictionary file and parse it
    dictionary = {}

    with open('harvard_meddict.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and ':' in line:  # Skip empty lines
                # Split on the first colon only
                term, definition = line.split(':', 1)
                dictionary[term.strip()] = definition.strip()

    # Convert to list of objects with term and explanation keys
    entries = [
        {"term": term, "explanation": definition}
        for term, definition in dictionary.items()
    ]

    # Write to JSON file
    with open('harvard_meddict.json', 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

    print(f"Converted {len(dictionary)} terms to JSON")
