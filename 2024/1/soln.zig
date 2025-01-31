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

    var left = std.ArrayList(i64).init(allocator);
    var right = std.ArrayList(i64).init(allocator);

    var line_cnt: i64 = 0;
    for (lines.items) |line| {
        var iter = ul.split(u8, line, "   ");
        try left.append(try ul.parseInt(i64, iter.next().?, 10));
        try right.append(try ul.parseInt(i64, iter.next().?, 10));
        line_cnt += 1;
    }

    var ans: u64 = 0;
    while (line_cnt != 0) {
        var min_left: ?i64 = null;
        var min_left_idx: ?usize = null;
        var min_right: ?i64 = null;
        var min_right_idx: ?usize = null;

        var i: usize = 0;
        for (left.items) |left_num| {
            if (min_left == null or left_num < min_left.?) {
                min_left = left_num;
                min_left_idx = i;
            }
            i += 1;
        }

        i = 0;
        for (right.items) |right_num| {
            if (min_right == null or right_num < min_right.?) {
                min_right = right_num;
                min_right_idx = i;
            }
            i += 1;
        }

        ans += @abs(min_right.? - min_left.?);
        _ = right.swapRemove(min_right_idx.?);
        _ = left.swapRemove(min_left_idx.?);
        line_cnt -= 1;
    }

    std.debug.print("{d}\n", .{ans});
}
