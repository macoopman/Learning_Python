import sys

script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line: # Recursive Base Case
        print_line(line, encoding, errors)

        # recursive call to main()
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # strip() removes the trailing '\n'
    next_lang = line.strip()

    # takes the string and "encodes" it to the give UTF type
    raw_bytes = next_lang.encode(encoding, errors=errors)


    # takes the UTF encoding and decodes it to a string
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes,"<====>", cooked_string)

languages = open("languages.txt", encoding="utf-8")
main(languages, encoding, error)
