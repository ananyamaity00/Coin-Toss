import random
import time
import matplotlib.pyplot as plt
import datetime
import os

def flip_coin():
    return random.choice(["Heads", "Tails"])

def display_chart(heads_count, tails_count):
    labels = ["Heads", "Tails"]
    counts = [heads_count, tails_count]
    colors = ["blue", "red"]
    
    plt.figure(figsize=(5, 5))
    plt.pie(counts, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
    plt.title("🪙 Coin Toss Results")
    plt.show()

def save_results(session_history):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"coin_toss_results_{timestamp}.txt"
    
    with open(filename, "w") as file:
        file.write("📝 Session Summary:\n")
        for i, (heads, tails) in enumerate(session_history, 1):
            file.write(f"Session {i}: Heads - {heads}, Tails - {tails}\n")
    
    print(f"\n✅ Results saved to {os.path.abspath(filename)}")

def coin_toss_simulation():
    session_history = []
    print("🎲 Welcome to the Coin Toss Simulator!")
    
    while True:
        try:
            num_flips = int(input("\n🔢 Enter the number of times you want to flip the coin: "))
            if num_flips <= 0:
                print("⚠️ Please enter a positive number.")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue
        
        heads_count = 0
        tails_count = 0
        flip_results = []
        
        print("\nFlipping the coin...\n")
        for _ in range(num_flips):
            time.sleep(0.2)
            result = flip_coin()
            flip_results.append(result)
            print(result)
            if result == "Heads":
                heads_count += 1
            else:
                tails_count += 1
        
        session_history.append((heads_count, tails_count))
        
        print("\n📊 Results Summary:")
        print(f"Heads: {heads_count} ({(heads_count / num_flips) * 100:.2f}%)")
        print(f"Tails: {tails_count} ({(tails_count / num_flips) * 100:.2f}%)")
        print("🧾 Flip Sequence:", " -> ".join(flip_results))
        
        show_chart = input("Do you want to see a pie chart of this session? (yes/no): ").strip().lower()
        if show_chart == "yes":
            display_chart(heads_count, tails_count)
        
        again = input("\nDo you want to flip again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\n📘 Full Session Summary:")
            for i, (heads, tails) in enumerate(session_history, 1):
                print(f"Session {i}: Heads - {heads}, Tails - {tails}")
            save_results(session_history)
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    coin_toss_simulation()
