def main():
    prompts = ["adjective", "noun", "verb (past tense)", "animal"]

    while True:
        words = {}
        for word_type in prompts:
            words[word_type] = input(f"Give me a {word_type}: ").strip()

        story = f"""
Once upon a time, there was a {words["adjective"]} {words["noun"]}.
One day, it {words["verb (past tense)"]} all the way to the zoo,
where it made friends with a very confused {words["animal"]}.
The end.
"""

        print(story)

        again = input("Generate another story? (y/n): ").strip().lower()
        if again != "y":
            break


main()