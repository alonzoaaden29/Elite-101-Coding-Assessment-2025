# READ ME! This is the copy i am turning in!




def get_free_table_ids(tables):
    """ Level 1, Returns a list of tables, displaying their availability."""

    return [t["table_id"] for t in tables if not t ["occupied"]]

     
def find_table(tables, size):
    """Level 2, Finds a free table for party size, or returns None."""

    suitable_tables = next((t["table_id"] for t in tables if not t["occupied"] and t["capacity"] >= size), None)
    return suitable_tables
    

def all_tables(tables, size):
   """Level 3, List of all free tables for party size."""

   return [t["table_id"] for t in tables if not t["occupied"] and t["capacity"] >= size]

# Here i am not really sure what do with the last function, as how to implement it is not clear to me.
# I did try to understand it on my miro
if __name__ == "__main__":
    # Example data
    tables_data = [
        {"table_id": "T1", "occupied": False, "capacity": 2},
        {"table_id": "T2", "occupied": True,  "capacity": 4},
        {"table_id": "T3", "occupied": False, "capacity": 6},
        {"table_id": "T4", "occupied": False, "capacity": 2}
    ]

    print("LEVEL 1: Free Tables =", get_free_table_ids(tables_data))

    print("LEVEL 2: One table for party size 2 =", find_table(tables_data, 2))

    print("LEVEL 3: All tables for party size 2 =", all_tables(tables_data, 2))





# references:
# https://stackoverflow.com/questions/509211/how-slicing-in-python-works
# https://www.w3schools.com/python/python_dictionaries.asp




