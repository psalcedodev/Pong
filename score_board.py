from pygame import draw, Rect
from text import Text


class Indicator:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.c = color

    def setX(self, x):
        self.x = x

    def draw(self, surface):
        draw.rect(surface, self.c, (self.x, self.y, self.w, self.h))


class ScoreBoard:
    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mLeftScore = 0
        self.mLeftText = Text(str(self.mLeftScore), self.mX + 20, self.mY + 22)
        self.mLeftText.setColor((0, 89, 179))
        self.mRightScore = 0
        self.mRightText = Text(str(self.mRightScore),
                               self.mX + 60, self.mY + 22)
        self.mRightText.setColor((214, 26, 60))
        self.mServeStatus = 1
        self.mServeIndicator = Indicator(
            self.mX + 3, self.mY + 40, 15, 5, (0, 255, 43))

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getLeftScore(self):
        return self.mLeftScore

    def getRightScore(self):
        return self.mRightScore

    def getServeStatus(self):
        return self.mServeStatus

    def isGameOver(self):
        if self.mServeStatus > 2:
            return True
        else:
            return False

    def scoreLeft(self):
        if not self.isGameOver():
            self.mLeftScore += 1
            self.mLeftText.setText(str(self.mLeftScore))
            if self.mLeftScore == 9:
                self.mServeStatus = 3

    def scoreRight(self):
        if not self.isGameOver():
            self.mRightScore += 1
            self.mRightText.setText(str(self.mRightScore))
            if self.mRightScore == 9:
                self.mServeStatus = 4

    def swapServe(self):
        if not self.isGameOver():
            if self.mServeStatus == 1:
                self.mServeStatus = 2
                self.mServeIndicator.setX(self.mX + 53)
            else:
                self.mServeStatus = 1
                self.mServeIndicator.setX(self.mX + 13)

    def draw(self, surface):
        color = (70, 160, 126)
        rect = (self.mX, self.mY, self.mWidth, self.mHeight)
        draw.rect(surface, color, rect)
        self.mLeftText.draw(surface)
        self.mRightText.draw(surface)
        self.mServeIndicator.draw(surface)
