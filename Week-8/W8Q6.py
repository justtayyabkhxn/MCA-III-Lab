def count_vowels_in_file(file_path):
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            for char in content:
                if char in vowel_count:
                    vowel_count[char] += 1

        max_vowel = max(vowel_count, key=vowel_count.get)
        max_count = vowel_count[max_vowel]

        return max_vowel, max_count

    except FileNotFoundError:
        return "File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"

file_path = "file3.txt" 
result = count_vowels_in_file(file_path)
print(result)
