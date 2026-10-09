# Kế hoạch năm học 2026–2027 · CLB Ngoại khoa Trưng Vương

App một trang để theo dõi các đầu việc của CLB trong năm học: ai phụ trách, hạn, trạng thái, quyết định và biên bản họp. Chạy hoàn toàn trong trình duyệt; không có máy chủ, không cần đăng nhập.

## Dùng

Mở `index.html` (bấm đúp trên máy tính, hoặc mở địa chỉ web nếu đã đặt lên GitHub Pages).

| Mục | Để làm gì |
|---|---|
| Tổng quan | Tiến độ 14 đầu việc, điều kiện khởi động, việc quá hạn và sắp đến hạn |
| Họp | Đi lần lượt từng đầu việc: ghi người phụ trách, hạn, quyết định, ghi chú; cuối cùng xuất biên bản |
| Đầu việc | Xem và sửa chi tiết từng đầu việc, thêm bớt việc cụ thể, theo dõi theo từng nhà |
| Phân công | Bảng tất cả việc, lọc theo người, trạng thái, quá hạn |
| Lịch | Các hạn xếp theo tháng |
| Nhân sự | Danh sách tên để gợi ý khi phân công |
| Lưu trữ | Xuất biên bản (Word, PDF, Markdown), bảng phân công (CSV), sao lưu và khôi phục |

## Dữ liệu nằm ở đâu

Tên người, hạn, ghi chú **chỉ lưu trong trình duyệt của máy đang dùng**. Kho mã này chỉ chứa khung kế hoạch, không chứa dữ liệu phân công.

- Mỗi địa chỉ mở app (tệp trên máy, hoặc địa chỉ web) có kho dữ liệu riêng. Nên dùng cố định một cách mở.
- Chuyển sang máy khác hoặc gửi cho người cùng quản lý: **Lưu trữ → Sao lưu dữ liệu**, rồi bên kia **Khôi phục từ tệp sao lưu**.
- Nên sao lưu sau mỗi cuộc họp. Xóa dữ liệu duyệt web của trình duyệt sẽ xóa luôn dữ liệu của app.

## Sửa khung kế hoạch

- Sửa nhỏ: ngay trong app, mục “Sửa khung đầu việc” ở cuối mỗi đầu việc.
- Sửa khung gốc: sửa `nguon/ke-hoach.json` hoặc `nguon/app.src.html`, rồi chạy `python dong_goi.py`. Lệnh này tạo lại `index.html` và bản kế hoạch Markdown ở thư mục cha. Khung gốc mới chỉ áp dụng cho máy chưa có dữ liệu, hoặc sau khi bấm “Đặt lại về khung gốc”.
