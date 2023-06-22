'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
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
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #checking following list of subject and object
    subject_following = social_graph[from_member]["following"]
    object_following = social_graph[to_member]["following"]

    if to_member in subject_following:
        if from_member in object_following:
            relationship_status = "friends"
        else:
            relationship_status = "follower"
    else:
        if from_member in object_following:
            relationship_status = "followed by"
        else:
            relationship_status = "no relationship"
    
    return relationship_status

def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
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
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # ROW CHECK <3
    row_number = len(board) 
    for number in range(row_number):
        if board[number].count("X") == row_number:
            tic_tac_toe = "X"
            break
        elif board[number].count("O") == row_number:
            tic_tac_toe = "O"
            break

    # DIAGONAL CHECK <3

        diagonal1_number = 0
        board_number = 0
        diagonal1 = ""
        for number in range(row_number):
            diagonal1 += (board[board_number])[diagonal1_number]
            board_number += 1
            diagonal1_number += 1
    
        diagonal2 = ""
        diagonal2_number = row_number - 1
        for number in range(row_number):
            diagonal2 += board[number][diagonal2_number]
            diagonal2_number -= 1

        if diagonal1.count("X")==row_number or diagonal2.count("X")==row_number:
            tic_tac_toe = "X"
        elif diagonal1.count("O")==row_number or diagonal2.count("O")==row_number:
            tic_tac_toe = "O"
        else:

    # COLUMN CHECK </3    

            column1 = ""
            column2 = ""
            column3 = ""
            column4 = ""
            column5 = ""
            column6 = ""
            
            if row_number == 6:
                for row_numberr in range(row_number):
                    column1 += board[row_numberr][0]
                    column2 += board[row_numberr][1]
                    column3 += board[row_numberr][2]
                    column4 += board[row_numberr][3]
                    column5 += board[row_numberr][4]
                    column6 += board[row_numberr][5]
            elif row_number ==5:
                for row_numberr in range(row_number):
                    column1 += board[row_numberr][0]
                    column2 += board[row_numberr][1]
                    column3 += board[row_numberr][2]
                    column4 += board[row_numberr][3]
                    column5 += board[row_numberr][4]
            elif row_number == 4:
                for row_numberr in range(row_number):
                    column1 += board[row_numberr][0]
                    column2 += board[row_numberr][1]
                    column3 += board[row_numberr][2]
                    column4 += board[row_numberr][3]
            else:
                for row_numberr in range(row_number):
                    column1 += board[row_numberr][0]
                    column2 += board[row_numberr][1]
                    column3 += board[row_numberr][2]
            
            if column1.count("X")==row_number or column2.count("X")==row_number or column3.count("X")==row_number or column4.count("X")==row_number or column5.count("X")==row_number or column6.count("X")==row_number:
                tic_tac_toe = "X"  
            elif column1.count("O")==row_number or column2.count("O")==row_number or column3.count("O")==row_number or column4.count("O")==row_number or column5.count("O")==row_number or column6.count("O")==row_number:
                tic_tac_toe = "O"
            else:
                tic_tac_toe = "NO WINNER"
    
    return tic_tac_toe

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
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
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    eta = 0
    eta1 = 0
    eta2 = 0
    key1 = 0
    key2 = 0

    my_keys = list(route_map.keys())
    total_keys = len(my_keys)

    for key in my_keys:
        if key[0] == first_stop:
            key1 = my_keys.index(key)
        if key[1] == second_stop:
            key2 = my_keys.index(key)
    
    if first_stop == second_stop:
            eta = 0            
    elif key1 <= key2:
        if key[0] == first_stop and key[1] == second_stop:
            eta = route_map[key]["travel_time_mins"]
        else:
            for number in range(key1, key2+1):
                eta += route_map[my_keys[number]]["travel_time_mins"]
    else:
        eta1 = sum([route_map[my_keys[number]]["travel_time_mins"] for number in range(key1,total_keys)])
        eta2 = sum([route_map[my_keys[number]]["travel_time_mins"] for number in range(key2+1)])
        eta = eta1 + eta2
    
    return eta
