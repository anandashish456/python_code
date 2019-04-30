with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for lines in rf:
            wf.write(lines)
