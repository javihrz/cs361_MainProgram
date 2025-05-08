import pandas as pd
import random
from colorama import Fore, Style

header = ("\n-- New York Restaurant Recommender --\n\n"
          "Hello! This service is to help you decide which restaurant \n"
          "to try from a list of restaurants in New York. \n"
          "The following section shows the current options available. \n"
          "Please type and submit a letter to get your desired results. Thank you! \n")

input_options_1 = (Fore.CYAN + "---------------------------------------\n" + Style.RESET_ALL +
                   "--- Keyboard input options 1 ---\n\n"
                   "Show full list of restaurants:  " + Fore.CYAN + "'e' \n" + Style.RESET_ALL +
                   "Generate a random restaurant:   " + Fore.CYAN + "'r' \n" + Style.RESET_ALL +
                   "Search new list of restaurants: " + Fore.CYAN + "'s' \n\n" + Style.RESET_ALL +
                   "Get functions information:      " + Fore.CYAN + "'i' \n" + Style.RESET_ALL +
                   "Quit program:                   " + Fore.CYAN + "'q' \n"
                   "---------------------------------------" + Style.RESET_ALL)

input_options_2 = (Fore.CYAN + "---------------------------------------\n" + Style.RESET_ALL +
                   "--- Keyboard input options 1 ---\n\n"
                   "Generate a random restaurant:   " + Fore.CYAN + "'r' \n" + Style.RESET_ALL +
                   "Search new list of restaurants: " + Fore.CYAN + "'s' \n" + Style.RESET_ALL +
                   "Filter current list down:       " + Fore.CYAN + "'f' \n\n" + Style.RESET_ALL +
                   "Get functions information:      " + Fore.CYAN + "'i' \n" + Style.RESET_ALL +
                   "Quit program:                   " + Fore.CYAN + "'q' \n"
                   "---------------------------------------" + Style.RESET_ALL)

input_options_3 = (Fore.CYAN + "---------------------------------------\n" + Style.RESET_ALL +
                   "--- Keyboard input options 1 ---\n\n"
                   "Reset full list of restaurants: " + Fore.CYAN + "'e'\n" + Style.RESET_ALL +
                   "Generate a random restaurant:   " + Fore.CYAN + "'r' \n" + Style.RESET_ALL +
                   "Search new list of restaurants: " + Fore.CYAN + "'s' \n" + Style.RESET_ALL +
                   "Filter current list down:       " + Fore.CYAN + "'f' \n\n" + Style.RESET_ALL +
                   "Get functions information:      " + Fore.CYAN + "'i' \n" + Style.RESET_ALL +
                   "Quit program:                   " + Fore.CYAN + "'q' \n"
                   "---------------------------------------" + Style.RESET_ALL)

input_options_4 = (Fore.CYAN + "---------------------------------------\n" + Style.RESET_ALL +
                   "--- Keyboard input options 1 ---\n\n"
                   "Reset full list of restaurants:  " + Fore.CYAN + "'e'\n" + Style.RESET_ALL +
                   "Generate a random restaurant:    " + Fore.CYAN + "'r' \n" + Style.RESET_ALL +
                   "Search new list of restaurants:  " + Fore.CYAN + "'s' \n" + Style.RESET_ALL +
                   "Edit current filtration options: " + Fore.CYAN + "'w' \n\n" + Style.RESET_ALL +
                   "Get functions information:       " + Fore.CYAN + "'i' \n" + Style.RESET_ALL +
                   "Quit program:                    " + Fore.CYAN + "'q' \n"
                   "---------------------------------------" + Style.RESET_ALL)

search_options_1 = (Fore.CYAN + "---------------------------------------\n" + Style.RESET_ALL +
                    "--- Keyboard input options 2 ---\n\n"
                    "Cuisine type: " + Fore.CYAN + "'c' \n\n" + Style.RESET_ALL +
                    "Quit program: " + Fore.CYAN + "'q' \n\n"
                    "---------------------------------------" + Style.RESET_ALL)

search_options_2 = (Fore.CYAN + "---------------------------------------\n" + Style.RESET_ALL +
                    "--- Keyboard input options 3 ---\n\n"
                    "Note: Applying a new search will clear the current\n"
                    "selection, and generate a new list.\n\n"
                    "Dessert:      " + Fore.CYAN + "'1' \n" + Style.RESET_ALL +
                    "Italian:      " + Fore.CYAN + "'2' \n" + Style.RESET_ALL +
                    "Thai:         " + Fore.CYAN + "'3' \n\n" + Style.RESET_ALL +
                    "Quit program: " + Fore.CYAN + "'q' \n\n"

                    "---------------------------------------" + Style.RESET_ALL)

filter_options_1 = (Fore.CYAN + "---------------------------------------\n" + Style.RESET_ALL +
                    "--- Keyboard input options 2 ---\n\n"
                    "Note: More than one filtration option can be\n"
                    "applied by using commas (Ex: '1,2').\n\n"
                    "Low cost ($):      " + Fore.CYAN + "'1' \n" + Style.RESET_ALL +
                    "Average cost ($$): " + Fore.CYAN + "'2' \n" + Style.RESET_ALL +
                    "High cost ($$$):   " + Fore.CYAN + "'3' \n\n" + Style.RESET_ALL +
                    "Quit program:      " + Fore.CYAN + "'q' \n\n"
                    "---------------------------------------" + Style.RESET_ALL)

functions_information = (Fore.CYAN + "\nShow full list of restaurants / "
                                     "Reset full list of restaurants\n" + Style.RESET_ALL +
                         "    Press 'e' and enter. The current list is cleared, and\n"
                         "    a new list that contains all restaurants from the\n"
                         "    source file is loaded.\n\n"

                         + Fore.CYAN + "Filter current list of restaurants\n" + Style.RESET_ALL +
                         "    Press 'f' and enter. The current list is narrowed down\n"
                         "    to match the user's preference.\n\n"

                         + Fore.CYAN + "Generate a random restaurant\n" + Style.RESET_ALL +
                         "    Press 'r' and enter. The current list is cleared, and \n"
                         "    a single restaurant (picked at random) is displayed.\n\n"
                         
                         + Fore.CYAN + "Search new list of restaurants\n" + Style.RESET_ALL +
                         "    Press 's' and enter. The current list is cleared, and\n"
                         "    the program finds restaurants that match the user's\n"
                         "    search criteria to generate a new list.\n\n"

                         + Fore.CYAN + "Edit current filtration options\n" + Style.RESET_ALL +
                         "    Press 'w' and enter. The current list is cleared, and\n"
                         "    the pre-filtered list is re-filtered with the new\n"
                         "    criteria and displayed to the user.\n\n"

                         + Fore.CYAN + "Quit and close the program\n" + Style.RESET_ALL +
                         "    Press 'q' and enter. The program will terminate the\n"
                         "    current script. If one wishes to use the program again,\n"
                         "    The Python file will have to be ran again.\n")

class RestaurantFile:
    def __init__(self):
        """
        info to be added
        """
        self.data_frame = pd.read_csv("/Users/j_hernandez/Desktop/cs361_working/ny_restaurants.csv")
        self.saved_list = None
        self.unfiltered_list = None
        self.num_saved_list = 0
        self.saved_list_random = False
        self.latest_input_options = 1
        self.num_rows = self.data_frame.shape[0]

        pd.set_option('display.max_rows', None)

    @staticmethod
    def invalid_message():
        """
        Red 'invalid' text displayed to the user.
        """
        print(Fore.RED + "invalid input" + Style.RESET_ALL)

    def get_entire_list(self):
        """
        Returns the entire csv file as a dataframe.
        """
        return self.data_frame

    def get_random_row(self):
        """
        Returns a random series as a dataframe.
        """
        row_num = random.randint(0, self.num_rows - 1)
        random_restaurant = self.data_frame.iloc[[row_num]]

        return random_restaurant

    def set_latest_input_options(self, option_num):
        """
        Sets the most recent input option into a variable. Used for 'Info' window.
        """
        self.latest_input_options = option_num

    def set_saved_list(self, current_list):
        """
        Sets the current dataframe view as a variable.
        """
        self.saved_list = current_list
        self.num_saved_list = current_list.shape[0]

    def set_random_status(self, bool_value):
        """
        Determines if most recent dataframe view was from the random input or not.
        """
        self.saved_list_random = bool_value

    def search_type(self):
        """
        Determines what value will be searched by the user.
        """
        while True:
            second_input = get_input()

            if second_input == "q":
                quit()

            elif second_input == "c":
                print(Fore.MAGENTA + "\n--- Cuisine type search selected ---\n" + Style.RESET_ALL)
                print(search_options_2)
                return self.cuisine_search()

            else:
                self.invalid_message()

    def cuisine_search(self):
        """
        Returns a dataframe that matches the user's key input.
        """
        while True:
            cuisine_input = get_input()

            if cuisine_input == "q":
                quit()

            elif cuisine_input == "1":
                key_term = "Dessert"
                break

            elif cuisine_input == "2":
                key_term = "Italian"
                break

            elif cuisine_input == "3":
                key_term = "Thai"
                break

            else:
                self.invalid_message()

        print(Fore.MAGENTA + f"\n--- Cuisine type ({key_term}) selected ---\n" + Style.RESET_ALL)

        df = self.data_frame
        searched_rows = df.loc[df["Cuisine"] == key_term]

        return searched_rows

    def filter_type(self, f_or_w):
        """
        Returns a dataframe that matches the user's key input.
        """
        while True:
            second_input = get_input()
            valid_inputs = ["1", "2", "3"]
            filtered_set = set()

            if second_input == "q":
                quit()

            elif len(second_input) >= 1:

                for element in second_input:
                    if element in valid_inputs:
                        filtered_set.add(element)

                check_common = set(valid_inputs) & set(filtered_set)
                if check_common:
                    sorted_list = sorted(filtered_set)

                    num_to_price = {
                        "1": "$",
                        "2": "$$",
                        "3": "$$$"
                    }

                    sorted_list = [num_to_price.get(item, item) for item in sorted_list]

                    df = self.saved_list
                    if f_or_w == "w":
                        df = self.unfiltered_list

                    filtered_restaurants = df[df["Price"].isin(sorted_list)]
                    print(Fore.MAGENTA + "\n--- Low cost ($) filtration applied ---\n" + Style.RESET_ALL)

                    return filtered_restaurants

            else:
                self.invalid_message()

    def display_input_options(self, option_num):
        """
        Prints the available keyboard options per window.
        """
        if option_num == 1:
            print(input_options_1)

        elif option_num == 2:
            print(input_options_2)

        elif option_num == 3:
            print(input_options_3)

        elif option_num == 4:
            print(input_options_4)

        self.set_latest_input_options(option_num)

    def display_results(self, user_command):
        """
        Returns a dataframe that matches the user's key input.
        """
        if user_command == "q":
            quit()

        elif user_command == "i":
            print(functions_information)
            self.display_input_options(self.latest_input_options)

        elif user_command == "e":
            print(Fore.MAGENTA + "\n--- Full list selected. "
                                 "All restaurants being viewed ---\n" + Style.RESET_ALL)
            whole_list = self.get_entire_list()
            print(whole_list)

            self.set_saved_list(whole_list)
            self.set_random_status(False)
            self.display_input_options(2)

        elif user_command == "r":
            print(Fore.MAGENTA + "\n--- Random restaurant selected ---\n" + Style.RESET_ALL)
            random_restaurant = (self.get_random_row())
            print(random_restaurant)

            self.set_saved_list(random_restaurant)
            self.set_random_status(True)
            self.display_input_options(1)

        elif user_command == "s":
            print(Fore.MAGENTA + "\n--- Search selected ---\n" + Style.RESET_ALL)
            print(search_options_1)

            searched_restaurants = self.search_type()
            print(searched_restaurants)

            self.set_saved_list(searched_restaurants)
            self.set_random_status(False)

            if self.num_saved_list == 1:
                self.display_input_options(1)
            else:
                self.display_input_options(3)

        elif (user_command == "f" or user_command == "w") and self.saved_list_random is False:
            print(Fore.MAGENTA + "\n--- Filtration selected ---\n" + Style.RESET_ALL)
            print(filter_options_1)

            if user_command == "f":
                self.unfiltered_list = self.saved_list
            filtered_restaurants = self.filter_type(user_command)

            if len(filtered_restaurants) == 0:
                print("No restaurants to show")
            else:
                print(filtered_restaurants)

            self.set_saved_list(filtered_restaurants)
            self.set_random_status(False)
            self.display_input_options(4)

        else:
            self.invalid_message()


def get_input():
    """
    Records the user's input.
    """
    return input("Your input: ").lower()


if __name__ == '__main__':
    my_file = RestaurantFile()

    print(header)
    my_file.display_input_options(1)

    while True:  # Loops until the user presses the 'Q' key.
        user_input = get_input()
        my_file.display_results(user_input)
