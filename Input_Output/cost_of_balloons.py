green, purple = 0, 1

for case in range(int(input())):
    green_balloon_cost, purple_balloon_cost = map(int, input().split())

    total_green_balloons = 0
    total_purple_balloons = 0

    for participant in range(int(input())):
        solved_problems = [int(x) for x in input().split()]
        total_green_balloons += solved_problems[green]
        total_purple_balloons += solved_problems[purple]

    print(total_green_balloons * green_balloon_cost + total_purple_balloons * purple_balloon_cost)
    green, purple = purple, green
