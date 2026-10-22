# MinimalShip

**Build what matters. Ship what works. Improve what users need.**

MinimalShip là bộ sản phẩm được xây dựng từ nhu cầu thật: bắt đầu với một vấn đề cụ thể, đưa phiên bản nhỏ có giá trị đến tay người dùng, rồi liên tục cải tiến dựa trên phản hồi và dữ liệu thực tế.

Đây cũng là không gian chung để phát triển mã nguồn, bộ skill và công cụ phục vụ quá trình làm sản phẩm.

## Triết lý sản phẩm

### Build what matters

- Bắt đầu từ vấn đề có thật, không từ một danh sách tính năng hay công nghệ đang thịnh hành.
- Hiểu rõ người dùng là ai, họ đang gặp khó khăn gì và hiện giải quyết bằng cách nào.
- Phục vụ tốt một nhóm người dùng cụ thể trước khi mở rộng.
- Mỗi tính năng cần có lý do tồn tại và cách kiểm chứng giá trị.

### Ship what works

- Ra mắt phiên bản nhỏ nhất giải quyết được một nhu cầu trọn vẹn.
- Tối giản phạm vi, không cắt bỏ chất lượng của trải nghiệm cốt lõi.
- Làm theo chu kỳ ngắn; chia nhỏ những đầu việc chưa thể hoàn thành trong một chu kỳ.
- Kiểm thử luồng chính và lỗi hồi quy trước khi phát hành.
- Chấp nhận làm thủ công lúc đầu để hiểu bài toán; tự động hóa khi nút thắt đã rõ.

### Improve what users need

- Chủ động tiếp cận, hỗ trợ và lắng nghe những người dùng đầu tiên.
- Kết hợp phản hồi trực tiếp với dữ liệu sử dụng, không chỉ dựa vào cảm tính.
- Đo kết quả mà người dùng đạt được, không lấy số tính năng đã làm làm thước đo thành công.
- Cải tiến, loại bỏ hoặc mở rộng tính năng dựa trên bằng chứng mới.

## Cách chúng ta làm việc

**Hiểu vấn đề → Chọn mục tiêu → Xây bản nhỏ → Kiểm thử → Phát hành → Đo lường & lắng nghe → Cải tiến.**

Mỗi chu kỳ có một mục tiêu chính. Trước khi bắt đầu một đầu việc, cần làm rõ:

1. **Người dùng và vấn đề:** Ai cần việc này? Khó khăn cụ thể là gì?
2. **Kết quả mong muốn:** Điều gì sẽ tốt hơn sau khi hoàn thành?
3. **Phạm vi:** Phần nào bắt buộc, phần nào có thể để sau?
4. **Trách nhiệm:** Ai chịu trách nhiệm hoàn thành?
5. **Điều kiện hoàn thành:** Kiểm thử thế nào và đo hiệu quả bằng gì?

Ưu tiên được điều chỉnh theo những gì học được ở mỗi chu kỳ, thay vì bám cứng vào một roadmap dài hạn.

## Nguyên tắc chung cho bộ sản phẩm

- **Tập trung:** Mỗi sản phẩm có một giá trị cốt lõi rõ ràng.
- **Dễ sử dụng:** Giảm thao tác thừa và giúp người dùng hoàn thành công việc.
- **Đáng tin cậy:** Tốc độ phát hành không thay thế cho kiểm thử, an toàn dữ liệu và khả năng vận hành.
- **Vừa đủ:** Chọn giải pháp đơn giản đáp ứng nhu cầu hiện tại; chỉ thêm độ phức tạp khi cần.

## Mã nguồn, skill và tài liệu

Repository lưu mã nguồn, bộ skill có thể tái sử dụng và hướng dẫn cần thiết để làm việc với dự án.

Tài liệu tham khảo, ghi chú nghiên cứu và các bản phân tích trong quá trình làm việc **chỉ lưu cục bộ**, không commit hoặc push. Các thư mục `docs/`, `analysis/` và `.local/` đã được đưa vào `.gitignore` cho mục đích này.

## Trạng thái

Dự án đang ở giai đoạn thiết lập nền tảng. Chưa có sản phẩm được triển khai, stack công nghệ hay lệnh cài đặt/chạy ứng dụng được xác định trong repository.

Phần hướng dẫn chạy và kiểm thử sẽ được bổ sung cùng mã nguồn của sản phẩm đầu tiên.
