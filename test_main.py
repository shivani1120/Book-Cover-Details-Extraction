from files.text import Text

# for single file
def test_answer():
    path = "/Users/apple/Desktop/SE/CS305-2019CSB1120-3/images/Clean_code.png"
    flag = "0"
    info = []
    text = Text()
    info.append(text.get_info(path))
    assert (info == [['Clean Code C. R. * + * ', 'NJ + Boston + Indianapolis * San Francisco Object Mentor Inc. ', 'Robert C. Martin Michael C. Feathers Timothy R. Ottinger Joffrey J. Langr Brett L. Schuchert James W. Grenning Kevin Dean Wampler Robert C. Martin Michael C. Feathers Timothy R. Ottinger Jeffrey J. Langr Brett L. Schuchert James W. Grenning Kevin Dean Wampler ', None]])

# for folder
def test_answer_folder():
    path = "/Users/apple/Desktop/SE/CS305-2019CSB1120-3/images"
    flag = "1"
    info = []
    text = Text()
    info.append(text.get_data(path,flag))
    assert (info == [[['Clean Code ', '', 'Robert C. Martin Series Robert © Martin ', None], ['Clean Code C. R. * + * ', 'NJ + Boston + Indianapolis * San Francisco Object Mentor Inc. ', 'Robert C. Martin Michael C. Feathers Timothy R. Ottinger Joffrey J. Langr Brett L. Schuchert James W. Grenning Kevin Dean Wampler Robert C. Martin Michael C. Feathers Timothy R. Ottinger Jeffrey J. Langr Brett L. Schuchert James W. Grenning Kevin Dean Wampler ', None], ['ISBN 978-0-7334-2609-4 9780733426094 ', '', '', ' 978-0-7334-2609-4\n']]])


    


