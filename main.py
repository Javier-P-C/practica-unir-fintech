import sys


def sort_list(words):
    return sorted(words)


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py palabra1 palabra2 palabra3 ...")
        return

    words = sys.argv[1:]
    sorted_words = sort_list(words)

    print("Palabras ordenadas:")

    print(sorted_words)

    for i in range(len(sorted_words)):
        print(sorted_words[i])



if __name__ == "__main__":
    main()
