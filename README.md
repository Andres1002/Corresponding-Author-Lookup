# Corresponding-Author-Lookup

## Function

The function of this program is to parse publishing data for Iowa State University from Web of Science and Dimensions and return respective DOI, publisher, journal title, and Corresponding author information. Corresponding author information may include items such as:

* Full name
* Faculty or student classification
* Professional title
* Department or major


## Flowchart
![Flowchart](https://github.com/Andres1002/Corresponding-Author-Lookup/blob/main/Assets/Block%20Diagram%20for%20CA%20Lookup-cropped.svg)

## Input and Output Formats
### Input

The input that CAlookup.py requires can be obtained by exporting data from Web of Science and Dimensions. Once acquired, place the input files in the same directory as CALookup.py and update the path in the code located in line 195 til line 222. The program will start running and once completed the program will notify you if further action is needed. For error messages such as "Error: Input College Data for: " you will need to update the dictionary libraries. Currently, the code does not know which library needs to be updated but this can be mitigated by knowing what needs to be expanded. First try to add the missing entry into the department dictionary and rerun the program.

Note: some inputs required for the dictionary have a tab space before the name. Please input everything just before "Error: Input College Data for: " (space included).

### Output

The output is stored in Output/Masterlist.csv

The output data can be analyzed straight from the excel spread sheet but I have created a website that lets you just drop the file in and see relevant Pi charts from the data.

Website: [Click Here for Streamlit Website](https://andres1002-corresponding-author-lookup-commander-rbbd3j.streamlit.app/)
