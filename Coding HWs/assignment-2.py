'''Assignment 2
This assignment covers your proficiency with Python's data structures.
It engages your ability to manipulate and evaluate data stored in lists and dictionaries.
'''

def relationship_status(from_member, to_member, social_graph):
    '''
    Item 1.
    Relationship Status. 10 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-2-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Write your code below this line
    if from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
        return "friends"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    return "no relationship"

def tic_tac_toe(board):
    '''
    Item 2.
    Tic Tac Toe. 10 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-2    -sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Write your code below this line
    #check if the matrix is has the same row and columns
    if len(board) != len(board[0]):
        return "NO WINNER"
    #check if there are exactly 2 types of unique symbols
    for array in board:
        for symbol in array:
            if symbol != 'X' and symbol != 'O' and symbol != '':
                return "NO WINNER"
    row = ""
    column = ""
    first_diagonal = ""
    second_diagonal = ""
    for i in range(len(board)):
        for j in range(len(board)):
            row = row + board[i][j]
            column = column + board[j][i]
            if i == j:
                first_diagonal = first_diagonal + board[i][j]
            if i + j + 1 == len(board):
                second_diagonal = second_diagonal + board[i][j]
            if row == "XXX" or column == "XXX" or first_diagonal == "XXX" or second_diagonal == "XXX":
                return "X"
            if row == "OOO" or column == "OOO" or first_diagonal == "OOO" or second_diagonal == "OOO":
                return "O"
        row = ""
        column = ""
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''
    Item 3.
    ETA. 10 points.
    A shuttle van service is tasked to travel along a predefined circular route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "assignment-2-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Write your code below this line
    current = first_stop
    total_time = 0
    if first_stop == second_stop:
        return total_time
    while current != second_stop:
        print("current: " + current)
        print("destination: " + second_stop)
        for x in route_map:
            if current == x[0]:
                current = x[1]
                total_time = total_time + route_map[x]["travel_time_mins"]
                break
    return total_time