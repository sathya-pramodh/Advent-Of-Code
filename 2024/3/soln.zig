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

    var ans: i64 = 0;
    const ref = "mul(";
    for (lines.items) |line| {
        var cur: usize = 0;
        while (cur < line.len) {
            var refPtr: usize = 0;
            while (line[cur] == ref[refPtr]) {
                cur += 1;
                refPtr += 1;
            }

            if (refPtr != ref.len) {
                cur += 1;
                continue;
            }

            if (!std.ascii.isDigit(line[cur])) {
                cur += 1;
                continue;
            }

            var start: usize = cur;
            while (line[cur] != ',' and std.ascii.isDigit(line[cur])) {
                cur += 1;
            }

            if (line[cur] != ',') {
                cur += 1;
                continue;
            }

            const n1: i64 = try ul.parseInt(i64, line[start..cur], 10);

            cur += 1;

            start = cur;
            while (line[cur] != ')' and std.ascii.isDigit(line[cur])) {
                cur += 1;
            }

            if (line[cur] != ')') {
                cur += 1;
                continue;
            }

            const n2: i64 = try ul.parseInt(i64, line[start..cur], 10);
            cur += 1;
            ans += n1 * n2;
        }
    }

    std.debug.print("{d}\n", .{ans});
}
