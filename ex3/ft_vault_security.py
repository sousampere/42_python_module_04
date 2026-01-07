#!/usr/bin/python


class SecureOpen:
    def __enter__(self, file: str, flag: str):
        print("[SECURE OPEN] Opening file...")
        try:
            self.file = open()
        except Exception as e:
            raise Exception(f"Error while opening file: {e}")
        return (self.file)
    
    def write(self, data):
        try:
            return (self.file.write(data))
        except Exception as e:
            raise Exception(f"Error while writing: {e}")

    def __exit__(self):
        try:
            return (self.file.close())
        except:
            