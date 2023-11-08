class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        justification = []
        line = [words[0]]
        linelen = len(words[0])
        def justify_words(line, linelen):
            if len(line) == 1:
                justification.append(line[0]+' '*(maxWidth - linelen))
                return
            remaining_space = maxWidth - linelen
            no_of_spaces = len(line) - 1
            equal = remaining_space // no_of_spaces
            slack = remaining_space - equal * no_of_spaces
            myline = str(line[0])
            for word in line[1:]:
                myline += ' '
                myline += ' '*equal
                if slack:
                    myline += ' '
                    slack -= 1
                myline += word
            justification.append(myline)
        for word in words[1:]:
            wordlen = len(word)+1
            if linelen + wordlen <= maxWidth:
                line.append(word)
                linelen += wordlen
            else:
                justify_words(line, linelen)
                line = [word]
                linelen = wordlen - 1
        myline = line[0]
        for word in line[1:]:
            myline += ' '
            myline += word
        myline += ' '*(maxWidth - linelen)
        justification.append(myline)
        return justification

        