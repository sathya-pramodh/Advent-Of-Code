const std = @import("std");
const ul = @import("ul");

pub fn main() !void {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile("input.txt", .{ .mode = .read_only });
    defer file.close();
    var lines = std.ArrayList([]u8).init(allocator);
    defer lines.deinit();
    const buffer = try ul.fileReadLines(allocator, file, &lines);
    defer allocator.free(buffer);
}
