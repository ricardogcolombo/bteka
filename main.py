from src.server.instance import server
#  from src.resources import *
#  import logging
#  import os
#  import sys

# Need to import all resources
# so that they register with the server
app = server.app
if __name__ == '__main__':
    app.run(debug=True)
