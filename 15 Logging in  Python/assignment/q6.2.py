### Assignment 6: Contextual Logging

### 2. Modify the function to include additional contextual information (e.g., user ID, session ID).
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(user_id)s- %(session_id)s- %(message)s",
    filename="logs/q6 app.log",
    filemode="a"
)

class User:
    def __init__(self,id,name):
        self.user_id=id
        self.name=name
        self.session=0
    

    def new_session(self):
        print(f"Welcome to the new session {self.name}")
        self.session+=1
        logging.debug(f'Welcome {self.name}',extra={'user_id':self.user_id,'session_id':self.session})

user=User('CG25PBFDEL','Pradyumn')
user.new_session()
user.new_session()
