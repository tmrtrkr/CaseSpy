from flask import Flask
import threading
import UI  
from flask_cors import CORS
import logging
from flask import Flask, redirect


app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)

# Create a global reference that can be accessed across functions
gui_instance = None

def launch_gui():
    global gui_instance
    logging.info("Launching GUI...")
    gui_instance = UI.CustomGUI()  # Assign to the global instance
    gui_instance.run()
    logging.info("GUI launched.")

@app.route('/')
def home():
    return redirect('/start-gui')



@app.route('/start-gui')
def start_gui():
    if not gui_instance:
        threading.Thread(target=launch_gui).start()
        return "GUI is starting..."
    else:
        return "GUI already running."

@app.route('/trigger-sendToApi')  # Fixed missing route decorator
def trigger_sendToApi():
    if gui_instance:
        gui_instance.sendToApi()  # Ensure gui_instance is accessible
        return "sendToApi triggered"
    else:
        return "Something went wrong trigger-sendtoapi"
    


@app.route('/take-shot1')
def takeShot1():
    if gui_instance:
        gui_instance.sendScreenShotData1()
        return "screenshot1 taken as shot1.png"
    
    else:
        return "Something went wrong take-shot1"
    


@app.route('/take-shot2')
def takeShot2():
    if gui_instance:
        gui_instance.sendScreenShotData2()
        return "screenshot2 taken as shot2.png"
    
    else:
        return "Something went wrong take-shot2"
    



if __name__ == '__main__':
    app.run(debug=True, port=5000)







