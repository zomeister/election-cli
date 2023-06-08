""" IMPORTING CLASSES """
# from .classes import *
""" OR """
from classes.ballot import Ballot
# from .classes.candidate import Candidate
# from .classes.voter import Voter
# from .classes.position import Position
import ipdb

def start_cli():
    print(f" GREETINGS VALUED CITIZENS! ".center(80, '\u00AB'))
    print("Welcome to the Election CLI!".center(80))
    print("Here are the options:".rjust(80))
    print("1. Create a new ballot")
    print("2. Vote on a ballot")
    print("3. Tally a ballot")
    print("4. Exit")
    choice = input("What would you like to do? ")
    if choice == "1":
        create_ballot()
    elif choice == "2":
        vote_on_ballot()
    elif choice == "3":
        tally_ballot()
    elif choice == "4":
        print('{:-^80}'.format(" EXITING BALLOT "))

    else:
        print("Invalid choice. Please try again.")
        start_cli()
        
def create_ballot():
    print('{:.<80}'.format(" >>> ...LOADING BALLOT..."))
    # file_name = input("Enter ballots/filename.txt: ")
    # print(file_name)
    Ballot.create_ballot()
    
def vote_on_ballot():
    print('{:.<80}'.format(" >>> ...LOADING VOTER..."))
    name = input("Enter name: ")
    dob = input("Enter date of birth (MMDDYYYY): ")
    print(f'Voter Info: name={name}, dob={dob}')
    
def tally_ballot():
    print('{:.<80}'.format(" >>> ...LOADING RESULTS..."))
    

start_cli()