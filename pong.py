import pygame
import ball
import wall
import paddle
import score_board

LEFT = 1
RIGHT = 2
LEFT_WIN = 3
RIGHT_WIN = 4


class Pong:

    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height

        score_width = 80
        score_height = 40
        score_x = self.mWidth / 2 - score_width / 2
        score_y = 40
        self.mScoreBoard = score_board.ScoreBoard(
            score_x, score_y, score_width, score_height)

        wall_size = 10
        self.mLeftWall = wall.Wall(0, 0, wall_size, self.mHeight)
        self.mRightWall = wall.Wall(
            self.mWidth-wall_size, 0, wall_size, self.mHeight)
        self.mTopWall = wall.Wall(0, 0, self.mWidth, wall_size)
        self.mBottomWall = wall.Wall(
            0, self.mHeight-wall_size, self.mWidth, wall_size)

        paddle_margin = 20
        paddle_width = 20
        paddle_height = 100
        paddle_speed = self.mHeight / 1.25
        self.mLeftPaddle = paddle.Paddle(self.mLeftWall.getRightX() + paddle_margin,
                                         self.mHeight / 2 - paddle_height / 2,
                                         paddle_width, paddle_height,
                                         paddle_speed,
                                         self.mTopWall.getBottomY(),
                                         self.mBottomWall.getY())
        self.mLeftPaddle.setColor((	0, 89, 179))

        self.mRightPaddle = paddle.Paddle(self.mRightWall.getX() - paddle_margin - paddle_width,
                                          self.mHeight / 2 - paddle_height / 2,
                                          paddle_width, paddle_height,
                                          paddle_speed,
                                          self.mTopWall.getBottomY(),
                                          self.mBottomWall.getY())
        self.mRightPaddle.setColor((196, 2, 51))

        size = 20
        self.mBall = ball.Ball(size,
                               self.mLeftWall.getRightX(),
                               self.mRightWall.getX(),
                               self.mTopWall.getBottomY(),
                               self.mBottomWall.getY(),
                               self.mLeftPaddle.getRightX(),
                               self.mRightPaddle.getX())
        self.serveBall()

        self.mBall.setLeftPaddleY(
            self.mLeftPaddle.getY(), self.mLeftPaddle.getBottomY())
        self.mBall.setRightPaddleY(
            self.mRightPaddle.getY(), self.mRightPaddle.getBottomY())

        return

    def serveBall(self):
        min_dx = self.mWidth / 2.0
        max_dx = self.mWidth / 1.5
        max_dy = self.mHeight / 1.0
        min_dy = -max_dy
        if self.mScoreBoard.getServeStatus() == LEFT:
            self.mBall.serveLeft(self.mLeftPaddle.getRightX() + self.mBall.getSize(),
                                 self.mLeftPaddle.getY(),
                                 self.mLeftPaddle.getBottomY(),
                                 min_dx, max_dx, min_dy, max_dy)
            self.mScoreBoard.swapServe()
            self.mBallMoving = True
        elif self.mScoreBoard.getServeStatus() == RIGHT:
            self.mBall.serveRight(self.mRightPaddle.getX() - self.mBall.getSize(),
                                  self.mRightPaddle.getY(),
                                  self.mRightPaddle.getBottomY(),
                                  min_dx, max_dx, min_dy, max_dy)
            self.mScoreBoard.swapServe()
            self.mBallMoving = True
        return

    def update(self, dt, keys):

        if self.mBall.getDX() != 0:
            self.mBall.move(dt)

            if pygame.K_w in keys:
                self.mLeftPaddle.moveUp(dt)
                self.mBall.setLeftPaddleY(
                    self.mLeftPaddle.getY(), self.mLeftPaddle.getBottomY())
            elif pygame.K_s in keys:
                self.mLeftPaddle.moveDown(dt)
                self.mBall.setLeftPaddleY(
                    self.mLeftPaddle.getY(), self.mLeftPaddle.getBottomY())

            if pygame.K_UP in keys:
                self.mRightPaddle.moveUp(dt)
                self.mBall.setRightPaddleY(
                    self.mRightPaddle.getY(), self.mRightPaddle.getBottomY())
            elif pygame.K_DOWN in keys:
                self.mRightPaddle.moveDown(dt)
                self.mBall.setRightPaddleY(
                    self.mRightPaddle.getY(), self.mRightPaddle.getBottomY())

        else:
            if self.mBallMoving:
                self.mBallMoving = False
                if self.mBall.getX() < self.mWidth / 2:
                    self.mScoreBoard.scoreRight()
                else:
                    self.mScoreBoard.scoreLeft()

            if((self.mScoreBoard.getServeStatus() == LEFT and
                pygame.K_d in keys) or
                (self.mScoreBoard.getServeStatus() == RIGHT and
                 pygame.K_LEFT in keys)):
                self.serveBall()

        return

    def draw(self, surface):
        color = (70, 160, 126)
        surface.fill(color)
        self.mTopWall.draw(surface)
        self.mBottomWall.draw(surface)
        self.mLeftWall.draw(surface)
        self.mRightWall.draw(surface)
        self.mScoreBoard.draw(surface)
        self.mLeftPaddle.draw(surface)
        self.mRightPaddle.draw(surface)
        self.mBall.draw(surface)
        return
