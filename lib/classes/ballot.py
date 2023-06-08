import sqlite3
CONN = sqlite3.connect('election_database.db')
CURSOR = CONN.cursor()
class Ballot():
    def __init__(self, election_name):
        self.election_name = election_name
    
    @classmethod
    def create_table( cls ):
        sql = """
            create table if not exists ballots (
                id integer primary key,
                election_name text 
            )
        """
        CURSOR.execute(sql)
        print("Ballot table created successfully.")
    