# Problem: Simulated File System

# Description:
# Implement a simple file system that supports basic commands similar to those in Linux. The file system should have the following functionalities:

# mkdir(dirname: string):

# Create a new directory within the current working directory.
# If a directory with the same name already exists, print (or return) a message indicating that the directory already exists.
# pwd():

# Return the path of the current working directory.
# The root directory should be represented as /.
# For other directories, display the full path (e.g., /example/path/).
# cd(path: string):

# Change the current working directory.
# If the given path starts with /, treat it as an absolute path; otherwise, treat it as relative to the current working directory.
# The path can include the special directories . (current directory) and .. (parent directory).
# Input Format:

# The file system starts at the root directory (/).
# The commands will be provided in the order they are executed.
# Output Format:

# The output should be the return values or messages from the commands, such as the output from pwd() or error messages for invalid operations.
# Examples:

# Example 1:
# Commands:
# scss
# Copy
# Edit
# mkdir("a")
# mkdir("b")
# pwd()       # Expected output: "/"
# cd("a")
# pwd()       # Expected output: "/a/"
# cd("..")
# pwd()       # Expected output: "/"
# cd("/b")
# pwd()       # Expected output: "/b/"
# Example 2:
# Commands:
# scss
# Copy
# Edit
# mkdir("docs")
# cd("docs")
# mkdir("projects")
# cd("projects")
# pwd()       # Expected output: "/docs/projects/"

class FileSystem:
    def __init__(self):
        # TODO: Initialize the file system with a root directory and set the current directory to root.
        pass

    def mkdir(self, dirname: str):
        # TODO: Create a new directory in the current working directory.
        # If the directory already exists, print a message indicating so.
        pass

    def cd(self, path: str):
        # TODO: Change the current working directory.
        # If path starts with '/', treat it as an absolute path.
        # Support the special entries '.' (current directory) and '..' (parent directory).
        pass

    def pwd(self) -> str:
        # TODO: Return the current working directory as a string.
        # Return "/" if at root, otherwise something like "/dir1/dir2/".
        pass

def run_tests():
    fs = FileSystem()
    
    # Test 1: Create directories in the root and check pwd
    fs.mkdir("a")
    fs.mkdir("b")
    # pwd should return "/"
    print("Test 1:", "Pass" if fs.pwd() == "/" else f"Fail (Expected: /, Got: {fs.pwd()})")
    
    # Test 2: Change directory to "a" and verify pwd
    fs.cd("a")
    print("Test 2:", "Pass" if fs.pwd() == "/a/" else f"Fail (Expected: /a/, Got: {fs.pwd()})")
    
    # Test 3: Change back to parent directory using ".."
    fs.cd("..")
    print("Test 3:", "Pass" if fs.pwd() == "/" else f"Fail (Expected: /, Got: {fs.pwd()})")
    
    # Test 4: Change directory using an absolute path
    fs.cd("/b")
    print("Test 4:", "Pass" if fs.pwd() == "/b/" else f"Fail (Expected: /b/, Got: {fs.pwd()})")

if __name__ == '__main__':
    run_tests()
