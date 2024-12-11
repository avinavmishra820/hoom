# Alpha-Beta Pruning in Minimax Algorithm

# Constants for alpha and beta initial values
MAX, MIN = 1000, -1000

# Minimax function with Alpha-Beta pruning
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Base case: if we've reached the leaf node
    if depth == 3:
        return values[nodeIndex]
    
    if maximizingPlayer:
        best = MIN
        
        # Explore the two children (left and right)
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)  # Maximizer chooses the maximum
            alpha = max(alpha, best)
            
            # Alpha Beta Pruning
            if beta <= alpha:
                print(f"Pruning at depth {depth}, nodeIndex {nodeIndex}, alpha {alpha}, beta {beta}")
                break
        
        return best
    
    else:
        best = MAX
        
        # Explore the two children (left and right)
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)  # Minimizer chooses the minimum
            beta = min(beta, best)
            
            # Alpha Beta Pruning
            if beta <= alpha:
                print(f"Pruning at depth {depth}, nodeIndex {nodeIndex}, alpha {alpha}, beta {beta}")
                break
        
        return best

# Driver Code
if __name__ == "__main__":
    # Example tree with leaf node values
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    
    # Start Minimax with Alpha-Beta pruning
    print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))
