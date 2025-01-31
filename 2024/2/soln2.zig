const std = @import("std");
const ul = @import("ul");

fn checkSafe(items: std.ArrayList(i64)) bool {
    var diff = items.items[1] - items.items[0];
    var sign: i8 = 1;
    if (diff < 0) {
        sign = -1;
    }
    if (@abs(diff) < 1 or @abs(diff) > 3) {
        return false;
    }
    var i: usize = 2;
    var isSafe: bool = true;
    while (i < items.items.len) {
        diff = items.items[i] - items.items[i - 1];
        var curSign: i8 = 1;
        if (diff < 0) {
            curSign = -1;
        }
        if (sign != curSign) {
            isSafe = false;
            break;
        }

        if (@abs(diff) < 1 or @abs(diff) > 3) {
            isSafe = false;
            break;
        }
        i += 1;
    }
    return isSafe;
}

pub fn main() !void {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile("input.txt", .{ .mode = .read_only });
    defer file.close();
    var grid = std.ArrayList(std.ArrayList(i64)).init(allocator);
    defer grid.deinit();
    const buffer = try ul.fileReadGrid(allocator, file, &grid);
    defer allocator.free(buffer);

    var ans: u64 = 0;
    for (grid.items) |row| {
        var i: usize = 0;
        if (checkSafe(row)) {
            ans += 1;
            continue;
        }
        var isSafeAfterModify: bool = false;
        while (i < row.items.len) {
            var cpyRow = std.ArrayList(i64).init(allocator);
            try ul.copyExcluding(row, &cpyRow, i);
            if (checkSafe(cpyRow)) {
                isSafeAfterModify = true;
                break;
            }
            i += 1;
        }

        if (isSafeAfterModify) {
            ans += 1;
        }
    }

    std.debug.print("{d}\n", .{ans});
}
