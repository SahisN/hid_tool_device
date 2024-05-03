import curses
import time
from modules.reader import ReadJson
from modules.writer import Writer


def display_elements(stdscr, accounts, current_selection):
    # Clear screen
    stdscr.clear()

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

    # Display the list of accounts
    for i, account in enumerate(accounts):
        if i == current_selection:
            # Display selected account with '>' symbol and blue color
            stdscr.addstr(i, 0, "> " + account, curses.color_pair(1))
        else:
            # Display non-selected accounts
            stdscr.addstr(i, 0, "  " + account)

    # Refresh the screen
    stdscr.refresh()


def main(stdscr):
    while True:
        main_screen = display(stdscr, ["Password Manager", "Wireless keyboard", "Quit"])

        if main_screen == "Quit":
            return

        elif main_screen == "Password Manager":
            account_screen(stdscr)


def account_screen(stdscr):
    # load in json data
    json_reader = ReadJson()

    # get account list from json
    account_list = json_reader.get_accounts()

    while True:
        account = display(stdscr, account_list)
        # check if user wants to go back
        if account == "Back":
            return

        else:
            username_screen(
                stdscr=stdscr,
                account=account,
                json_reader=json_reader,
            )


def username_screen(stdscr, account, json_reader: ReadJson):
    # get username list from json depending on account list
    username_list = json_reader.get_usernames(account_type=account)

    while True:
        username = display(stdscr, username_list)

        # check if user wants to go back
        if username == "Back":
            return

        else:
            password = json_reader.get_password(account_type=account, username=username)
            inject(stdscr, username, password)


def display(stdscr, item_list):
    stdscr.clear()

    # List of accounts
    current_selection = 0

    while True:
        # Display accounts
        display_elements(stdscr, item_list, current_selection)

        # Get user input
        key = stdscr.getch()

        # Handle user input
        if key == curses.KEY_UP:
            # Move selection up
            current_selection = (current_selection - 1) % len(item_list)

        elif key == curses.KEY_DOWN:
            # Move selection down
            current_selection = (current_selection + 1) % len(item_list)

        elif key == ord("\n"):
            # current_list = accounts_option
            return item_list[current_selection]


def inject(stdscr, account_name, password):
    # clear the screen
    stdscr.clear()
    stdscr.refresh()

    # notify user about injection
    stdscr.addstr(
        f"Injecting {account_name}'s password in 3 seconds... password: {password}"
    )
    stdscr.refresh()

    # wait before injection
    time.sleep(3)

    # load in writer
    Writer.type_string(password)


if __name__ == "__main__":
    # Run the application
    curses.wrapper(main)
