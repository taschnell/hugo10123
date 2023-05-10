#include <raylib.h>
#include <iostream>

using namespace std;

// Global Var
const int win_width = 1920;
const int win_height = 1080;

class Ball
{
public:
    float x, y;
    int dx, dy;
    int radius;

    void Draw()
    {
        DrawCircle(x, y, radius, YELLOW);
    }

    void Update()
    {
        x += dx;
        y += dy;

        if (y + radius >= win_height || y - radius <= 0)
        {
            dy = -dy;
        }
        if (x + radius >= win_width || x - radius <= 0)
        {
            dx = -dx;
        }
    }
};

class Paddle
{
protected:
    void LimitMovement()
    {
        if (y <= 0)
        {
            y = 0;
        }
        if (y + height >= win_height){
            y = win_height - height;
        }
    }

public:
    float x, y;
    float width, height;
    int dy;

    void Draw()
    {
        DrawRectangle(x, y, width, height, BLACK);
    }
    void Update()
    {
        if (IsKeyDown(KEY_UP))
        {
            y = y - dy;
        }
        else if (IsKeyDown(KEY_DOWN))
        {
            y = y + dy;
        }
        LimitMovement();
    }
    
};

class CpuPaddle : public Paddle
{
public:
    void Update(int ball_y)
    {
        if (y + height / 2 > ball_y)
        {
            y = y - dy;
        }
        if (y + height / 2 < ball_y)
        {
            y = y + dy;
        }
        LimitMovement();
    }
};

Paddle player;
Ball ball;
CpuPaddle cpu;
int main()
{

    cout << "Game Start" << endl;

    const int paddle_height = 250;

    ball.radius = 30;
    ball.x = win_width / 2;
    ball.y = win_height / 2;
    ball.dx = 7;
    ball.dy = 7;

    InitWindow(win_width, win_height, "Pong");
    SetTargetFPS(60);

    player.width = 30;
    player.height = 200;
    player.x = win_width - player.width - 10;
    player.y = win_height / 2 - player.height;
    player.dy = 6;

    cpu.width = 30;
    cpu.height = 200;
    cpu.x = 10;
    cpu.y = win_height / 2 - player.height;
    cpu.dy = 6;

    while (WindowShouldClose() == false)
    {
        BeginDrawing();
        // Update
        ball.Update();
        player.Update();
        cpu.Update(ball.y);

        if (CheckCollisionCircleRec(Vector2{ball.x, ball.y}, ball.radius, Rectangle{player.x, player.y, player.width, player.height})){
            ball.dx = -ball.dx;
        }
        if (CheckCollisionCircleRec(Vector2{ball.x, ball.y}, ball.radius, Rectangle{cpu.x, cpu.y, cpu.width, cpu.height})){
            ball.dx = -ball.dx;
        }



        // Drawing
        ClearBackground(WHITE);

        // Draw
        player.Draw();
        cpu.Draw();
        ball.Draw();
        EndDrawing();
    }

    CloseWindow();
}