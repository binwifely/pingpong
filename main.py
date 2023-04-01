from pygame import*
window = display.set_mode((700, 500))

class Gameprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.y, self.rect.x))

class Player(Gameprite):
    def update_left():
        keys = key.get_pressed()

        if keys[K_w]:
            self.rect.y -= self.speed

        if keys[K_s]:
            self.rect.y += self.speed
    
    def update_right():
        keys = key.get_pressed()

        if keys[K_UP]:
            self.rect.y -= self.speed

        if keys[K_DOWN]:
            self.rect.y += self.speed

player1 = Player('wood.png', 20, 200, 50, 200, 5)
player2 = Player('wood.png', 500, 200, 50, 200, 5)
ball = Player('ball.png', 20, 200, 50, 200, 5)