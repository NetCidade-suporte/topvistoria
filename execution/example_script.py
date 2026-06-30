
"""
Execution Script: Example

This script demonstrates a simple deterministic action.
"""

import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python example_script.py <input_text>")
        sys.exit(1)

    input_text = sys.argv[1]
    
    # Process the input (example: uppercase it)
    result = input_text.upper()
    
    # Ensure .tmp exists
    os.makedirs('.tmp', exist_ok=True)
    
    # Write to output
    output_path = os.path.join('.tmp', 'output.txt')
    with open(output_path, 'w') as f:
        f.write(result)
        
    print(f"Processed text written to {output_path}")

if __name__ == "__main__":
    main()
