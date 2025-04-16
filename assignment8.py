"""
What is Recursion?

Recursion is a clever programming technique where a function solves a problem by calling itself with smaller versions of the same problem. It’s like telling someone to solve a big puzzle by first solving a smaller piece of it, then building up from there. Every recursive solution has two key parts:
1. Base Case: The simplest version of the problem that can be solved directly.
2. Recursive Case: Breaking the problem into smaller steps and solving each step by calling the function again.
   
Why Use Recursion?

Recursion shines when a problem naturally splits into smaller, similar problems. It makes code shorter, easier to understand, and often mirrors the logical structure of the task at hand.

  Cool Example: Tower of Hanoi

The Tower of Hanoi is a classic puzzle involving three rods and disks of different sizes stacked on one rod. The goal is to move all the disks to another rod, following these rules:
1. Move only one disk at a time.
2. Never place a larger disk on top of a smaller one.

This puzzle is perfect for recursion because solving it involves breaking it into smaller subproblems:
- First, move the top `n-1` disks to a helper rod.
- Then, move the largest disk to the target rod.
- Finally, move the `n-1` disks from the helper rod to the target rod.

  How Does the Code Work?

Here’s a simplified explanation of the Python code:
"""

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:  # Base case: Move one disk directly
        print(f"Move disk 1 from {source} to {target}")
        return
    
      # Recursive steps:
    tower_of_hanoi(n - 1, source, auxiliary, target)  # Move n-1 disks to helper rod
    print(f"Move disk {n} from {source} to {target}")  # Move the largest disk
    tower_of_hanoi(n - 1, auxiliary, target, source)  # Move n-1 disks to target rod

# Example usage:
tower_of_hanoi(3, 'A', 'C', 'B')
