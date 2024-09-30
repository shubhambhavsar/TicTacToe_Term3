import streamlit as st

# --------------------------------- Game Logic ---------------------------------------------
# Initialization of game board
if 'board' not in st.session_state:
    st.session_state['board'] = [[""] * 3 for _ in range(3)]
    st.session_state['currentplayer'] = "X"
    st.session_state['gameover'] = False
    st.session_state['winner'] = None

# Resetting the game
def reset_game():
    st.session_state['board'] = [[""] * 3 for _ in range(3)]
    st.session_state['currentplayer'] = "X"
    st.session_state['gameover'] = False
    st.session_state['winner'] = None

# Checking for the winner status if it is tie or a winner
def winnerscheck():
    board = st.session_state['board']

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    # Checking for tie
    if all(cell != "" for row in board for cell in row):
        return "Tie"
    return None

# Making a move
def move(row, col):
    if st.session_state['board'][row][col] == "" and not st.session_state['gameover']:
        st.session_state['board'][row][col] = st.session_state['currentplayer']
        winner = winnerscheck()
        if winner:
            st.session_state['gameover'] = True
            st.session_state['winner'] = winner
        else:
            st.session_state['currentplayer'] = "O" if st.session_state['currentplayer'] == "X" else "X"

# -----------------------------------------------------------------------------------------

# ---------------------------Game UI using Streamlit---------------------------------------
st.title("Multiplayer Tic Tac Toe")
st.markdown("Player 1 will be assigned: X")
st.markdown("Player 2 will be assigned: O")


# Displaying the board
for row in range(3):
    cols = st.columns([1, 1, 1]) 
    for col in range(3):
        with cols[col]:
            st.button(
                st.session_state['board'][row][col] or " ",
                key=f"{row}-{col}",
                on_click=move,
                args=(row, col),
                help=f"Cell ({row+1}, {col+1})",
                disabled=st.session_state['board'][row][col] != "" or st.session_state['gameover'],
                use_container_width=True  
            )

# Showing the status of the game
if st.session_state['gameover']:
    if st.session_state['winner'] == "Tie":
        st.success("tie! play again")
    else:
        st.success(f"Player {st.session_state['winner']} wins!")
else:
    st.write(f"Current player: {st.session_state['currentplayer']}")

# Reset button feature
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Reset Game", key="reset"):
    reset_game()
    st.experimental_rerun() 


# ----------------------------------------------------------------------------------------------
