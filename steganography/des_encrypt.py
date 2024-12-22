
import os
import numpy as np
from PIL import Image


#get phootos and convert them to bytes arrays

image_path_rgb = "H:/subjects/Fth/First Term/secuirty/Project/front/src/Photos/RGBPhoto.png"
image_path_gray = "H:/subjects/Fth/First Term/secuirty/Project/front/src/Photos/GrayPhoto.png"
def convert_rgb_to_byte_array():
    try:
        with Image.open(image_path_rgb) as img:
            rgb_img = img.convert('RGB')

        img_data = np.array(rgb_img)
        byte_array = img_data.flatten().tolist()
        return byte_array

    except Exception as e:
        print(f"Error processing image: {e}")
        return "Error"

def convert_image_to_byte_array():
    image_path = image_path_gray
    try:
        temp_file_path = image_path.replace('.png', '_temp.png')

        with Image.open(image_path) as img:
            grayscale_img = img.convert('L')
            grayscale_img.save(temp_file_path)

        img_data = np.array(grayscale_img)
        byte_array = img_data.flatten().tolist()
        os.remove(temp_file_path)
        return byte_array

    except Exception as e:
        print(f"Error processing image: {e}")
        return "Error"

#tables for encryption and decryption

ip_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
# PC1 permutation table
pc1_table = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]
# Define the left shift schedule for each round
shift_schedule = [1, 1, 2, 2,
                  2, 2, 2, 2,
                  1, 2, 2, 2,
                  2, 2, 2, 1]
# PC2 permutation table
pc2_table = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]
#expension
e_box_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]
# S-box tables for DES
s_boxes = [
    # S-box 1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S-box 2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S-box 3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S-box 4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S-box 5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S-box 6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S-box 7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S-box 8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]
p_box_table = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]
ip_inverse_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]


#function to get sublist and return string of bits
def get_sublist_as_bitstring(lst, start, end):
    sublist = lst[start:end+1]
    # print(sublist)
    bit_string = ''.join(format(item, '08b') for item in sublist)
    return bit_string

# functino take string bit and convert it to the list of bytes
def binstring_to_sublist(bit_string):
    # Ensure the bit string is exactly 64 bits long
    bit_string = bit_string[:64].ljust(64, '0')
    # Split the bit string into 8-bit chunks
    sublist = [int(bit_string[i:i + 8], 2) for i in range(0, 64, 8)]
    return sublist

#initial permutatino of the binary string
def ip_on_binary_rep(binary_representation):
    ip_result = [None] * 64
    for i in range(64):
        ip_result[i] = binary_representation[ip_table[i] - 1]
    # Convert the result back to a string for better visualization
    ip_result_str = ''.join(ip_result)
    return ip_result_str

#function to generate the key
def key_in_binary_conv():
    # Original key (can be changed but it should be 8 char)
    original_key = 'abcdefgh'
    binary_representation_key = ''

    for char in original_key:
        # Convert the characters to binary and concatenate to form a 64-bit binary string
        binary_key = format(ord(char), '08b')
        binary_representation_key += binary_key

    return binary_representation_key

#funciton to generat the subkeys and save it in a list
def generate_round_keys():
    # Key into binary
    binary_representation_key = key_in_binary_conv()
    pc1_key_str = ''.join(binary_representation_key[bit - 1] for bit in pc1_table)

    # Split the 56-bit key into two 28-bit halves
    c0 = pc1_key_str[:28]
    d0 = pc1_key_str[28:]
    round_keys = []
    for round_num in range(16):
        # Perform left circular shift on C and D
        c0 = c0[shift_schedule[round_num]:] + c0[:shift_schedule[round_num]]
        d0 = d0[shift_schedule[round_num]:] + d0[:shift_schedule[round_num]]
        # Concatenate C and D
        cd_concatenated = c0 + d0

        # Apply the PC2 permutation
        round_key = ''.join(cd_concatenated[bit - 1] for bit in pc2_table)

        # Store the round key
        round_keys.append(round_key)
    return round_keys

def encryption(user_input,start,end):
    binary_rep_of_input = get_sublist_as_bitstring(user_input,start,end)
    # Initialize lists to store round keys
    round_keys = generate_round_keys()

    ip_result_str = ip_on_binary_rep(binary_rep_of_input)

    # the initial permutation result is devided into 2 halfs
    lpt = ip_result_str[:32]
    rpt = ip_result_str[32:]

    # Assume 'rpt' is the 32-bit right half, 'lpt' is the 32-bit left half, and 'round_keys' is a list of 16 round keys

    for round_num in range(16):
        # Perform expansion (32 bits to 48 bits)
        expanded_result = [rpt[i - 1] for i in e_box_table]
        expanded_result_str = ''.join(expanded_result)
        round_key_str = round_keys[round_num]

        xor_result_str = ''
        for i in range(48):
            xor_result_str += str(int(expanded_result_str[i]) ^ int(round_key_str[i]))
        six_bit_groups = [xor_result_str[i:i + 6] for i in range(0, 48, 6)]

        # Initialize the substituted bits string
        s_box_substituted = ''

        # Apply S-box substitution for each 6-bit group
        for i in range(8):
            # Extract the row and column bits
            row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
            col_bits = int(six_bit_groups[i][1:-1], 2)
            # Lookup the S-box value
            s_box_value = s_boxes[i][row_bits][col_bits]
            # Convert the S-box value to a 4-bit binary string and append to the result
            s_box_substituted += format(s_box_value, '04b')
        # Apply a P permutation to the result
        p_box_result = [s_box_substituted[i - 1] for i in p_box_table]
        # # Convert the result back to a string for better visualization
        # p_box_result_str = ''.join(p_box_result)
        # Convert LPT to a list of bits for the XOR operation
        lpt_list = list(lpt)
        # Perform XOR operation
        new_rpt = [str(int(lpt_list[i]) ^ int(p_box_result[i])) for i in range(32)]
        # Convert the result back to a string for better visualization
        new_rpt_str = ''.join(new_rpt)

        # Update LPT and RPT for the next round
        lpt = rpt
        rpt = new_rpt_str



    # print('\n')
    # At this point, 'lpt' and 'rpt' contain the final left and right halves after 16 rounds

    # After the final round, reverse the last swap
    final_result = rpt + lpt

    # Perform the final permutation (IP-1)
    final_cipher = [final_result[ip_inverse_table[i] - 1] for i in range(64)]

    # Convert the result back to a string for better visualization
    final_cipher_str = ''.join(final_cipher)

    # Convert binary cipher to ingeter list
    final_cipher_ascii = binstring_to_sublist(final_cipher_str)
    # print("Final Cipher text:", final_cipher_ascii, len(final_cipher_ascii))
    return final_cipher_ascii

#start doing the encryption

def encrypt_graylist_in_chunks(grayList):
    try:
        encrypted_chunks = []
        for start in range(0, len(grayList), 8):
            chunk = grayList[start:start + 8]
            if len(chunk) < 8:
                chunk += [0] * (8 - len(chunk))
            encrypted_chunk = encryption(chunk, 0, 8)
            encrypted_chunks.extend(encrypted_chunk)  # Add items to the flat list
        return encrypted_chunks

    except Exception as e:
        print(f"Error encrypting graylist: {e}")
        return "Error"

def apply_lsb_steganography(rgbList, res):
    res_bits = ''.join(format(num, '08b') for num in res)
    modified_rgbList = []
    for i in range(len(rgbList)):
        rgb_byte = format(rgbList[i], '08b')
        if i < len(res_bits):
            new_byte = rgb_byte[:-1] + res_bits[i]
        else:
            new_byte = rgb_byte
        modified_rgbList.append(int(new_byte, 2))  # Convert back to an integer
    return modified_rgbList

def modify_and_save_rgb_image(input_image_path, modified_list, output_image_path):
    input_image = Image.open(input_image_path)
    width, height = input_image.size

    # Step 2: Ensure the modified_list matches the required size
    expected_size = width * height * 3
    if len(modified_list) < expected_size:
        # Pad with zeros if the list is too short
        modified_list += [0] * (expected_size - len(modified_list))
    elif len(modified_list) > expected_size:
        # Truncate if the list is too long
        modified_list = modified_list[:expected_size]

    #Convert the flat list to a list of RGB tuples
    rgb_data = [tuple(modified_list[i:i+3]) for i in range(0, len(modified_list), 3)]

    #Create a new image with the same dimensions as the input
    new_image = Image.new("RGB", (width, height))
    new_image.putdata(rgb_data)

    #Save the new image to the specified output path
    new_image.save(output_image_path)
    print(f"Modified image saved at: {output_image_path}")

input_image_path = r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\RGBPhoto.png"
output_image_path = r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\stegoPhoto.png"

#function that will start everything
def start_encrypt():
    print("start encrypting")
    grayList = convert_image_to_byte_array()
    rgbList = convert_rgb_to_byte_array()
    try:
        res = encrypt_graylist_in_chunks(grayList)
        modified = apply_lsb_steganography(rgbList, res)
        modify_and_save_rgb_image(input_image_path, modified, output_image_path)
        return "Success"
    except :
        return "Failed"

# start_encrypt()
# only call the start encrypt function


def decryption(final_cipher):
    # Initialize lists to store round keys
    round_keys = generate_round_keys()
    # Apply Initial Permutation
    ip_dec_result_str = ip_on_binary_rep(get_sublist_as_bitstring(final_cipher, 0,8 ))
    lpt = ip_dec_result_str[:32]
    rpt = ip_dec_result_str[32:]
    for round_num in range(16):
        # Perform expansion (32 bits to 48 bits)
        expanded_result = [rpt[i - 1] for i in e_box_table]

        # Convert the result back to a string for better visualization
        expanded_result_str = ''.join(expanded_result)
        # print(expanded_result_str)
        # Round key for the current round
        round_key_str = round_keys[15 - round_num]

        # XOR between key and expanded result
        xor_result_str = ''
        for i in range(48):
            xor_result_str += str(int(expanded_result_str[i]) ^ int(round_key_str[i]))

        # Split the 48-bit string into 8 groups of 6 bits each
        six_bit_groups = [xor_result_str[i:i + 6] for i in range(0, 48, 6)]

        # Initialize the substituted bits string
        s_box_substituted = ''

        # Apply S-box substitution for each 6-bit group
        for i in range(8):
            # Extract the row and column bits
            row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
            col_bits = int(six_bit_groups[i][1:-1], 2)

            # Lookup the S-box value
            s_box_value = s_boxes[i][row_bits][col_bits]

            # Convert the S-box value to a 4-bit binary string and append to the result
            s_box_substituted += format(s_box_value, '04b')

        # Apply a P permutation to the result
        p_box_result = [s_box_substituted[i - 1] for i in p_box_table]

        # Convert the result back to a string for better visualization
        # p_box_result_str = ''.join(p_box_result)

        # Convert LPT to a list of bits for the XOR operation
        lpt_list = list(lpt)

        # Perform XOR operation
        new_rpt = [str(int(lpt_list[i]) ^ int(p_box_result[i])) for i in range(32)]

        # Convert the result back to a string for better visualization
        new_rpt_str = ''.join(new_rpt)

        # Update LPT and RPT for the next round
        lpt = rpt
        rpt = new_rpt_str

        # Print or use the RPT for each round

    # print('\n')
    final_result = rpt + lpt
    # Perform the final permutation (IP-1)
    final_cipher = [final_result[ip_inverse_table[i] - 1] for i in range(64)]

    # Convert the result back to a string for better visualization
    final_cipher_str = ''.join(final_cipher)

    # Print or use the final cipher

    # binary cipher string to ascii
    final_cipher_ascii = binstring_to_sublist(final_cipher_str)
    # print("Decryption of Cipher :", final_cipher_ascii)

    return final_cipher_ascii
