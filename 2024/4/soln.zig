const std = @import("std");
const ul = @import("ul");

const xmas = "XMAS";

pub fn main() !void {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile("input.txt", .{ .mode = .read_only });
    defer file.close();
    var lines = std.ArrayList([]u8).init(allocator);
    defer lines.deinit();
    const buffer = try ul.fileReadLines(allocator, file, &lines);
    defer allocator.free(buffer);

    var ans: u64 = 0;
    for (lines.items, 0..) |line, r| {
        for (line, 0..) |_, c| {
            var dirs = std.ArrayList([2]i8).init(allocator);
            defer dirs.deinit();
            try ul.padj8(&lines, r, c, &dirs);

            for (dirs.items) |dir| {
                var currentR = r;
                var currentC = c;
                var xmasPtr: usize = 0;
                while (xmasPtr != xmas.len and lines.items[currentR][currentC] == xmas[xmasPtr]) {
                    xmasPtr += 1;
                    if (!ul.inBounds(&lines, currentR, currentC, dir[0], dir[1])) {
                        break;
                    }
                    currentR = @as(usize, @intCast(@as(isize, @intCast(currentR)) + dir[0]));
                    currentC = @as(usize, @intCast(@as(isize, @intCast(currentC)) + dir[1]));
                }
                if (xmasPtr == xmas.len) {
                    ans += 1;
                }
            }
        }
    }
    std.debug.print("{d}\n", .{ans});
}
