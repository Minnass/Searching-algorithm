from Space import *
from Constants import *
import math
from queue import PriorityQueue
def DFS(g: Graph, sc: pygame.Surface):
    open_set = []
    open_set.append(g.start)
    closed_set = []
    father = [-1]*g.get_len()
    while (len(open_set) != 0):
        current_node = open_set.pop()
        if (current_node in closed_set):
            continue
        closed_set.append(current_node)
        if (current_node != g.goal):
            pygame.time.wait(50)
            current_node.set_color(yellow)
            current_node.draw(sc)
            pygame.display.flip()
        if (current_node.value == g.goal.value):
            position = g.goal.value
            path = []
            while (father[position] != -1):
                path.append(father[position])
                position = father[position]
            begin_Point = g.goal
            while (len(path) != 0):
                pygame.time.wait(100)
                index = path.pop(0)
                end_Point = g.grid_cells[index]
                if(index!=g.start.value):
                    end_Point.set_color(grey)
                    end_Point.draw(sc)
                pygame.draw.line(sc, grey,
                                 (begin_Point.x, begin_Point.y), (end_Point.x, end_Point.y), 2)
                pygame.display.flip()
                begin_Point = end_Point
            break
        neighbors = g.get_neighbors(current_node)
        for neighbor in neighbors:
            if (neighbor not in closed_set):
                pygame.time.wait(50)
                if (neighbor != g.goal):
                    neighbor.set_color(red)
                    neighbor.draw(sc)
                    pygame.display.flip()
                open_set.append(neighbor)
                father[neighbor.value] = current_node.value
        if (current_node != g.start and current_node != g.goal):
            current_node.set_color(blue)
            current_node.draw(sc)
            pygame.display.flip()


def BFS(g: Graph, sc: pygame.Surface):
    open_set = []
    open_set.append(g.start)
    closed_set = []
    closed_set.append(g.start)
    father = [-1]*g.get_len()
    while (len(open_set) != 0):
        current_node = open_set.pop(0)
        if (current_node != g.goal):
            pygame.time.wait(50)
            current_node.set_color(yellow)
            current_node.draw(sc)
            pygame.display.flip()
        if (current_node.value == g.goal.value):
            position = g.goal.value
            path = []
            while (father[position] != -1):
                path.append(father[position])
                position = father[position]
            begin_Point = g.goal
            while (len(path) != 0):
                pygame.time.wait(100)
                index = path.pop(0)
                end_Point = g.grid_cells[index]
                if(index!=g.start.value):
                    end_Point.set_color(grey)
                    end_Point.draw(sc)
                pygame.draw.line(sc, grey,
                                 (begin_Point.x, begin_Point.y), (end_Point.x, end_Point.y), 2)
                pygame.display.flip()
                begin_Point = end_Point
            break
        neighbors = g.get_neighbors(current_node)
        for neighbor in neighbors:
            if (neighbor not in closed_set):
                pygame.time.wait(50)
                if (neighbor != g.goal):
                    neighbor.set_color(red)
                    neighbor.draw(sc)
                    pygame.display.flip()
                open_set.append(neighbor)
                closed_set.append(neighbor)
                father[neighbor.value] = current_node.value
        if (current_node != g.start and current_node != g.goal):
            current_node.set_color(blue)
            current_node.draw(sc)
            pygame.display.flip()


def calculate_distance(From: Node, To: Node):
    return math.sqrt(pow(To.x-From.x, 2)+pow(To.y-From.y, 2))


def UCS(g: Graph, sc: pygame.Surface):
    open_set: list[(float, Node)] = []
    open_set.append((0, g.start))
    closed_set: list[Node] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0
    while (len(open_set) != 0):
        current_node = open_set.pop(0)[1]
        closed_set.append(current_node)
        if (current_node != g.goal):
            pygame.time.wait(50)
            current_node.set_color(yellow)
            current_node.draw(sc)
            pygame.display.flip()
        if (current_node.value == g.goal.value):
            position = g.goal.value
            path = []
            while (father[position] != -1):
                path.append(father[position])
                position = father[position]
            begin_Point = g.goal
            while (len(path) != 0):
                pygame.time.wait(100)
                index = path.pop(0)
                end_Point = g.grid_cells[index]
                if(index!=g.start.value):
                    end_Point.set_color(grey)
                    end_Point.draw(sc)
                pygame.draw.line(sc, grey,
                                 (begin_Point.x, begin_Point.y), (end_Point.x, end_Point.y), 2)
                pygame.display.flip()
                begin_Point = end_Point
            break
        neighbors = g.get_neighbors(current_node)
        for neighbor in neighbors:
            if (neighbor not in closed_set and cost[neighbor.value] > cost[current_node.value]+calculate_distance(current_node, neighbor)):
                cost[neighbor.value] = cost[current_node.value] + \
                    calculate_distance(current_node, neighbor)
                open_set.append((cost[neighbor.value], neighbor))
                father[neighbor.value] = current_node.value
                if (neighbor != g.goal):
                    pygame.time.wait(50)
                    neighbor.set_color(red)
                    neighbor.draw(sc)
                    pygame.display.flip()
        open_set.sort(key=lambda tup: tup[0])
        if (current_node != g.start and current_node != g.goal):
            current_node.set_color(blue)
            current_node.draw(sc)
            pygame.display.flip()


def heuristic(current_node: Node, goal: Node):
    dx = abs(current_node.x-goal.x)
    dy = abs(current_node.y-goal.y)
    return math.sqrt(pow(dx, 2)+pow(dy, 2))


def AStar(g: Graph, sc: pygame.Surface):
    open_set: list[(float, Node)] = []
    open_set.append((0, g.start))
    closed_set: list[Node] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0
    fxN = [1000_000]*g.get_len()

    while (len(open_set)):
        current_node = open_set.pop(0)[1]
        closed_set.append(current_node)
        if (current_node != g.goal):
            pygame.time.wait(50)
            current_node.set_color(yellow)
            current_node.draw(sc)
            pygame.display.flip()
        if (current_node.value == g.goal.value):
            position = g.goal.value
            path = []
            while (father[position] != -1):
                path.append(father[position])
                position = father[position]
            begin_Point = g.goal
            while (len(path) != 0):
                pygame.time.wait(100)
                index = path.pop(0)
                end_Point = g.grid_cells[index]
                if(index!=g.start.value):
                    end_Point.set_color(grey)
                    end_Point.draw(sc)
                pygame.draw.line(sc, grey,
                                 (begin_Point.x, begin_Point.y), (end_Point.x, end_Point.y), 2)
                pygame.display.flip()
                begin_Point = end_Point
            break
        neighbors = g.get_neighbors(current_node)
        for neighbor in neighbors:
            hN = heuristic(neighbor, g.goal)
            gN = cost[current_node.value] + \
                calculate_distance(current_node, neighbor)
            fN = hN+gN
            if (neighbor not in closed_set and fxN[neighbor.value] > fN):
                if (neighbor != g.goal):
                    pygame.time.wait(50)
                    neighbor.set_color(red)
                    neighbor.draw(sc)
                    pygame.display.flip()
                fxN[neighbor.value] = fN
                open_set.append((fN, neighbor))
                father[neighbor.value] = current_node.value
        open_set.sort(key=lambda tup: tup[0])
        if (current_node != g.start and current_node != g.goal):
            current_node.set_color(blue)
            current_node.draw(sc)
            pygame.display.flip()

    # TODO: Implement A* algorithm using open_set, closed_set, and father
