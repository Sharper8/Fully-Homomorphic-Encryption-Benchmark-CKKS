import tenseal as ts
import numpy as np
import time
import base64

# Dummy sensitive medical data (blood pressure readings)
sensitive_data = [120, 130, 125, 140, 115, 135]

def print_section(title):
    print(f"\n{'='*50}\n{title}\n{'='*50}")

def encrypt_data(data):
    context = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[60, 40, 40, 60]
    )
    context.global_scale = 2**40
    context.generate_galois_keys()
    return ts.ckks_vector(context, data), context

def encrypted_data_to_base64(encrypted_data):
    return base64.b64encode(encrypted_data.serialize()).decode('utf-8')

def base64_to_encrypted_data(base64_str, context):
    serialized_data = base64.b64decode(base64_str.encode('utf-8'))
    return ts.ckks_vector_from(context, serialized_data)

# Simulate the user side
def user_side():
    print_section("User Side: Encryption")
    print(f"Original sensitive data: {sensitive_data}")
    
    print("\nEncrypting the sensitive data...")
    encrypted_data, context = encrypt_data(sensitive_data)
    
    base64_encrypted = encrypted_data_to_base64(encrypted_data)
    print(f"\nEncrypted data (Base64, first 100 chars):\n{base64_encrypted[:100]}...")
    
    print("\nSending encrypted data to the server...")
    return base64_encrypted, context

# Simulate the server side
def server_side(base64_encrypted, context):
    print_section("Server Side: Computation on Encrypted Data")
    print(f"Received encrypted data (Base64, first 100 chars):\n{base64_encrypted[:100]}...")
    
    encrypted_data = base64_to_encrypted_data(base64_encrypted, context)
    
    print("\nPerforming computation (average) on encrypted data...")
    sum_vector = encrypted_data.sum()
    encrypted_result = sum_vector * (1.0 / len(sensitive_data))
    
    base64_result = encrypted_data_to_base64(encrypted_result)
    print(f"\nEncrypted result (Base64, first 100 chars):\n{base64_result[:100]}...")
    
    print("\nSending encrypted result back to the user...")
    return base64_result

# Simulate the entire process
def main():
    # User encrypts and sends data
    base64_encrypted, context = user_side()
    
    # Server processes encrypted data
    base64_result = server_side(base64_encrypted, context)
    
    print_section("User Side: Decryption and Verification")
    print(f"Received encrypted result (Base64, first 100 chars):\n{base64_result[:100]}...")
    
    # User decrypts the result
    print("\nDecrypting the result...")
    encrypted_result = base64_to_encrypted_data(base64_result, context)
    decrypted_result = encrypted_result.decrypt()[0]
    
    print(f"\nDecrypted result (average blood pressure): {decrypted_result:.2f}")
    print(f"Actual average (for comparison): {np.mean(sensitive_data):.2f}")
    
    print("\nVerifying the result:")
    print(f"  Original data: {sensitive_data}")
    print(f"  Sum of original data: {sum(sensitive_data)}")
    print(f"  Average of original data: {sum(sensitive_data) / len(sensitive_data):.2f}")

# Direct calculation function
def direct_calculation():
    return sum(sensitive_data) / len(sensitive_data)

# Benchmarking
def benchmark():
    print_section("Benchmarking")
    
    # FHE calculation
    start_time = time.time()
    main()
    fhe_time = time.time() - start_time
    print(f"\nFHE calculation time: {fhe_time:.6f} seconds")
    
    # Direct calculation
    start_time = time.time()
    result = direct_calculation()
    direct_time = time.time() - start_time
    print(f"Direct calculation time: {direct_time:.6f} seconds")
    print(f"Direct calculation result: {result:.2f}")
    
    if direct_time > 0:
        print(f"\nFHE is {fhe_time / direct_time:.2f} times slower than direct calculation")
    else:
        print("\nDirect calculation was too fast to measure accurately.")
        print(f"FHE took {fhe_time:.6f} seconds, while direct calculation took less than {direct_time:.6f} seconds.")

if __name__ == "__main__":
    benchmark()