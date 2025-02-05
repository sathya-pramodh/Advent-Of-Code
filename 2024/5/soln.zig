const std = @import("std");
const ul = @import("ul");

pub fn main() !void {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile("input.txt", .{ .mode = .read_only });
    defer file.close();
    var blocks: [2]std.ArrayList([]u8) = .{ std.ArrayList([]u8).init(allocator), std.ArrayList([]u8).init(allocator) };
    defer for (blocks) |block| {
        block.deinit();
    };
    const buffer = try ul.fileReadBlocks(allocator, file, &blocks);
    defer allocator.free(buffer);

    var edges = std.AutoHashMap(u64, std.ArrayList(u64)).init(allocator);
    defer edges.deinit();

    const firstBlock = blocks[0];
    const secondBlock = blocks[1];
    for (firstBlock.items) |line| {
        var i: usize = 0;
        var num1: u64 = 0;
        while (i < line.len and std.ascii.isDigit(line[i])) {
            num1 = num1 * 10 + @as(u64, @intCast(line[i] - '0'));
            i += 1;
        }
        i += 1;

        var num2: u64 = 0;
        while (i < line.len and std.ascii.isDigit(line[i])) {
            num2 = num2 * 10 + @as(u64, @intCast(line[i] - '0'));
            i += 1;
        }

        var res = try edges.getOrPut(num1);
        if (!res.found_existing) {
            res.value_ptr.* = std.ArrayList(u64).init(allocator);
        }
        try res.value_ptr.append(num2);
    }

    var ans: u64 = 0;
    for (secondBlock.items) |line| {
        var iter = ul.split(u8, line, ",");
        var items = std.ArrayList(u64).init(allocator);
        defer items.deinit();
        while (iter.next()) |numStr| {
            const num = try ul.parseInt(u64, numStr, 10);
            try items.append(num);
        }

        var ok: bool = true;
        var seen = std.AutoHashMap(u64, bool).init(allocator);
        defer seen.deinit();
        for (items.items) |num| {
            if (edges.get(num)) |associatedRules| {
                for (associatedRules.items) |other| {
                    if (seen.get(other) != undefined) {
                        ok = false;
                        break;
                    }
                }
            }
            try seen.put(num, true);
        }

        if (ok) {
            ans += items.items[@as(usize, items.items.len / 2)];
        }
    }

    std.debug.print("{d}\n", .{ans});
}
