# imports 
import random 
from matplotlib import pyplot as plt, animation 
  
# helper methods 
def swap(A, i, j): 
    A[i], A[j] = A[j], A[i] 
  
  
# algorithms 
def insertion_sort(A):
    length = range(1, len(A))
    for i in length:
        value_to_sort = A[i]
        while A[i-1] > value_to_sort and i>0:
            A[i], A[i-1] = A[i-1], A[i]
            i = i-1
    return A
  
  
def visualize(): 
    N = 100
    A = list(range(1, N + 1)) 
    random.shuffle(A) 
      
    # creates a generator object containing all  
    # the states of the array while performing  
    # sorting algorithm 
    generator = insertion_sort(A) 
      
    # creates a figure and subsequent subplots 
    fig, ax = plt.subplots() 
    ax.set_title("Insertion Sort O(n\N{SUPERSCRIPT TWO})") 
    bar_sub = ax.bar(range(len(A)), A, align="edge") 
      
    # sets the maximum limit for the x-axis 
    ax.set_xlim(0, N) 
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes) 
    iteration = [0] 
      
    # helper function to update each frame in plot 
    def update(A, rects, iteration): 
        for rect, val in zip(rects, A): 
            rect.set_height(val) 
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}") 
  
    # creating animation object for rendering the iteration 
    anim = animation.FuncAnimation( 
        fig, 
        func=update, 
        fargs=(bar_sub, iteration), 
        frames=generator, 
        repeat=False, 
        blit=False, 
        interval=15, 
        save_count=90000, 
    ) 
      
    # for showing the animation on screen 
    plt.show() 
    plt.close() 
  
  
if __name__ == "__main__": 
    visualize() 