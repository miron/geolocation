from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/gps/")
def handle_gps_data(latitude: float = Body(...), longitude: float = Body(...)):
    # Do something with the location data
    return {"latitude": latitude, "longitude": longitude}
