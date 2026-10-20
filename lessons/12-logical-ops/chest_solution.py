# Your turn, solved: open a treasure chest
has_key = False
has_lockpick = True
stunned = False

if (has_key or has_lockpick) and not stunned:
    print("The chest opens.")
else:
    print("The chest stays shut.")
