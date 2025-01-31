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
