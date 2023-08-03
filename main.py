
from fastapi import FastAPI, Query, HTTPException, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import zipfile
from generator import generate_organization
from items import peripherals, servers, services


def zip_files_in_directory(directory_path, extension):
    # Get a list of all files in the directory with the specified extension
    files = [file for file in os.listdir(directory_path) if file.endswith(extension)]

    # Create a zip file in memory
    zip_buffer = zipfile.ZipFile(f"{directory_path}.zip", "w", zipfile.ZIP_DEFLATED)

    # Add each file to the zip
    for file in files:
        zip_buffer.write(os.path.join(directory_path, file), file)

    # Close the zip buffer
    zip_buffer.close()

    return f"{directory_path}.zip"



app = FastAPI()



# Generate organization and return its report as JSON
@app.get('/generate_organization')
def generate_organization_api(
    num_buildings: int = Query(default=1, alias='num_buildings'),
    num_rooms: int = Query(default=3, alias='num_rooms'),
    seed: int = Query(default=0),
    is_json: bool = Query(default=False, alias='json')
):

    # Call generate_organization function with parameters
    org = generate_organization(num_buildings, num_rooms, peripherals, servers, services, seed)
    
    if is_json:
        report = org.generate_report_json()
        return {"organization_report": report}
    else:
        report = org.generate_report()
        return {"organization_report": report}

@app.get("/main.zip")
def zip_py_files():

    
    # Define the current directory
    current_directory = os.getcwd()

    # Define the file extension to filter
    file_extension = ".py"
        
    try:
        # Zip all py files in the current directory
        zip_file_path = zip_files_in_directory(current_directory, file_extension)

        # Return the zipped file as a download
        return FileResponse(zip_file_path, filename="project.zip")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error zipping files")


app.mount("/", StaticFiles(directory="docs"), name="docs")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=25422)