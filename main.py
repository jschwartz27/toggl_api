import argparse

import app.analyze as analyze
import app.email_function as email_function
import app.toggl_function as toggl_function
import app.venmo_function as venmo_function
from app.cipher import Cipher

CREDENTIALS_ENCRYPT = {
    "EMAIL"     : "AEHls.qCJRPn1f&h",                
    "PASSWORD"  : "tP TzXlZ",                        
    "API_TOKEN" : "DXRy@cDbfhhzFR71ocH DlGaGU6W Vfb" 
}
EMAIL_CREDENTIALS = {
    "usernameFrom" : "1$EXoFQCMFUk8.",
    "password"     : "87FltNEHGQHs7H73",
    "usernameTo"   : "2EFaMLEEUDSpBZP"
}


def load_yml(name: str) -> dict:
    filename = name + ".yml"


def get_args() -> object:
    parser = argparse.ArgumentParser(description="Cipher key and helper arguments")
    parser.add_argument("-key", required=True, type=str,
                        help='cipher_key')
    parser.add_argument("-pdf", required=False, type=bool,
                        help="Option to attach detailed pdfs to your email")
    return parser.parse_args()


def main() -> None:
    args = get_args()
    configs = load_yml("config")
    c = Cipher(args.key)

    creds = {
        i: c.decryptMessage(CREDENTIALS_ENCRYPT[i]) for i in CREDENTIALS_ENCRYPT
    }

    e_CREDS_deCRYpTed = {
        i: c.decryptMessage(EMAIL_CREDENTIALS[i]) for i in EMAIL_CREDENTIALS
    }

    the_D = toggl_function.retrieve_toggl_data(creds, args.pdf)
    analysis = analyze.analyze_data(the_D)
    # email_function.send(analysis["message"], args.pdf, e_CREDS_deCRYpTed)
    # venmo_function(configs["transfer_amount"])

if __name__ == "__main__":
    main()
