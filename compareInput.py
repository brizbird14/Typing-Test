

#def testCorrections(test_input, test_template):
def testCorrections(user_in, template):
        #user_in = str(test_input)
        #template = str(test_template)

        error_count = 0
        error_indices = [] # creates list that contains indices of errors

        print('test input: ', user_in)
        print('test template: ', template)

        index = 0

        # before loop, checks which longer (don't want to compare out of bound)

        for letter in template:
            if (index >= len(user_in)): # if input shorter than template
                error_count += (len(template) - index)
                # print('length discrepancy detected, BREAKING --------------------------')
                break
            if (user_in[index] != template[index]):
                error_count += 1
                error_indices.append(index)
            index = index + 1

        # at end of loop, if input longer than template
        if (len(user_in) > len(template)):
            error_count += (len(user_in) - len(template))

        # if case where input shorter than template, fill error_indices to end
        while index < len(template):
            error_indices.append(index)
            index = index + 1

        print('error count before return: ', error_count)

        return (error_count, error_indices)