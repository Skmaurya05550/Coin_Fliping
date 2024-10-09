import random
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Coin:
    def __init__(self):
        self.sides = ['Heads', 'Tails']
    
    def flip(self):
        """Simulate flipping the coin."""
        result = random.choice(self.sides)
        logging.info(f'Coin flipped: {result}')
        return result

class CoinFlipper:
    def __init__(self):
        self.coin = Coin()
        self.results = {'Heads': 0, 'Tails': 0}

    def flip_multiple_times(self, number_of_flips):
        """Flip the coin multiple times and store results."""
        for _ in range(number_of_flips):
            result = self.coin.flip()
            self.results[result] += 1

    def display_results(self):
        """Display results of the coin flips."""
        print("\nTotal results:")
        for side, count in self.results.items():
            print(f"{side}: {count}")

    def save_results_to_json(self, filename):
        """Save results to a JSON file."""
        with open(filename, 'w') as json_file:
            json.dump(self.results, json_file)
        logging.info(f'Results saved to {filename}')

def main():
    try:
        number_of_flips = int(input("Enter the number of times to flip the coin: "))
        coin_flipper = CoinFlipper()
        coin_flipper.flip_multiple_times(number_of_flips)
        coin_flipper.display_results()
        
        # Optional: Save results to a JSON file
        save_choice = input("Do you want to save the results to a JSON file? (y/n): ").lower()
        if save_choice == 'y':
            filename = input("Enter the filename (with .json extension): ")
            coin_flipper.save_results_to_json(filename)
    
    except ValueError:
        logging.error("Invalid input! Please enter a valid integer.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
