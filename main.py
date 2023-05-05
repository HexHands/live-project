import scratchattach as scratch3
import os

session = scratch3.login("ScratchAttachAccount", os.environ['PASSWORD'])

project = session.connect_project("694515459")

print(project.views)
print(project.loves)
print(project.favorites)

project.set_title(f"❤️ {project.loves}  | ⭐ {project.favorites} | ◉ {project.views}")

project.set_instructions(f"""This project updates every 5-10 minutes!

Currently this project has...
{project.views} project views!
{project.loves} loves!
{project.favorites} favorites!

Thanks to TimMcCool for scratchattach!
""")
