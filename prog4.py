# 1
def speed_camera(time_seconds):
    distance_meters = 100
    speed_kmh = (distance_meters / time_seconds) * (3600/1000)  # Convert m/s to km/h
    return speed_kmh

result = speed_camera(4.0)
print("{:.1f}".format(result))

# 2
def check_string(input_string):
    has_lower = any(char.islower() for char in input_string)
    has_upper = any(char.isupper() for char in input_string)
    return has_lower and has_upper

input_str = "Nirvana"
result = check_string(input_str)
print(result)

print(check_string("nirvana"))
print(check_string("OASIS"))

# 3

def encrypt_message():
    plaintext = input("Enter the message you want to encrypt: ")
    encrypted_message = [str(i + ord(char)) for i, char in enumerate(plaintext)]
    print("Encrypted:", " ".join(encrypted_message))
    return encrypted_message

# 4
def decrypt_message(encrypted_message):
    decrypted_chars = [chr(int(char) - i) for i, char in enumerate(encrypted_message)]
    decrypted_message = "".join(decrypted_chars)
    print("Decrypted:", decrypted_message)

encrypted_msg = encrypt_message()
decrypt_message(encrypted_msg)

