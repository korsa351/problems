with open("input.txt", "r") as inp, open("output.txt", "w") as out:
    seq_symbls = [i.strip() for i in inp]
    out.write('\n'.join(seq_symbls[::-1]))