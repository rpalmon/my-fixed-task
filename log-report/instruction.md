# Access log report

The file `/app/access.log` contains Apache "common log format" entries, one
request per line, e.g.:

    192.168.0.1 - - [16/Jun/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024

Parse it and write a JSON object to `/app/report.json` with exactly these three keys:

- `total_requests` (integer): the number of non-empty log lines.
- `unique_ips` (integer): the number of distinct client IP addresses (the first
  whitespace-separated field of each line).
- `top_path` (string): the request path (the token after the HTTP method inside
  the quoted request) that appears most often.

Write nothing else to that file. Example shape:

    {"total_requests": 123, "unique_ips": 45, "top_path": "/index.html"}