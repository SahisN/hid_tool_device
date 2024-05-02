import curses
import time


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


# ["Google", "Amazon", "Twitter", "Back"]


def main(stdscr):
    while True:
        main_screen = display(stdscr, ["Password Manager", "Wireless keyboard", "Quit"])

        if main_screen == "Quit":
            return

        elif main_screen == "Password Manager":
            account_screen(stdscr)


def account_screen(stdscr):
    while True:
        account = display(stdscr, ["Google", "Amazon", "Twitter", "Back"])
        # check if user wants to go back
        if account == "Back":
            return

        else:
            option(stdscr=stdscr, option_list=["Inject", "Back"], account=account)


def option(stdscr, option_list, account):
    while True:
        option = display(stdscr, option_list)

        # check if user wants to go back
        if option == "Back":
            return

        else:
            # fetch password based on the account selection
            inject(stdscr, account_name=account)


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


def inject(stdscr, account_name):
    global timer
    stdscr.clear()
    stdscr.refresh()

    stdscr.addstr(f"Injecting {account_name}'s password in 3 seconds")
    stdscr.refresh()
    time.sleep(3)
    return


if __name__ == "__main__":
    # Run the application
    curses.wrapper(main)
