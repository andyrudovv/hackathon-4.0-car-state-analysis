def save_uploaded_file(file):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())

def read_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()

def create_upload_directory():
    import os
    if not os.path.exists("uploads"):
        os.makedirs("uploads")