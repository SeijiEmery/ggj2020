import std.stdio;
import std.string: toStringz;
import raylib;

void main() {
    const auto screenSize = Vector2(800, 600);
	writefln("%s", screenSize);

	InitWindow(cast(int)screenSize.x, cast(int)screenSize.y, "ggj 2020");
	SetTargetFPS(60);

	while (!WindowShouldClose()) {
		// UPDATE

		// DRAW
		BeginDrawing();
			ClearBackground(RAYWHITE);
			DrawText("Hello, world!".toStringz, 190, 200, 20, LIGHTGRAY);
		EndDrawing();
	}
}