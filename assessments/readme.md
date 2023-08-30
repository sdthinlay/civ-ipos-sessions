# About

Contains information related to assessments. Please see Blackboard for the latest info.

## Next Assessment

KBA related to binary file handling and data structures. 

Preview question: 

Consider the following fictional image file format (`.RIF`):
- File Structure: A binary file containing image data.
- First 9 bytes: Text encoded with the image's dimensions (e.g., "1920x1080").
- Following bytes: Series of 3 bytes representing RGB values of each of the pixels.
> E.g. `1920x1080200244002`


Given the specification, outline how you would use seek, read, write, and tell (as appropriate) to:
a. Retrieve the RGB Value of the Center Pixel
b. Retrieve all pixel values as integers from a random 100x100 grid within the image
c. Reduce the resolution by half

> NOTE: While you don't need to create a `.rif` parser to finish the exercise, a rif file creator has been added for illustrative purposes.

