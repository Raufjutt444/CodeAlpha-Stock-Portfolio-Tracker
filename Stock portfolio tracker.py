def run_stock_tracker():
    # 1. Setup: Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "MSFT": 400.00,
        "GOOGL": 140.00,
        "AMZN": 175.00
    }
    
    portfolio = []
    total_investment = 0.0
    
    print("Welcome to the Portfolio Tracker!")
    print(f"Available stocks to track: {', '.join(stock_prices.keys())}")
    
    # 2. Input/Output and Arithmetic Loop
    while True:
        ticker = input("\nEnter a stock ticker (or type 'done' to finish): ").upper()
        
        if ticker == 'DONE':
            break
            
        if ticker not in stock_prices:
            print(f"Sorry, '{ticker}' is not in our database. Try again.")
            continue
            
        try:
            quantity = float(input(f"Enter the number of shares for {ticker}: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
            
        # Basic arithmetic: Calculate cost and add to total
        price_per_share = stock_prices[ticker]
        total_cost = price_per_share * quantity
        total_investment += total_cost
        
        # Store for the receipt
        portfolio.append((ticker, quantity, total_cost))
        print(f"Added {quantity} shares of {ticker} at ${price_per_share:.2f} each.")
        print(f"Current Total: ${total_investment:.2f}")

    # Display final results
    print("\n--- Portfolio Summary ---")
    if not portfolio:
        print("No stocks added.")
    else:
        for ticker, qty, cost in portfolio:
            print(f"{ticker}: {qty} shares = ${cost:.2f}")
    print(f"Total Investment Value: ${total_investment:.2f}")
    print("-------------------------")

    # 3. Optional File Handling
    if portfolio:
        save_file = input("\nWould you like to save this summary to a text file? (y/n): ").lower()
        if save_file == 'y':
            try:
                # 'w' mode opens the file for writing (and creates it if it doesn't exist)
                with open("portfolio_summary.txt", "w") as file:
                    file.write("Portfolio Summary\n")
                    file.write("-------------------------\n")
                    for ticker, qty, cost in portfolio:
                        file.write(f"{ticker}: {qty} shares = ${cost:.2f}\n")
                    file.write("-------------------------\n")
                    file.write(f"Total Investment Value: ${total_investment:.2f}\n")
                
                print("Successfully saved to 'portfolio_summary.txt'.")
            except Exception as e:
                print(f"An error occurred while saving the file: {e}")

# Run the program
if __name__ == "__main__":
    run_stock_tracker()