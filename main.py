import app.analyze as analyze
import app.helper_functions as helper_functions
import app.email_function as email_function
import app.toggl_function as toggl_function
import app.venmo_function as venmo_function


def main() -> None:
    args = helper_functions.get_args()
    CREDENTIALS = helper_functions.load_yml("../toggl_creds")
    configs = helper_functions.load_yml("config")

    the_D = toggl_function.retrieve_toggl_data(CREDENTIALS["toggl"], args.pdf)
    analysis = analyze.analyze_data(the_D)

    # venmo_function(configs["transfer_amount"], CREDENTIALS["venmo"])
    try:
        email_function.send(analysis, args.pdf, CREDENTIALS["email"])
        print("EMAIL SENT!")
    except:
        print("ERROR: EMAIL FAILED TO SEND")

if __name__ == "__main__":
    main()
