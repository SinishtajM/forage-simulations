'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile, BadZipFile
import sys

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except RuntimeError:
        return False
    except BadZipFile:
        print("[!] Bad ZIP file format")
        sys.exit(1)

def main():
    print("[+] Beginning bruteforce on enc.zip using rockyou.txt")
    try:
        with ZipFile('enc.zip') as zf:
            with open('rockyou.txt', 'rb') as f:
                for line in f:
                    password = line.strip()
                    if attempt_extract(zf, password):
                        print(f"[+] Success! Password found: {password.decode('utf-8')}")
                        return
                    else:
                        print(f"[-] Incorrect Password: {password.decode('utf-8')}")
    except FileNotFoundError:
        print("[!] 'enc.zip' or 'rockyou.txt' not found. Make sure they are in the same directory.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        
    print("[+] Password not found in list")
    
if __name__ == "__main__":
    main()