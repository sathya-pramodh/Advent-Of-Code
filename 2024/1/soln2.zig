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
    defer left.deinit();
    var right = std.ArrayList(i64).init(allocator);
    defer right.deinit();

    for (lines.items) |line| {
        var iter = ul.split(u8, line, "   ");
        try left.append(try ul.parseInt(i64, iter.next().?, 10));
        try right.append(try ul.parseInt(i64, iter.next().?, 10));
    }

    var ans: i64 = 0;
    var freq = std.AutoHashMap(i64, i64).init(allocator);
    defer freq.deinit();
    var left_seen = std.AutoHashMap(i64, bool).init(allocator);
    defer left_seen.deinit();

    for (left.items) |left_num| {
        if (left_seen.get(left_num) != null) {
            continue;
        }
        for (right.items) |right_num| {
            if (left_num == right_num) {
                const res = try freq.getOrPut(left_num);
                if (!res.found_existing) {
                    res.value_ptr.* = 1;
                } else {
                    _ = try freq.put(left_num, res.value_ptr.* + 1);
                }
            }
        }
        _ = try left_seen.put(left_num, true);
    }

    for (left.items) |left_num| {
        const frequency = freq.get(left_num);
        if (frequency == null) {
            continue;
        }
        ans += left_num * frequency.?;
    }
    defer std.debug.print("{d}\n", .{ans});
}
