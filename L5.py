def mcculloch_pitts(inputs, weights, threshold):
    """McCulloch-Pitts neuron model."""
    # Ensure the number of inputs matches the number of weights
    assert len(inputs) == len(weights), "Number of inputs must match number of weights"
    
    # Calculate the weighted sum of inputs
    weighted_sum = sum(x * w for x, w in zip(inputs, weights))
    
    # Apply the threshold function
    output = 1 if weighted_sum >= threshold else 0
    return output

def test_logic_gate(logic_gate):
    """Test a logic gate using McCulloch-Pitts neuron."""
    print(f"Testing {logic_gate} gate:")
    
    if logic_gate == "AND":
        # AND gate
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        weights = (1, 1)
        threshold = 2
        
        # Test the AND gate
        for input_pair in inputs:
            result = mcculloch_pitts(input_pair, weights, threshold)
            print(f"{input_pair}: {result}")

    elif logic_gate == "OR":
        # OR gate
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        weights = (1, 1)
        threshold = 1
        
        # Test the OR gate
        for input_pair in inputs:
            result = mcculloch_pitts(input_pair, weights, threshold)
            print(f"{input_pair}: {result}")

    elif logic_gate == "XOR":
        # XOR gate (requires a combination of AND, OR, and NOT gates)
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        weights_and = (1, 1)
        weights_or = (1, 1)
        weights_not = (-1,)
        threshold_and = 2
        threshold_or = 1
        threshold_not = 0  # for NOT gate in this context

        for input_pair in inputs:
            input1, input2 = input_pair
            
            # Simulate the XOR logic using AND, OR, and NOT
            and_result = mcculloch_pitts(input_pair, weights_and, threshold_and)
            or_result = mcculloch_pitts(input_pair, weights_or, threshold_or)
            not_result = mcculloch_pitts((and_result,), weights_not, threshold_not)
            xor_result = mcculloch_pitts((or_result, not_result), weights_and, threshold_and)
            
            print(f"{input_pair}: {xor_result}")

    elif logic_gate == "AND NOT":
        # AND NOT gate
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        weights = (1, -1)
        threshold = 1
        
        # Test the AND NOT gate
        for input_pair in inputs:
            result = mcculloch_pitts(input_pair, weights, threshold)
            print(f"{input_pair}: {result}")
    
    else:
        print("Invalid logic gate.")
        return

# Test different logic gates
test_logic_gate("AND")
test_logic_gate("OR")
test_logic_gate("XOR")
test_logic_gate("AND NOT")
