#So the first appis the name of the package (which is a folder with a __init__.py file inside)
# and the second is the name of the imported object from that package. 
from app import app
  
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)