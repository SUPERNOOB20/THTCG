def rgb_hex_to_fp(stripped_hexcode: str):
    r_16_string = stripped_hexcode[0] + stripped_hexcode[1]
    r_16 = int(r_16_string, 16)
    r_fp = r_16 / 255
    
    g_16_string = stripped_hexcode[2] + stripped_hexcode[3]
    g_16 = int(g_16_string, 16)
    g_fp = g_16 / 255
    
    b_16_string = stripped_hexcode[4] + stripped_hexcode[5]
    b_16 = int(b_16_string, 16)
    b_fp = b_16 / 255
    return (r_fp, g_fp, b_fp)


def rgba_hex_to_fp(rgba_hexcode: str):

    stripped_hexcode = rgba_hexcode.strip("#, ")

    if len(stripped_hexcode) == 6:
        return rgb_hex_to_fp (stripped_hexcode)
    
    elif len(stripped_hexcode) != 8:

        print("ERROR: invalid input.\n")
        print("Examples of valid inputs:\n")
        print('"a0f3bc"\n')
        print('"#a0f3bc"\n')
        print('"a0f3bcd3"\n')
        print('"#a0f3bc20"\n')

        return

    # You can safely assume len(stripped_hexcode) == 8 from here on :)

    rgb = rgb_hex_to_fp(stripped_hexcode)

    a_16_string = stripped_hexcode[6] + stripped_hexcode[7]
    a_16 = int(a_16_string, 16)
    a_fp = a_16 / 255

    return (rgb[0], rgb[1], rgb[2], a_fp)





print(str(rgba_hex_to_fp("#f4abffff")))