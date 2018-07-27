# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    emptyset_vn = set() #An empty set is created to keep track of visited nodes
    stack_fr = util.Stack() #An empty stack is created for DFS implementation
    initial_path = []
    stack_fr.push((problem.getStartState(),initial_path, 0)) #Problem's start state, empty list for the path and current cost are pushed in the stack
    while stack_fr: #while the stack is not empty
        cState, cPath, cCost = stack_fr.pop() #pop the current values from the stack based on LIFO
        if not cState in emptyset_vn: #if the current state is not in the visted nodes set then add the current state in the visited nodes set
            emptyset_vn.add(cState)
            if problem.isGoalState(cState): #if the current state is the goal state then return the path travelled to reach the goal state
                return cPath
            for nState, nPath, nCost in problem.getSuccessors(cState): #for every successor state keep pushing the nextstate, new path + current path and  newcost + current cost in the stack
                stack_fr.push((nState, cPath + [nPath], cCost + nCost))
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    emptyset_vn = set()  # An empty set is created to keep track of visited nodes
    queue_fr = util.Queue()  # An empty queue is created for BFS implementation
    initial_path = []
    queue_fr.push((problem.getStartState(), initial_path, 0))  # Problem's start state, empty list for the path and current cost are pushed in the stack
    while queue_fr:  # while the queue is not empty
        cState, cPath, cCost = queue_fr.pop()  # pop the current values from the queue based on FIFO
        if not cState in emptyset_vn:  # if the current state is not in the visted nodes set then add the current state in the visited nodes set
            emptyset_vn.add(cState)
            if problem.isGoalState(cState):  # if the current state is the goal state then return the path travelled to reach the goal state
                return cPath
            for nState, nPath, nCost in problem.getSuccessors(cState):  # for every successor state keep pushing the nextstate, new path + current path and  newcost + current cost in the queue
                queue_fr.push((nState, cPath + [nPath], cCost + nCost))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    emptyset_vn = set()  # An empty set is created to keep track of visited nodes
    pQueue_fr = util.PriorityQueue()  # An empty priority queue is created for UCS implementation by setting priority for the cheapest nodes
    initial_path = []
    pQueue_fr.push((problem.getStartState(), initial_path, 0), 0)  # Problem's start state, empty list for the path and current cost are pushed in the stack
    while pQueue_fr:  # while the priority queue is not empty
        cState, cPath, cCost = pQueue_fr.pop()  # pop the current values from the priority queue based on priority
        if not cState in emptyset_vn:  # if the current state is not in the visted nodes set then add the current state in the visited nodes set
            emptyset_vn.add(cState)
            if problem.isGoalState(cState):  # if the current state is the goal state then return the path travelled to reach the goal state
                return cPath
            for nState, nPath, nCost in problem.getSuccessors(cState):  # for every successor state keep pushing the nextstate, new path + current path and  newcost + current cost in the priority queue
                pQueue_fr.push((nState, cPath + [nPath] ,cCost + nCost), cCost + nCost)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    emptyset_vn = set()  # An empty set is created to keep track of visited nodes
    pQueue_fr = util.PriorityQueue()  # An empty priority queue is created for UCS implementation by setting priority for the cheapest nodes
    initial_path = []
    pQueue_fr.push((problem.getStartState(), initial_path, 0), 0)  # Problem's start state, empty list for the path and current cost are pushed in the stack
    while pQueue_fr:  # while the priority queue is not empty
        cState, cPath, cCost = pQueue_fr.pop()  # pop the current values from the priority queue based on priority
        if not cState in emptyset_vn:  # if the current state is not in the visted nodes set then add the current state in the visited nodes set
            emptyset_vn.add(cState)
            if problem.isGoalState(cState):  # if the current state is the goal state then return the path travelled to reach the goal state
                return cPath
            for nState, nPath, nCost in problem.getSuccessors(cState):# for every successor state keep pushing the nextstate, new path + current path and  newcost + current cost in the queue
                heur = heuristic (nState,problem) #for every new state call the heuristic function and add that heuristic value to the cost
                pQueue_fr.push((nState, cPath + [nPath], cCost + nCost), cCost + nCost + heur)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
