def get_input():

    userinput = []

    userinput.append(input("Enter the heading 1: "))
    userinput.append(input("Enter a paragraph: "))
    userinput.append(input("Enter reference paragraph: "))
    userinput.append(input("Enter reference display message: "))
    userinput.append(input("Enter reference links: "))

    return userinput

def file_structurer(userinput):

    h1 = '# ' + '**%s**' % userinput[0]
    p = userinput[1]
    ref_text = userinput[2]
    ref = '[%s]' % userinput[3]
    href = '(%s)' % userinput[4]

    line_ref = ref_text + ' ' + ref + href + '.'

    return [h1, p, line_ref]

def write_tofile(structured_list):

    content = '\n\n'.join(structured_list)

    with open('README.md', 'w') as f:

        f.write(content)

def run_main():

    user_input = get_input()
    structured_inlist = file_structurer(user_input)
    write_tofile(structured_inlist)

run_main()