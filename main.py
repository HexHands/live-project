import scratchattach as scratch3
import os

session = scratch3.login("ScratchAttachAccount", os.environ['PASSWORD'])

project = session.connect_project("694515459")

print(project.views)
print(project.loves)
print(project.favorites)

project.set_title(f"◉{project.views} | ❤️{project.loves}  | ⭐{project.favorites}")
