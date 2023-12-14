import re

def args_parser_typed(*type_args):
    def args_parser(func):
        def wrapper(args):
            function_args = args.split(" ")

            if len(type_args) != len(function_args):
                raise ValueError("Incorrect arguments amount")

            for i in range(len(type_args)):
                function_args[i] = type_args[i](function_args[i])

            try:
                return func(*function_args)

            except TypeError as err:
                raise ValueError(f"Error: {err}")

            except ValueError as err:
                raise ValueError(f"Handler error: {err}")

            except KeyError as err:
                raise KeyError(f"Error: {err}")

        return wrapper
    return args_parser

def validate_phone_number(contact_number):
    if re.match(r'^\d{10}$', contact_number) is None:
        raise ValueError("The contact number is not valid.")

@args_parser_typed(str, str)
def add_handler(contact_name, contact_number):
    validate_phone_number(contact_number)
    database[contact_name] = contact_number
    return f"Number of {contact_name} was added"

@args_parser_typed(str, str)
def change_handler(contact_name, new_contact_number):
    contact_number = database.get(contact_name)
    if contact_number is None:
        raise KeyError(f"{contact_name} not found in contacts")

    validate_phone_number(new_contact_number)
    database[contact_name] = new_contact_number
    return f"Number for {contact_name} was changed"

@args_parser_typed(str)
def phone_handler(contact_name):
    if contact_name not in database:
        raise KeyError(f"{contact_name} not found in contacts")

    return f"The phone number for {contact_name} is {database[contact_name]}"

def show_all_handler():
    if not database:
        return "No contacts found"
    
    return database

def hello_handler():
    return "How can I help you?"

database = {
    
}

def main():
    table = {
        "add": add_handler,
        "change": change_handler,
        "phone": phone_handler,
        "show all": show_all_handler,
        "hello": hello_handler
    }

    while True:
        user_input = str(input(">>> "))

        if user_input.lower() in ["good bye", "close", "exit", "quit"]:
            print("Good Bye!")
            break

        first_space = user_input.find(" ")
        handler_name = user_input[:first_space].lower()
        args = user_input[first_space:].strip()

        if user_input.lower() == "hello":
            handler_name = "hello"
        
        if user_input.lower() == "show all":
            handler_name = "show all"        

        if handler_name in table:

            if user_input.lower() == "hello":
                table[handler_name]()

            elif user_input.lower() == "show all":
                table[handler_name]()
            
            try:
             
                if user_input.lower() == "hello":
                    result = table[handler_name]()

                elif user_input.lower() == "show all":
                    result = table[handler_name]()  

                else:             
                    result = table[handler_name](args)

                if result:
                    print(result)

            except (ValueError, KeyError) as e:
                print(f"{e}")
        else:
            print("No such command")

if __name__ == "__main__":
    main()
