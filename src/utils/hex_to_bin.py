from src.constants import HEX_TO_BIN

def hex_to_bin(hex_str:str):
    bin_str = ''
    for ch in hex_str:
        bin_str+= HEX_TO_BIN[ch]
    
    return bin_str