import matplotlib.pyplot as plt

# Create basic plots (line, bar, scatter) using matplotlib.
def create_basic_plots():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Line plot
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(x, y, marker='o')
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Bar plot
    plt.subplot(3, 1, 2)
    plt.bar(x, y)
    plt.title('Bar Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Scatter plot
    plt.subplot(3, 1, 3)
    plt.scatter(x, y)
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Show plots
    plt.tight_layout()
    plt.show()

# Call the function to create plots
create_basic_plots()