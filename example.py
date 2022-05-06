import os
import comtypes.client as cc

mcao = cc.CreateObject("ModelCenter.Application")
print("ModelCenter Application Object created")

# path to workflow
mcao.loadModel( os.path.abspath("example.pxcz") )
print("ModelCenter loaded example.pxcz")

# set variables
mcao.setValue("Model.variables.basic.in.b", True)
mcao.setValue("Model.variables.basic.in.i", 1)
mcao.setValue("Model.variables.basic.in.d", 2.2)
mcao.setValue("Model.variables.basic.in.s", "three")

mcao.setValue("Model.variables.array.in.b", "false, true")
mcao.setValue("Model.variables.array.in.i", "bounds[2,2] {1, 3, 2, 4}")
mcao.setValue("Model.variables.array.in.d", "bounds[3,2,2] {0, 0, 0.1, 0.01, 1, 10, 1.1, 10.01, 2, 20, 2.1, 20.01}")
mcao.setValue("Model.variables.array.in.s", '"orange", "maroon", "glow-in-the-dark"')

print("Running workflow")
# run workflow
mcao.run("")

# get variables
tval = mcao.getValue("Model.logger.t")
print(tval)

print("Getting basic variables")

print( mcao.getValue("Model.variables.basic.out.b") )
print( mcao.getValue("Model.variables.basic.out.i") )
print( mcao.getValue("Model.variables.basic.out.d") )
print( mcao.getValue("Model.variables.basic.out.s") )

print("Getting array variables")

print( mcao.getValue("Model.variables.array.out.b") )
print( mcao.getValue("Model.variables.array.out.i") )
print( mcao.getValue("Model.variables.array.out.d") )
print( mcao.getValue("Model.variables.array.out.s") )

