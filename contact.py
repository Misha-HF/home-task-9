import re

def args_parser_typed(*type_args):
    def args_parser(func):
        def wrapper(args):
            function_args = args.split(" ")

            if len(type_args) != len(function_args):
                print("Incorrect arguments amount")
                return

            for i in range(len(type_args)):
                function_args[i] = type_args[i](function_args[i])

            try:
                func(*function_args)

            except TypeError as err:
                return print(f"Error: {err}")

            except ValueError as err:
                return print(f"Handler error: {err}")

            except KeyError as err:
                return print(f"Error: {err}")

            return

        return wrapper
    return args_parser

def validate_phone_number(contact_number):
    if re.match(r'^\d{10}$', contact_number) is None:
        raise ValueError("The contact number is not valid.")

@args_parser_typed(str, str)
def add_handler(contact_name, contact_number):
    validate_phone_number(contact_number)
    database[contact_name] = contact_number
    return print(f"Number of {contact_name} was added")


@args_parser_typed(str, str)
def change_handler(contact_name, new_contact_number):
    contact_number = database.get(contact_name)
    if contact_number is None:
        raise KeyError(f"{contact_name} not found in contacts")

    validate_phone_number(new_contact_number)
    database[contact_name] = new_contact_number
    return print(f"Number for {contact_name} was changed")


@args_parser_typed(str)
def phone_handler(contact_name): 
    return print(f"The phone number for {contact_name} is {database[contact_name]}")


def show_all_handler():
    if not database:
        return "No contacts found"
    
    return print(database)


def hello_handler():
    return print("How can I help you?")


def main():
    global database
    database = {
        "User": "0689999999"
    }

    table = {
        "add": add_handler,
        "change": change_handler,
        "phone": phone_handler,
        "show all": show_all_handler,
        "hello": hello_handler
    }

    while True:
        user_input = str(input(">>> "))

        if user_input in ["good bye", "close", "exit", "quit"]:
            print("Good Bye!")
            break

        first_space = user_input.find(" ")

        handler_name = user_input[:first_space]
        handler_name = handler_name.lower()

        args = user_input[first_space:].strip()

        if user_input.lower() == "hello":
            handler_name = "hello"
        
        if user_input.lower() == "show all":
            handler_name = "show all"

        if table.get(handler_name) is not None:

            if user_input.lower() == "hello":
                table[handler_name]()

            elif user_input.lower() == "show all":
                table[handler_name]()

            else:
                table[handler_name](args)
                
        else:
            print("No such command")


if __name__ == "__main__":
    main()