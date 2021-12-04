## --- Day 2: Dive! ---

Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like `forward 1`, `down 2`, or `up 3`:

-   `forward X` increases the horizontal position by `X` units.
-   `down X` _increases_ the depth by `X` units.
-   `up X` _decreases_ the depth by `X` units.

Note that since you're on a submarine, `down` and `up` affect your _depth_, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

```
forward 5
down 5
forward 8
up 3
down 8
forward 2
```

Your horizontal position and depth both start at `0`. The steps above would then modify them as follows:

-   `forward 5` adds `5` to your horizontal position, a total of `5`.
-   `down 5` adds `5` to your depth, resulting in a value of `5`.
-   `forward 8` adds `8` to your horizontal position, a total of `13`.
-   `up 3` decreases your depth by `3`, resulting in a value of `2`.
-   `down 8` adds `8` to your depth, resulting in a value of `10`.
-   `forward 2` adds `2` to your horizontal position, a total of `15`.

After following these instructions, you would have a horizontal position of `15` and a depth of `10`. (Multiplying these together produces `_150_`.)

Calculate the horizontal position and depth you would have after following the planned course. _What do you get if you multiply your final horizontal position by your final depth?_

```python
# dive - using function with return values


def parse_line(command_line, forward, depth):
    """
    takes a command, and parses it
    """
    direction, units_str = command_line.strip().replace("\n", "").split(" ")
    units = int(units_str)
    if direction == "forward":
        forward += units
    elif direction == "down":
        depth += units
    elif direction == "up":
        depth -= units
    else:
        raise ValueError("invalid line")

    return (forward, depth)


with open("input_files/problem2.txt", "r") as f:
    forward, depth = 0, 0
    for line in f:
        forward, depth = parse_line(line, forward, depth)

print(f"forward is {forward}, depth is {depth}")
print(f"the answer is {forward * depth}")

```

## --- Part Two ---

Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a third value, _aim_, which also starts at `0`. The commands also mean something entirely different than you first thought:

-   `down X` _increases_ your aim by `X` units.
-   `up X` _decreases_ your aim by `X` units.
-   `forward X` does two things:
    -   It increases your horizontal position by `X` units.
    -   It increases your depth by your aim _multiplied by_ `X`.

Again note that since you're on a submarine, `down` and `up` do the opposite of what you might expect: "down" means aiming in the positive direction.

Now, the above example does something different:

-   `forward 5` adds `5` to your horizontal position, a total of `5`. Because your aim is `0`, your depth does not change.
-   `down 5` adds `5` to your aim, resulting in a value of `5`.
-   `forward 8` adds `8` to your horizontal position, a total of `13`. Because your aim is `5`, your depth increases by `8*5=40`.
-   `up 3` decreases your aim by `3`, resulting in a value of `2`.
-   `down 8` adds `8` to your aim, resulting in a value of `10`.
-   `forward 2` adds `2` to your horizontal position, a total of `15`. Because your aim is `10`, your depth increases by `2*10=20` to a total of `60`.

After following these new instructions, you would have a horizontal position of `15` and a depth of `60`. (Multiplying these produces `_900_`.)

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. _What do you get if you multiply your final horizontal position by your final depth?_

```python
# part 2

# dive - using collector

#  horizontal, depth, aim
collector = [0, 0, 0]


def parse_line(command_line, collector):
    """
    takes a command, and parses it
    """
    horizontal, depth, aim = collector
    direction, units_str = command_line.strip().replace("\n", "").split(" ")
    units = int(units_str)
    if direction == "forward":
        horizontal += units
        depth += aim * units
    elif direction == "down":
        aim += units
    elif direction == "up":
        aim -= units
    else:
        raise ValueError("invalid line")

    collector[0], collector[1], collector[2] = horizontal, depth, aim
    return


with open("input_files/problem2.txt", "r") as f:
    for line in f:
        parse_line(line, collector)

forward, depth, aim = collector

print(f"forward is {forward}, depth is {depth}")
print(f"the answer is {forward * depth}")

```