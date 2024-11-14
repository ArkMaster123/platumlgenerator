from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from plantuml import PlantUML

app = FastAPI()

class PlantUMLRequest(BaseModel):
    script: str

# Initialize the PlantUML server URL
plantuml_server = PlantUML(url="http://www.plantuml.com/plantuml/png/")

@app.post("/generate-image/")
async def generate_image(request: PlantUMLRequest):
    try:
        # Use the `processes` function to get the raw PNG data
        image_data = plantuml_server.processes(request.script)
        return Response(content=image_data, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
