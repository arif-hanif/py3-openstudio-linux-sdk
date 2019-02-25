import py3_openstudio_linux_sdk as openstudio

model = openstudio.model.Model()
space = openstudio.model.Space(model)
space.setName("New Space")

for s in openstudio.model.getSpaces(model):
    print(s)
