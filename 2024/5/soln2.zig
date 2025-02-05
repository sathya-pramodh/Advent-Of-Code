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

        if (!ok) {
            var inDeg = std.AutoHashMap(u64, u64).init(allocator);
            defer inDeg.deinit();
            for (items.items) |num| {
                try inDeg.put(num, 0);
                for (items.items) |other| {
                    if (edges.get(other)) |nums| {
                        for (nums.items) |child| {
                            if (child == num) {
                                inDeg.getPtr(num).?.* += 1;
                                break;
                            }
                        }
                    }
                }
            }

            var order = std.ArrayList(u64).init(allocator);
            defer order.deinit();
            while (order.items.len < items.items.len) {
                var root: u64 = undefined;
                var inDegIter = inDeg.iterator();
                while (inDegIter.next()) |entry| {
                    if (entry.value_ptr.* == 0) {
                        root = entry.key_ptr.*;
                        entry.value_ptr.* = std.math.maxInt(u64);
                        break;
                    }
                }

                if (edges.get(root)) |associated| {
                    for (associated.items) |other| {
                        if (inDeg.getPtr(other)) |deg| {
                            deg.* -= 1;
                        }
                    }
                }
                try order.append(root);
            }

            ans += order.items[@as(usize, order.items.len / 2)];
        }
    }

    std.debug.print("{d}\n", .{ans});
}
