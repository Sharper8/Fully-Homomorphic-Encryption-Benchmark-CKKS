# Fully Homomorphic Encryption (FHE) Example using CKKS Scheme

This project demonstrates a basic implementation of Fully Homomorphic Encryption (FHE) using the CKKS (Cheon-Kim-Kim-Song) scheme, as implemented in the TenSEAL library. The example showcases how to perform computations on encrypted data, specifically calculating the average of a list of numbers (simulating blood pressure readings) without decrypting the data.

## Overview

Fully Homomorphic Encryption allows computations to be performed on encrypted data without decrypting it first. This is particularly useful in scenarios where data privacy is crucial, such as in healthcare or financial services.

In this example, we use the CKKS scheme, which is designed for approximate arithmetic on encrypted real or complex numbers. It's well-suited for applications that can tolerate small approximation errors, like many machine learning and statistical computations.

## Key Components

1. **TenSEAL Library**: We use the TenSEAL library, which provides a Python API for the Microsoft SEAL homomorphic encryption library. TenSEAL implements the CKKS scheme among others.

2. **CKKS Scheme**: This scheme allows for approximate arithmetic on encrypted real numbers. It's suitable for our use case of calculating averages.

3. **Encryption Parameters**: 
   - Polynomial modulus degree: 8192
   - Coefficient modulus bit sizes: [60, 40, 40, 60]
   - Global scale: 2^40

## Code Structure

The code is structured to simulate a scenario where:

1. A user (client) has sensitive data they want to process.
2. The data is encrypted on the client side.
3. The encrypted data is sent to a server.
4. The server performs computations on the encrypted data.
5. The result is sent back to the client.
6. The client decrypts the result.

## Key Functions

- `encrypt_data()`: Encrypts the input data using the CKKS scheme.
- `encrypted_data_to_base64()` and `base64_to_encrypted_data()`: Convert encrypted data to and from Base64 encoding for easy transmission and display.
- `user_side()`: Simulates the client-side operations (encryption).
- `server_side()`: Simulates the server-side operations (computation on encrypted data).
- `main()`: Orchestrates the entire process.
- `benchmark()`: Compares the performance of FHE with direct calculation.

## Running the Example

1. Ensure you have Python installed (3.7 or later recommended).
2. Install the required libraries:
   ```
   pip install tenseal numpy
   ```
3. Run the script:
   ```
   python fhe_example.py
   ```

## Output Explanation

The script will output:

1. The original sensitive data.
2. Base64 representations of the encrypted data at various stages.
3. The decrypted result and verification against the actual average.
4. Timing comparisons between FHE and direct calculation.

## Educational Value

This example demonstrates:

1. How data can be encrypted using FHE (specifically the CKKS scheme).
2. How computations can be performed on encrypted data.
3. The accuracy of FHE computations compared to direct calculations.
4. The performance trade-offs of using FHE (significantly slower but provides data privacy).

## Limitations and Considerations

1. This is a simplified example. Real-world applications would require more robust error handling and security measures.
2. The CKKS scheme provides approximate results, which is suitable for many statistical and machine learning applications but may not be appropriate for all use cases.
3. The performance difference between FHE and direct calculation is significant. In practice, FHE is used when data privacy outweighs performance considerations.

## Further Learning

To deepen your understanding of FHE and the CKKS scheme:

1. Explore the [TenSEAL documentation](https://github.com/OpenMined/TenSEAL)
2. Read about the [CKKS scheme](https://eprint.iacr.org/2016/421.pdf)
3. Investigate other FHE libraries and schemes (e.g., TFHE, BGV)

Remember, FHE is a powerful tool for preserving privacy in computations, but it comes with its own set of challenges and considerations. Always consider the specific requirements of your application when deciding to use FHE.