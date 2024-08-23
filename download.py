

from roboflow import Roboflow
rf = Roboflow(api_key="lLvyCwgR99azQkLqmSYm")
project = rf.workspace("-jwzpw").project("continuous_fire")
version = project.version(6)
dataset = version.download("tensorflow")
