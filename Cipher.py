# Caesar Cipher Functions

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-letters unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Just reverse the shift

# --- Main Program ---
print("=== Caesar Cipher ===")
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

message = input("Enter your message: ")
shift = int(input("Enter shift number (e.g., 3): "))

if choice == 'E':
    encrypted = encrypt(message, shift)
    print("Encrypted message:", encrypted)
elif choice == 'D':
    decrypted = decrypt(message, shift)
    print("Decrypted message:", decrypted)
else:
    print("Invalid choice.")
