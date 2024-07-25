from browser import document, alert

# Function to convert input matrix to 3x3 list
def get_matrix(prefix):
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            element = document[f"{prefix}_matrix_{i}{j}"].value
            row.append(int(element))
        matrix.append(row)
    return matrix

# Function to encode the string
def encode(event):
    input_string = document['encode_string'].value
    if not input_string:
        alert("Please enter a string to encode.")
        return

    matrix = get_matrix('e')
    input_list = [ord(char) for char in input_string]

    if len(input_list) % 3 != 0:
        input_list += [0] * (3 - len(input_list) % 3)

    encoded_list = []
    for i in range(0, len(input_list), 3):
        for j in range(3):
            encoded_value = sum(input_list[i + k] * matrix[k][j] for k in range(3))
            encoded_list.append(encoded_value)

    document['encoded_output'].text = str(encoded_list)

# Function to decode the list
def decode(event):
    input_list = document['decode_list'].value
    if not input_list:
        alert("Please enter a list to decode.")
        return

    input_list = eval(input_list)
    matrix = get_matrix('d')

    decoded_chars = []
    for i in range(0, len(input_list), 3):
        for j in range(3):
            decoded_value = sum(input_list[i + k] * matrix[j][k] for k in range(3))
            decoded_chars.append(chr(decoded_value))

    document['decoded_output'].text = ''.join(decoded_chars)

document['encode_button'].bind('click', encode)
document['decode_button'].bind('click', decode)
