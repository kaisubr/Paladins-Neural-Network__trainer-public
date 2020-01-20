import os

# If no XML is found for the associated PNG, then the PNG is moved into the noxml directory.
wd = os.getcwd()
m = 0

for filename in os.listdir(wd):

    if (filename.endswith(".png")):
        string = filename.split(".png")[0]
        if (os.path.exists( os.path.join(wd, string + '.xml') ) == False):
            print("No " + string + ".xml found,\tmoving png to noxml/")
            os.rename(os.path.join(wd, filename), (wd + "/noxml/" + filename))
            m += 1

print("Moved " + str(m) + " files")