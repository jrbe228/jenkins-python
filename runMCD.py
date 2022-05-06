import sys
import os
import comtypes.client as cc

# lenth of command line arguments
l = len(sys.argv)

# print usage help
def printHelp():
	print("usage: runMCD.exe pxczPath")
	print("argument: pxczPath        path to .pxcz file to run")

# verify that there is only one command line argument
if (l != 2):
	printHelp()
	print("Expect exactly one argument, found: " + str(l))
	sys.exit(0)

# path to workflow
p = sys.argv[1]

# verify that file extension is correct
if not p.endswith(".pxcz"):
	printHelp()
	print("Expected .pxcz file")
	print("Invalid file extension: " + p)
	sys.exit(0)

# verify that file exists
if not os.path.isfile(p):
	printHelp()
	print("File not found: " + p)
	sys.exit(0)

# get absolute path to workflow
p = os.path.abspath(p)
print("Path to .pxcz file:")
print(p)

# create ModelCenter Desktop COM object
print("Creating ModelCenter Application Object")
mcao = cc.CreateObject("ModelCenter.Application")

# load path to workflow
print("Loading Workflow")
mcao.loadModel(p)

# run workflow
print("Running Workflow")
mcao.run("")

# done !
print("Script Complete")
