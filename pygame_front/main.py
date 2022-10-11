from urllib import response
import pygame
import requests
import json

SCREENSIZE = WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)  # the color black
WHITE = (255, 255, 255)  # the color white
GREY = (169, 169, 169)  # the color grey
GREEN = (66, 245, 99)

_VARS = {}

cx, cy = 400, 400
sz = 5

gx, gy = 0, 0

def spam_guesses():
    rng = 2
    for x in range(-rng, rng+1):
        for y in range(-rng, rng+1):
            response_API = requests.get(f"http://localhost:5000/query_chunk?x={x}&y={y}")
            if response_API.status_code == 200 and json.loads(response_API.text)['loaded']:
                return x, y

    return None

if __name__ == "__main__":
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Nocom')

    

    while True:
        clock.tick(20)

        # Actual position
        response_API = requests.get("http://localhost:5000/actual_location")
        if response_API.status_code == 200:
            dict = json.loads(response_API.text)
        
        _VARS['surf'].fill(WHITE)
        pygame.draw.circle(_VARS['surf'], BLACK, (cx + dict['Bob'][0] * sz, cy + dict['Bob'][1] * sz), sz, sz)

        ans = spam_guesses()
        print(ans)
        #ans = None

        # spamming guesses
        if ans:
            pygame.draw.circle(_VARS['surf'], GREEN, (cx + ans[0] * sz, cy + ans[1] * sz), sz, sz)

        pygame.display.update()