from pygame import draw


class Paddle:
    def __init__(self, x, y, width, height, speed, min_y, max_y):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mSpeed = speed
        self.mMinY = min_y
        self.mMaxY = max_y
        self.mColor = (255, 255, 255)

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getRightX(self):
        return self.mX + self.mWidth

    def getBottomY(self):
        return self.mY + self.mHeight

    def getSpeed(self):
        return self.mSpeed

    def getMaxY(self):
        return self.mMaxY

    def getMinY(self):
        return self.mMinY

    def setPosition(self, y):
        if y >= self.mMinY and y + self.mHeight <= self.mMaxY:
            self.mY = y

    def setColor(self, color):
        self.mColor = color

    def moveUp(self, dt):
        self.mY -= self.mSpeed * dt
        if self.mY < self.mMinY:
            self.mY = self.mMinY

    def moveDown(self, dt):
        self.mY += self.mSpeed * dt
        if self.mY + self.mHeight > self.mMaxY:
            self.mY = self.mMaxY - self.mHeight

    def draw(self, surface):
        rect = (self.mX, self.mY, self.mWidth, self.mHeight)
        draw.rect(surface, self.mColor, rect)
