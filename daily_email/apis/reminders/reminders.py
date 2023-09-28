from pathlib import Path


def get_message():
    path = Path(__file__).parent / 'todos.txt'  # Get todos.txt from this file's directory
    filename = path.absolute()                  # whether importing or running directly

    with open(filename) as file:
        reminders = file.read().split('\n')

    content = "Remember to:"

    for reminder in reminders:
        content += f"\n- {reminder}"

    return content


if __name__ == '__main__':
    print(get_message())
