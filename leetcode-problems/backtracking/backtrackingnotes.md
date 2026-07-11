Backtracking is a strategy used to find all permutations of something, can think of it like a decisision tree. you explore possible paths of a solution step by step 

Once you reach a dead end, you backtrack, which means you undo your last step and try to find something else. imagine you are in a maze, you hit a dead end, and then you walk back and keep repeating until you find your way to the exit, thats how it works in code. 


A backtracking question is EXTREMELY similar to a decision tree, each branch is a possible option that you can pick.

The easiest way to understand backtracking is to understand the subsets problem in recursive backtracking, leetcode #78. 

Given an integer array nums of unique elements, return all possible subsets. The solution must not contain duplicate subsets. 

Typicall (when appending to the result array in backtracking), you want to do something like out.append(path.copy()), because you want a local copy, you dont want a reference to the path array because it will end up changing, you simpy want again, a local COPY of what path is at that instance. 

Pattern:

def backtrack(state, choices, path, result):
    # 1. Base Case / Goal Met
    if is_solution(state):
        result.append(list(path)) # Store a copy of the valid solution
        return

    # 2. Iterate through available options
    for choice in choices:
        # 3. Apply Constraints (Pruning)
        if not is_valid(choice, state):
            continue
        
        # 4. Make Choice
        make_choice(choice, state, path)
        
        # 5. Explore Next Level
        backtrack(state, choices, path, result)
        
        # 6. Undo Choice (The Backtrack Step)
        undo_choice(choice, state, path)

