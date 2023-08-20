'''Revision on reading and writing text files in Python 
With a twist: what happens when we use multi-byte characters?
How do we move backwards in the file?'''

# Create the file we will work with, try:
# remove encoding and see what happens
# remove encoding and the emojis and see what happens
# NOTE: the behaviour here is different on Windows and non-Windows platforms!
with open("my_new_file", "w", encoding='utf-8') as f:
    f.write("Hello😊😊\nWorld")

# Ditto: try removing encoding and see what happens    
with open("my_new_file", "r", encoding='utf-8') as f:
    print(f.read()) # prints the content
    print(f.read()) # prints nothing, why?
    # move the cursor back to the beginning of the file
    f.seek(0)
    print(f.read()) # prints the content again
    f.seek(0)
    for _ in range(5):
        print(f.read(1)) # prints the first 5 characters
    print(f.tell()) # tells us where the cursor is
    print(f.read(1)) # prints the emoji
    print(f.tell()) # tells us where the cursor is - WHAT? Notice where the cursor is, it jumped 4 bytes!  # noqa: E501
    # if you have removed the encoding, see what happens here and continue reading - notice no emoji just 4 random characters # noqa: E501
