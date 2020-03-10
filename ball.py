from random import uniform
from pygame import draw


class Ball:
    def __init__(self, size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
        self.mX = min_x
        self.mY = min_y
        self.mSize = size
        self.mDX = 0
        self.mDY = 0
        self.mMinX = min_x
        self.mMaxX = max_x
        self.mMinY = min_y
        self.mMaxY = max_y
        self.mLeftPaddleX = left_paddle_x
        self.mLeftPaddleMinY = min_y
        self.mLeftPaddleMaxY = max_y
        self.mRightPaddleX = right_paddle_x
        self.mRightPaddleMinY = min_y
        self.mRightPaddleMaxY = max_y
        self.mWallRight = self.mMaxX - self.mSize
        self.mWallBottom = self.mMaxY - self.mSize

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getSize(self):
        return self.mSize

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY

    def getMinX(self):
        return self.mMinX

    def getMaxX(self):
        return self.mMaxX

    def getMinY(self):
        return self.mMinY

    def getMaxY(self):
        return self.mMaxY

    def getLeftPaddleX(self):
        return self.mLeftPaddleX

    def getLeftPaddleMinY(self):
        return self.mLeftPaddleMinY

    def getLeftPaddleMaxY(self):
        return self.mLeftPaddleMaxY

    def getRightPaddleX(self):
        return self.mRightPaddleX

    def getRightPaddleMinY(self):
        return self.mRightPaddleMinY

    def getRightPaddleMaxY(self):
        return self.mRightPaddleMaxY

    def setPosition(self, x, y):
        if self.mMinX < x and x + self.mSize < self.mMaxX:
            if self.mMinY < y and y + self.mSize < self.mMaxY:
                self.mX = x
                self.mY = y

    def setSpeed(self, dx, dy):
        self.mDX = dx
        self.mDY = dy

    def setLeftPaddleY(self, paddle_min_y, paddle_max_y):
        if paddle_max_y > paddle_min_y >= self.mMinY:
            if paddle_max_y <= self.mMaxY:
                self.mLeftPaddleMinY = paddle_min_y
                self.mLeftPaddleMaxY = paddle_max_y

    def setRightPaddleY(self, paddle_min_y, paddle_max_y):
        if paddle_max_y > paddle_min_y >= self.mMinY:
            if paddle_max_y <= self.mMaxY:
                self.mRightPaddleMinY = paddle_min_y
                self.mRightPaddleMaxY = paddle_max_y

    def checkTop(self, new_y):
        if new_y >= self.mMinY:
            return new_y
        else:
            self.mDY *= -1
            diff = self.mMinY - new_y
            act_y = self.mMinY + diff
            return act_y

    def checkBottom(self, new_y):
        if new_y <= self.mWallBottom:
            return new_y
        else:
            self.mDY *= -1
            diff = new_y - self.mWallBottom
            act_y = self.mWallBottom - diff
            return act_y

    def checkLeft(self, new_x):
        if new_x >= self.mMinX:
            return new_x
        else:
            self.setSpeed(0, 0)
            act_x = self.mMinX
            return act_x

    def checkRight(self, new_x):
        if new_x <= self.mWallRight:
            return new_x
        else:
            self.setSpeed(0, 0)
            act_x = self.mMaxX - self.mSize
            return act_x

    def checkLeftPaddle(self, new_x, new_y):
        mid_y = (self.mY + new_y) / 2
        if self.mLeftPaddleMinY <= mid_y <= self.mLeftPaddleMaxY and new_x <= self.mLeftPaddleX <= self.mX:
            self.mDX *= -1
            diff = self.mLeftPaddleX - new_x
            act_x = self.mLeftPaddleX + diff
            return act_x
        else:
            return new_x

    def checkRightPaddle(self, new_x, new_y):
        mid_y = (self.mY + new_y) / 2
        if self.mRightPaddleMinY <= mid_y <= self.mRightPaddleMaxY and (new_x + self.mSize) >= self.mRightPaddleX >= self.mX:
            self.mDX *= -1
            diff = new_x + self.mSize - self.mRightPaddleX
            act_x = self.mRightPaddleX - diff - self.mSize
            return act_x
        else:
            return new_x

    def move(self, dt):
        new_x = self.mX + self.mDX * dt
        new_y = self.mY + self.mDY * dt

        new_y = self.checkTop(new_y)
        new_y = self.checkBottom(new_y)

        new_x = self.checkLeft(new_x)
        new_x = self.checkRight(new_x)

        new_x = self.checkLeftPaddle(new_x, new_y)
        new_x = self.checkRightPaddle(new_x, new_y)

        self.mX = new_x
        self.mY = new_y

    def serveLeft(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        self.mX = x
        self.mY = uniform(min_y, max_y)
        self.mDX = uniform(min_dx, max_dx)
        self.mDY = uniform(min_dy, max_dy)

    def serveRight(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        self.mX = x
        self.mY = uniform(min_y, max_y)
        self.mDX = uniform(-min_dx, -max_dx)
        self.mDY = uniform(min_dy, max_dy)

    def draw(self, surface):
        color = (255, 255, 255)
        rect = (self.mX, self.mY, self.mSize, self.mSize)
        draw.rect(surface, color, rect)
