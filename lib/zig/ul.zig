const std = @import("std");
pub const split = std.mem.split;
pub const parseInt = std.fmt.parseInt;

pub fn fileReadLines(allocator: std.mem.Allocator, file: std.fs.File, lines: *std.ArrayList([]u8)) ![]u8 {
    const file_size = (try file.stat()).size;
    const buffer = try allocator.alloc(u8, file_size);
    _ = try file.reader().readAll(buffer);

    var start: usize = 0;
    var end: usize = 0;
    while (end < buffer.len) {
        if (buffer[end] == '\n') {
            try lines.append(buffer[start..end]);
            start = end + 1;
        }
        end += 1;
    }
    if (start < end) {
        try lines.append(buffer[start..end]);
    }
    return buffer;
}

pub fn fileReadGrid(allocator: std.mem.Allocator, file: std.fs.File, grid: *std.ArrayList(std.ArrayList(i64))) ![]u8 {
    var lines = std.ArrayList([]u8).init(allocator);
    defer lines.deinit();
    const buf = try fileReadLines(allocator, file, &lines);
    for (lines.items) |line| {
        var line_parsed = std.ArrayList(i64).init(allocator);
        var iter = split(u8, line, " ");
        while (iter.next()) |num_str| {
            const val = try parseInt(i64, num_str, 10);
            try line_parsed.append(val);
        }
        try grid.append(line_parsed);
    }
    return buf;
}

pub fn fileReadBlocks(allocator: std.mem.Allocator, file: std.fs.File, blocks: *[2]std.ArrayList([]u8)) ![]u8 {
    var lines = std.ArrayList([]u8).init(allocator);
    defer lines.deinit();
    const buf = try fileReadLines(allocator, file, &lines);
    var curIdx: usize = 0;
    for (lines.items) |line| {
        if (std.mem.eql(u8, line, "")) {
            curIdx += 1;
            continue;
        }
        try blocks[curIdx].append(line);
    }
    return buf;
}

pub fn copyExcluding(list: std.ArrayList(i64), cpy: *std.ArrayList(i64), idx: usize) !void {
    var i: usize = 0;
    while (i < list.items.len) {
        if (i == idx) {
            i += 1;
            continue;
        }
        try cpy.append(list.items[i]);
        i += 1;
    }
}

pub fn inBounds(grid: *std.ArrayList([]u8), r: usize, c: usize, i: i8, j: i8) bool {
    const rr = @as(isize, @intCast(r)) + @as(isize, i);
    const cc = @as(isize, @intCast(c)) + @as(isize, j);

    return 0 <= rr and rr < grid.items.len and 0 <= cc and cc < grid.items[0].len;
}

pub fn padj4(grid: *std.ArrayList([]u8), r: usize, c: usize, res: *std.ArrayList([2]i8)) !void {
    const dirs: [4][2]i8 = .{ .{ -1, 0 }, .{ 0, 1 }, .{ 1, 0 }, .{ 0, -1 } };
    for (dirs) |dir| {
        if (inBounds(grid, r, c, dir[0], dir[1])) {
            try res.append(dir);
        }
    }
}

pub fn padj8(grid: *std.ArrayList([]u8), r: usize, c: usize, res: *std.ArrayList([2]i8)) !void {
    const remaining: [4][2]i8 = .{ .{ -1, -1 }, .{ -1, 1 }, .{ 1, -1 }, .{ 1, 1 } };
    try padj4(grid, r, c, res);
    for (remaining) |rem| {
        if (inBounds(grid, r, c, rem[0], rem[1])) {
            try res.append(rem);
        }
    }
}
