from enigma_machine import EnigmaMachine, InvalidPresetCode
import datetime


def main():
    machine = EnigmaMachine()
    help_text = {
        "date": '''The machine starts out with today's date as the default message-date. To set the message-date for
            the machine, input a date in any valid ISO 8601 format, except ordinal dates (e.g. YYYY-DDD).
            >> Year-Month-Day format:
            >> YYYYMMDD (basic format) or YYYY-MM-DD (extended format)
            The date is saved for all future messages ciphered through this machine. To change the date, call this command again.''',
        "private": '''For one message-cipher only, set a "8-letter" code as the private key. When the next message is
            ciphered, the machine will reset to the latest date set using the 'date' command. Format -> re:"[a-zA-Z]{8}"
            To check if the private-key is set, use the 'code' command. When trying to decipher the generated message, re-enter the private-key using this command.''',
        "code": '''If a private-key is active for the next message, this command will print the private-key, else it
            displays "None"''',
        "message": '''Enter your message that needs to ciphered by the EnigmaMachine. Press "RETURN/ENTER" after you  
            have typed the message to process the cipher through the EnigmaMachine. 
            EnigmaMachine only ciphers alphabets, all white-spaces and punctuation/symbols will remain as they are in the ciphered message.
            For private-messages make sure that the private-key is set using the 'private' command. To check if the private-key is set, use the 'code' command.''',
        "exit": '''Close the EnigmaMachine and exit the program.'''
    }

    while True:
        print("-" * 100)
        command = input("Enter your command:\n> ").strip().lower()
        match command:
            case "help":
                print("Available commands--")
                for key, value in help_text.items():
                    print(f"{key:10}: {value}")

            case "date":
                date_s = input("Message-date: ").strip()
                try:
                    n_date = datetime.date.fromisoformat(date_s)
                except ValueError:
                    print(">> Invalid date format. Try 'help' for the accepted date-format")
                    continue

                try:
                    machine.set_preset_date(n_date)
                except FileNotFoundError:
                    print(">> Presets not yet defined for required month. Try using a date from the current decade.")
                    continue

            case "private":
                code = input("Private Code: ").strip()
                try:
                    machine.set_private_code(code)
                except InvalidPresetCode:
                    print(">> Invalid private-code. Try 'help' for the accepted code-format")

            case "code":
                print(f">> Active code: {machine.get_private_code()}")

            case "message":
                message = input("Type your message:\n").strip()
                print(f">> Ciphered message:\n{machine.cipher_message(message)}")

            case "exit":
                exit(0)

            case _:
                print(">> Invalid command. Try 'help' to see the available commands")


if __name__ == '__main__':
    main()
