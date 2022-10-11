from threading import Thread
from Agent import Agent
import time
from server import app, AgentList

if __name__ == "__main__":
    app_t = Thread(target=app.run)
    app_t.daemon = True
    app_t.start()
    
    AgentList.append(Agent("Bob"))

    while True:
        time.sleep(0.1)
        for agent in AgentList:
            agent.update()