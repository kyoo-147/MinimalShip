# MINFLOW 0.1 — Bộ skill phát triển sản phẩm tối giản

**Mục tiêu:** Làm đúng phần cần thiết → prototype hoạt động sớm → kiểm thử → cải tiến. Không biến ý tưởng nhỏ thành framework lớn, không coi tài liệu là thành quả thay cho code chạy được.

## Có gì trong bộ này?
- `SKILL.md`: chỉ thị dành cho Pi (ngắn, chạy theo 7 giai đoạn).
- `templates/RUN.md`: **một tài liệu duy nhất** cho mục tiêu, spec, task, lựa chọn worker, acceptance và bằng chứng test.
- `references/orchestration.md`: cách phối hợp Pi + Herdr + một orchestrator + Lavish khi cần.
- `references/yc-principles.md`: bộ lọc quyết định rút từ YC.
- `references/yc-comprehensive.vi.md`: trích xuất chi tiết đầy đủ các chủ đề, chương, ví dụ và lưu ý từ nguồn.
- `sources/`: **5 file gốc, sao chép nguyên byte**, không làm mất nội dung. `references/complete-line-index.md` có chỉ số từng dòng cho kiểm chứng.
- `scripts/install.py`: cài theo project hoặc global vào Pi mà không cần ghi đè nếu chưa chọn --force.
- `scripts/check.py`: kiểm tra cấu trúc bộ skill, nguồn và bảo đảm không mất dòng.

## Cài trong Pi
Giải nén toàn bộ thư mục `MINFLOW/`, sau đó tại chính thư mục chứa `SKILL.md`:

```bash
python scripts/install.py --global
# hoặc trong project muốn dùng:
python scripts/install.py --project /path/to/project
```

Trên Windows PowerShell:

```powershell
py .\scripts\install.py --global
# hoặc
py .\scripts\install.py --project D:\work\my-project
```

Sau khi cài, vào **Herdr**, khởi động Pi (hoặc reload), gõ:

```text
/skill:minflow Build a working prototype today for <feature>. Ask me once for worker model, thinking, fast mode, limit, budget and approval before spawning.
```

Skill không tự cài đặt Pi/Herdr/orchestrator và không tự kết nối VPS từ chat này. Phải có `pi` và `herdr` hoạt động trên máy thật để điều phối worker. Trên Windows từng gặp lỗi `pi.ps1` bị chặn bởi PowerShell Execution Policy: có thể kiểm tra nhanh với `pi.cmd --version` trước khi chỉnh policy; không cần tắt bảo vệ toàn hệ thống chỉ để thử.

## Lựa chọn orchestrator
**Nên ưu tiên thử `pi-herdsman`** nếu làm việc với nhiều worker, nhiều nhánh và quyền sở hữu task. Nếu muốn giao diện tool ít hơn, có thể thử `pi-herdr` trong môi trường riêng. Hai thứ này không nên là orchestrator mặc định cùng lúc; tham khảo các README gốc để kiểm tra phiên bản/runtime.

## Cách chạy một prototype trong một ngày
- Buổi đầu: kiểm tra repo và một lần chốt kết quả cần chạy + phân phối model/thinking/worker/permission.
- Tiếp: lập `RUN.md` thật ngắn, tạo skeleton có thể chạy và giao các task thực sự độc lập.
- Giữa buổi: thực thi song song, liên tục tích hợp các vertical slice, sửa lỗi sớm.
- Cuối: chạy build, smoke end-to-end, regression liên quan và demo theo acceptance.
- Báo cáo PASS/FAIL/BLOCKED trung thực; đưa optional feature sang chu kỳ sau.

Không có bảo đảm hoàn tất trong một ngày nếu yêu cầu, repo, dữ liệu hay hạ tầng chưa sẵn sàng. Hạn một ngày là **timebox để giảm scope**, không phải lý do bỏ kiểm thử hoặc che giấu lỗi.

## 5 rào chắn chống overengineering
1. Một `RUN.md`, không sinh hàng loạt PRD/ADR/diagrams mặc định.
2. Mỗi tác vụ chỉ một kết quả kiểm chứng được.
3. Chỉ tạo abstraction/dependency mới khi nó giải quyết nhu cầu hiện hữu.
4. Worker làm song song khi tách sở hữu file/interface được; không tạo xung đột chỉ để tăng số agent.
5. Chỉ đánh dấu DONE khi có bằng chứng từ chạy thử.

Nguồn tham khảo: tài liệu anh tải lên, https://www.ycombinator.com/blog/product-development-cycle-fundamentals/, https://github.com/kunchenguid/lavish-axi, https://github.com/mattpocock/skills, https://github.com/boadij/pi-herdsman, https://github.com/AndrewJacop/pi-herdr, https://pi.dev/docs/latest/skills.
