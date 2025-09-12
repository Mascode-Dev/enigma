-----

# Enigma Machine Simulator 🔐

A Python simulator of the famous Enigma cipher machine used during World War II. This project implements the double rotor rotation mechanism for message encryption and decryption.

## 🎯 Description

The Enigma machine was an electromechanical cipher device used to secure military and diplomatic communications. This simulator replicates its working principle with:

  - **Two configurable substitution rotors**
  - **Automatic rotor rotation mechanism**
  - **Bidirectional encryption/decryption**
  - **Space management** in messages

-----

## ✨ Features

### 🔒 Encryption/Decryption

  - **Simple encryption** with static rotors
  - **Enigma encryption** with automatic rotor rotation
  - **Decryption** to recover the original message
  - **Space preservation** in the text

### ⚙️ Rotor Mechanism

  - **Double rotation**: first rotor rotates with each character
  - **Cascade rotation**: second rotor rotates after the first completes a full turn
  - **Customizable rotor configuration**
  - **Random generation** of new rotors

-----

## 🔧 How It Works

### Enigma Encryption Principle

1.  **Step 1**: Find the letter's index in the alphabet.
2.  **Step 2**: Substitute it using the first rotor.
3.  **Step 3**: Find the index of the substituted letter.
4.  **Step 4**: Substitute it using the second rotor.
5.  **Step 5**: Rotate the rotors for the next character.

### Decryption Principle

1.  **Step 1**: Find the letter in the second rotor.
2.  **Step 2**: Get its position in the alphabet.
3.  **Step 3**: Find that letter in the first rotor.
4.  **Step 4**: Get the original letter from the alphabet.

### Rotation Mechanism

```
Rotor 1: Rotates with each character
Rotor 2: Rotates after 26 rotations of Rotor 1
```

-----

## 📖 Usage

### Module Import

```python
from enigma_simulator import *
```

### Main Functions

#### 1\. Generate Random Rotors

```python
rotor1 = shuffle_alphabet()
rotor2 = shuffle_alphabet()
```

#### 2\. Simple Encryption (Static Rotors)

```python
code(rotor1, rotor2, "your message")
```

#### 3\. Decryption

```python
decode(rotor1, rotor2, "encrypted message")
```

#### 4\. Enigma Encryption (With Rotation)

```python
encrypted_message = code_enigma(rotor1, rotor2, "your message")
```

#### 5\. Manual Rotor Rotation

```python
new_rotor = rotation(current_rotor)
```

-----

## 💡 Examples

### Basic Example

```python
# Demo rotors
rotor1 = ['f', 'g', 'r', 'o', 'w', 'd', 'c', 'i', 'y', 't', 'p', 'z', 'u', 'a', 'h', 'm', 'l', 'q', 's', 'j', 'b', 'x', 'k', 'n', 'v', 'e']
rotor2 = ['u', 'i', 'f', 'e', 'w', 'x', 'z', 't', 'n', 'j', 'q', 'a', 'm', 's', 'h', 'c', 'l', 'o', 'v', 'd', 'b', 'y', 'g', 'k', 'p', 'r']

# Encryption
print("Original message: je suis en classe de nsi")
code(rotor1, rotor2, "je suis en classe de nsi")
# Output: "dg vipv gu orxvvg hg uvp"

# Decryption
print("Encrypted message: dg vipv gu orxvvg hg uvp")
decode(rotor1, rotor2, "dg vipv gu orxvvg hg uvp")
# Output: "je suis en classe de nsi"
```

-----

## 🔍 Technical Details

### Character Handling

  - **Lowercase letters**: a-z supported
  - **Spaces**: preserved in the message
  - **Other characters**: not supported in this version

### Rotation Mechanism

  - **Simple rotation**: shifts one position to the right
  - **Cascade rotation**: the second rotor turns after 26 rotations of the first
  - **Rotor state**: modified during Enigma encryption

### Performance

  - **Time complexity**: O(n×m) where n = message length, m = alphabet size
  - **Space complexity**: O(m) for the rotors

-----

## ⚠️ Limitations

### Supported Characters

  - Only lowercase letters (a-z)
  - Accents and special characters are not handled
  - Case is not preserved

### Security

  - Rotors are generated with `random()` (not cryptographically secure)
  - No user input validation
  - Rotor configuration is visible in plain text

### Missing Features

  - No plugboard
  - A single implicit reflector
  - No initial rotor position configuration

-----

## 🤝 Contributing

1.  **Fork** the project
2.  **Create a feature branch** (`git checkout -b feature/improvement`)
3.  **Commit** your changes (`git commit -m 'Add new feature'`)
4.  **Push** to the branch (`git push origin feature/improvement`)
5.  **Open a Pull Request**

### Areas for Contribution

  - User interface improvements
  - Performance optimization
  - Adding unit tests
  - Documentation and examples
  - Supporting new characters
  - Historically accurate features

-----

## 📝 License

This project is developed for educational purposes to understand the principles of historical cryptography.

-----

## 👨‍💻 Author

Project developed for learning about cryptography and historical computing.

-----

**Educational Note**: This simulator is a simplification of the historical Enigma machine, designed to illustrate the basic concepts of substitution cipher with a mechanical rotation.
