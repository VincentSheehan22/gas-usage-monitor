import pandas as pd
import matplotlib.pyplot as plt


def get_entry():
    """Get input from user, and return as data frame."""
    date = input("Input date (yyyy-mm-dd): ")
    reading = input("Input reading (kWh): ")

    df_entry = pd.DataFrame([[date, reading]], columns=["Date", "Reading"])

    return df_entry


def add_to_df(df_log, df_entry):
    """Add entry as new row in main data frame."""
    df_out = df_log.append(df_entry)

    return df_out


def run_menu():
    """Launch menu."""
    option = input("""Select option: 
    1 - Add new entry.
    2 - Display trend.
    3 - Display data frame.
    4 - Exit.
    """)

    return option


if __name__ == '__main__':
    while True:
        menu_option = run_menu()

        if menu_option == '1':
            df_readings = pd.read_csv("Meter Readings.csv", index_col=False)
            df_entry = get_entry()
            df_updated = add_to_df(df_readings, df_entry)
            csv = df_updated.to_csv("Meter Readings.csv", index=False)
        elif menu_option == '2':
            df_readings = pd.read_csv("Meter Readings.csv", index_col=False)
            plt.plot(df_readings["Date"], df_readings["Reading"])
            plt.show()
        elif menu_option == '3':
            df_readings = pd.read_csv("Meter Readings.csv", index_col=False)
            print(df_readings)
        elif menu_option == '4':
            exit()
        else:
            print("Enter 1-4.")


