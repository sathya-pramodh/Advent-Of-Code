const std = @import("std");
const ul = @import("ul");

const mas = "MAS";
const sam = "SAM";
const words: [2]*const [3:0]u8 = .{ mas, sam };
const diags: [2][3][2]i8 = .{ .{ .{ -1, -1 }, .{ 0, 0 }, .{ 1, 1 } }, .{ .{ 1, -1 }, .{ 0, 0 }, .{ -1, 1 } } };

fn diagHasWord(lines: *std.ArrayList([]u8), r: usize, c: usize, diag: *const [3][2]i8, word: *const [3:0]u8) bool {
    var diagPtr: usize = 0;
    var wordPtr: usize = 0;

    if (!ul.inBounds(lines, r, c, diag[diagPtr][0], diag[diagPtr][1])) {
        return false;
    }

    var currentR = @as(usize, @intCast(@as(isize, @intCast(r)) + diag[diagPtr][0]));
    var currentC = @as(usize, @intCast(@as(isize, @intCast(c)) + diag[diagPtr][1]));
    while (wordPtr != word.len and lines.items[currentR][currentC] == word[wordPtr]) {
        wordPtr += 1;
        diagPtr += 1;
        if (diagPtr == diag.len or !ul.inBounds(lines, r, c, diag[diagPtr][0], diag[diagPtr][1])) {
            break;
        }
        currentR = @as(usize, @intCast(@as(isize, @intCast(r)) + diag[diagPtr][0]));
        currentC = @as(usize, @intCast(@as(isize, @intCast(c)) + diag[diagPtr][1]));
    }

    return wordPtr == word.len;
}

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
            var matchingDiagonals: u8 = 0;
            for (diags) |diag| {
                for (words) |word| {
                    if (diagHasWord(&lines, r, c, &diag, word)) {
                        matchingDiagonals += 1;
                        break;
                    }
                }
            }

            if (matchingDiagonals == 2) {
                ans += 1;
            }
        }
    }
    std.debug.print("{d}\n", .{ans});
}
