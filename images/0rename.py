import os

# Rename XML to include -1 at end.
wd = os.getcwd()

def xml() :
    for filename in os.listdir(wd):

        if (filename.endswith(".xml")):
            string = filename.split(".xml")[0] + "-1" + ".xml"
            os.rename(os.path.join(wd, filename), os.path.join(wd, string))
            print("renamed to " + str(string))
        

# Rename PNG to remove .1 and replace with -1
def png() :
    for filename in os.listdir(wd):
        if (filename.endswith(".png")):
            string = filename.split(".1.png")[0] + "-1" + ".png"
            os.rename(os.path.join(wd, filename), os.path.join(wd, string))
            print("renamed to " + str(string))



# Run selected method:
png()