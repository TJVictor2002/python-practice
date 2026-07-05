def main():
    adjective = input("Give me an adjective: ").strip()
    noun = input("Give me a noun: ")
    verb = input("Give me a verb (past tense): ")
    animal = input("Give me an animal: ")

    story = f"""
Once upon a time, there was a {adjective} {noun}.
One day, it {verb} all the way to the zoo,
where it made friends with a very confused {animal}.
The end.
"""

    print(story)


main()