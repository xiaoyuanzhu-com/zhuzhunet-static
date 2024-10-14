import os
import random
import string

def generate_random_filename(file_suffix, length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) + file_suffix

def generate_random_content(size_in_bytes):
    return os.urandom(size_in_bytes)

def create_random_files(num_files, size_in_bytes, file_suffix):
    for _ in range(num_files):
        filename = generate_random_filename(file_suffix, length=8)
        content = generate_random_content(size_in_bytes)
        with open(filename, 'wb') as f:
            f.write(content)
        print(f"Created file: {filename}")

create_random_files(1, 1, ".1b.bin")
create_random_files(10, 1 * 1024, ".1kib.bin")
create_random_files(10, 1 * 1024 * 1024, ".1mib.bin")
create_random_files(10, 1 * 1024 * 1024 * 10, ".10mib.bin")
