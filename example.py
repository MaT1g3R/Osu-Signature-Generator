from osu_sig import generate, Mode  # both imports are necessary

if __name__ == '__main__':
    # This showcases the most simple usage
    print(generate('Underforest', '0286F4'))

    # This showcases a more advanced usage
    print(generate('MaT1g3R', '0286F4', Mode.taiko, 1, removemargin=True,
                   xpbar=True, xpbarhex=True, onlineindicator=3,
                   avatarrounding=100))

    # more details can be found in the python docstrings or in the wiki.
