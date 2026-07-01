# Enumerate()

`enumerate()` is a Python built-in function used to track both the index, or custom counter, and value of items in an iterable (such as a `list`, `dictionary`, `tuple`, or `string`) simultaneously.

The `enumerate` function accepts two arguments, an  `iterable` and an optional numeric `start` value. The `start` value defaults to `0` unless we specify a starting value.

The function returns the elements of the iterable as a `tuple` containing the index or counter and the value of the element.

```python
coolest_bears = ["Boots", "Yogi", "Paddington"]

enumerated = list(enumerate(coolest_bears))
print(enumerated)  # [(0, 'Boots'), (1, 'Yogi'), (2, 'Paddington')]
```

This allows us to write loops that require us to keep track of index positions without the use of `range(len(iterable))` or without having to manually keep track of a counter variable.

For example:

```python
tasks = ["Log in to Boot.dev", "Drink XP Potion", "Give Boots some Salmon"]

for i in range(0, len(tasks)):
 print(f"{i + 1}. {tasks[i]}")
 
# Output:
# 1. Log in to Boot.dev
# 2. Drink XP Potion
# 3. Give Boots some Salmon
```

is the same as:

```python
tasks = ["Log in to Boot.dev", "Drink XP Potion", "Give Boots some Salmon"]

for num, task in enumerate(tasks, start=1):
 print(f"{num}. {task}")
 
# Output:
# 1. Log in to Boot.dev
# 2. Drink XP Potion
# 3. Give Boots some Salmon
```

We can use tuple unpacking to capture the index or counter and value for each iteration, then use those values directly within the loop. This gives us a way to write loops that is more readable and easier to reason about.

## Assignment

As a text-based RPG, Fantasy Quest has thousands of lines of text dialog. One of our proofreaders has flagged that we have been misspelling an NPC's name!

We need to write a function to find and replace all the instances of the typo and update the logging system as it runs. As there are so many lines we only need to update the logging system after a set number of lines have been parsed so our logs can stay as clear as possible.

Let's finish the `find_and_replace` function.

1. [ ] Initialize a variable to act as a counter for how many errors we've found. I called mine `found` but you can use any name that makes sense to you.
2. [ ] We're going to simulate a log by creating an empty list and adding our log messages to it.
3. [ ] Loop over the `lines` list and use `enumerate()` with a `start` value of `1`
 1. [ ] Within the loop, check if the current line contains `name_err`
  1. [ ] If so, replace the instance of the `name_err` with `actual_name`
  2. [ ] Increment the `found` counter
 2. [ ] Check to see if current line number is divisible by `3`
  1. [ ] If so, append the return value of the `update_log` function to our `log` list
4. [ ] Return the `log`

## Tip

- The Python [str.replace()]("https://docs.python.org/3/library/stdtypes.html#str.replace")string method might be useful for replacing words in a string
