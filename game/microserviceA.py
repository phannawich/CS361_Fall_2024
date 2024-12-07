import time

INFILE1 = 'prompt.txt'
INFILE2 = 'user_input.txt'
OUTFILE = 'compared_result.txt'


def main():
    while True:
        word_array1 = file_to_array(INFILE1)
        word_array2 = file_to_array(INFILE2)
        if len(word_array1) > 0 or len(word_array2) > 0:
            output = count_matching_words(word_array1,word_array2)
            write_output(output,OUTFILE)
        time.sleep(0.5)


def count_matching_words(array1, array2):
    shortest_array_length = min(len(array1), len(array2))
    longest_array_length = max(len(array1), len(array2))
    i = 0
    num_matches = 0
    while i < shortest_array_length:
        arr1_word = array1[i]
        arr2_word = array2[i]
        if arr1_word.lower() == arr2_word.lower():
            num_matches += 1
        i += 1
    return [num_matches, longest_array_length]


def file_to_array(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return words
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []


def write_output(array, file_path):
    if len(array) == 2:
        result = f"{array[0]}/{array[1]}"
        try:
            with open(file_path, 'w') as file:
                file.write(result)
            print(f"Successfully written to {file_path}: {result}")
        except Exception as e:
            print(f"Error writing to file {file_path}: {e}")
    else:
        print("The array should have exactly two values.")


if __name__ == "__main__":
    main()
