import pandas as pd


def and_perceptron(v1, v2):
    # TODO: create an AND perceptron
    weight1 = 1.0
    weight2 = 1.0
    bias = -2.0
    linear_combination = weight1 * \
        v1 + weight2 * v2 + bias
    return int(linear_combination >= 0)

def or_perceptron(v1, v2):
    weight1 = 1.0
    weight2 = 1.0
    bias = -0.5
    linear_combination = weight1 * \
        v1 + weight2 * v2 + bias
    return int(linear_combination >= 0)


def not_perceptron(v):
    weight = -1.0
    bias = 0.0
    linear_combination = weight * v + bias
    return int(linear_combination >= 0)


def xor_perceptron(v1, v2):
    o1 = and_perceptron(v1,v2)
    o2 = or_perceptron(v1,v2)
    o3 = not_perceptron(o1)
    return and_perceptron(o2,o3)


if __name__ == "__main__":

    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    correct_outputs = [False, True, True, False]
    outputs = []

    for test_input, correct_output in zip(test_inputs, correct_outputs):
        output = xor_perceptron(test_input[0], test_input[1])
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1],
                        output, is_correct_string])
    num_wrong = len([output[3] for output in outputs if output[3] == 'No'])
    output_frame = pd.DataFrame(outputs, columns=[
                                'Input 1', '  Input 2', '  Activation Output', '  Is Correct'])
    if not num_wrong:
        print('Nice!  You got it all correct.\n')
    else:
        print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
    print(output_frame.to_string(index=False))
