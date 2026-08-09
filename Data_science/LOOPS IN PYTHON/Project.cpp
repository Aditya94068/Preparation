#include <iostream>
using namespace std;

char board[3][3];  // 3x3 Tic-Tac-Toe board

// Initialize the board with numbers 1–9
void initializeBoard() {
    char num = '1';
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            board[i][j] = num++;
}

// Display the current board
void displayBoard() {
    cout << "\n";
    for (int i = 0; i < 3; i++) {
        cout << " ";
        for (int j = 0; j < 3; j++) {
            cout << board[i][j];
            if (j < 2) cout << " | ";
        }
        if (i < 2) cout << "\n-----------\n";
    }
    cout << "\n";
}

// Check if a player has won
bool checkWin(char player) {
    // Check rows and columns
    for (int i = 0; i < 3; i++) {
        if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) || 
            (board[0][i] == player && board[1][i] == player && board[2][i] == player))
            return true;
    }
    // Check diagonals
    if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) || 
        (board[0][2] == player && board[1][1] == player && board[2][0] == player))
        return true;

    return false;
}

// Check for a draw
bool checkDraw() {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] != 'X' && board[i][j] != 'O')
                return false;
    return true;
}

// Handle a player move
bool makeMove(char player) {
    int move;
    cout << "Player " << player << ", enter your move (1-9): ";
    cin >> move;

    if (move < 1 || move > 9) {
        cout << "Invalid move! Try again.\n";
        return false;
    }

    int row = (move - 1) / 3;
    int col = (move - 1) % 3;

    if (board[row][col] == 'X' || board[row][col] == 'O') {
        cout << "Cell already taken! Try again.\n";
        return false;
    }
    
    board[row][col] = player;
    return true;
}

// Main game loop
int main() {
    char currentPlayer = 'X';
    initializeBoard();

    while (true) {
        displayBoard();

        if (!makeMove(currentPlayer))
            continue;

        if (checkWin(currentPlayer)) {
            displayBoard();
            cout << "Player " << currentPlayer << " wins!\n";
            break;
        }

        if (checkDraw()) {
            displayBoard();
            cout << "It's a draw!\n";
            break;
        }

        // Switch player
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    return 0;
}
