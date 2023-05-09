import scratchattach as scratch3
import os
import thumbnail

try:
  session = scratch3.login("ScratchAttachAccount", os.environ['PASSWORD'])

  project = session.connect_project("694515459")

  print(project.loves)
  print(project.favorites)
  print(project.views)

  project.set_title(f"❤️ {project.loves}  | ⭐ {project.favorites} | ◉ {project.views}")

  project.set_instructions(f"""This project updates every 5-15 minutes!

  Currently this project has...
  {project.views} project views!
  {project.loves} loves!
  {project.favorites} favorites!

  Thanks to TimMcCool for scratchattach!
  """)

  thumbnail.create_thumbnail(project.loves, project.favorites, project.views)

  project.set_thumbnail(file="thumbnail.png")
  
except Exception as e:
  print(e)
