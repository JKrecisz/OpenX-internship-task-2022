# Task 1
### What the script does
The program present whole Supply Chain tree for OpenX in an easy to read way.

### Problems encountered
Approaching this task, I wanted everything to take place in a separate window, the so-called gui. I wanted everything to
be arranged hierarchically and to easily expand the seller into his under seller. Unfortunately, time was not in my favor,
it took a while to learn PyQt5 and the task had to be handed over.

If I had more time and skills with the new PyQt5 library, I would have done it in a different way. My idea was that the 
program, when turned on, would write out the main sellers. Only when we click on a specific seller, I wanted the program
to download under seller data for that seller and then expand the list with them. This would reduce the time opening of
a program, as I have noticed that just checking out 1st degree under sellers is very time consuming.

The last problem I encountered was the fact that some companies do not provide their sellers in the domain ending in _sellers.json_.

### How to run

Before everything, check if you have these libraries:
- sys
- json
- urllib
- PyQt5

If not, just download them like:

```text
pip install PyQt5
    # or
pip3 install PyQt5
```
Then, download the entire repository:
```text
git clone https://github.com/JKrecisz/OpenX-internship-task-2022.git
```
Next:
```text
cd OpenX-internship-task-2022
# then
cd task1
```

Now, just run it:
```text
python3 supply-chain-tree.py
```

### How it looks
