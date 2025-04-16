"""
What is Recursion?

Recursion is a clever programming technique where a function solves a problem by calling itself with smaller versions of the same problem. It’s like telling someone to solve a big puzzle by first solving a smaller piece of it, then building up from there. Every recursive solution has two key parts:
1. Base Case: The simplest version of the problem that can be solved directly.
2. Recursive Case: Breaking the problem into smaller steps and solving each step by calling the function again.
   
Why Use Recursion?

Recursion shines when a problem naturally splits into smaller, similar problems. It makes code shorter, easier to understand, and often mirrors the logical structure of the task at hand.

  a cool usage of recursion is to Sum a list

"""
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

# Example
print(sum_list([1, 2, 3, 4]))  # Output: 10
