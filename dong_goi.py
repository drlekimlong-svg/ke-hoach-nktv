"""Đóng gói app và sinh bản kế hoạch từ cùng một nguồn.

Nguồn:  nguon/ke-hoach.json  (khung 14 đầu việc)
        nguon/app.src.html   (giao diện và mã)
Ra:     index.html                                   (app, một tệp, mở trực tiếp được)
        ../KE_HOACH_TRIEN_KHAI_NAM_HOC_2026-2027.md  (bản kế hoạch để đọc và in)

Chạy:   python dong_goi.py
"""
import io
import json
from pathlib import Path

GOC = Path(__file__).resolve().parent
NGUON = GOC / "nguon"
THU = ["T2", "T3", "T4", "T5", "T6", "T7", "CN"]


def dmy(iso):
    return f"{iso[8:10]}/{iso[5:7]}/{iso[0:4]}" if iso else ""


def thu(iso):
    from datetime import date
    y, m, d = (int(x) for x in iso.split("-"))
    return THU[date(y, m, d).weekday()]


def dong_goi_app(seed_text):
    src = (NGUON / "app.src.html").read_text(encoding="utf-8")
    assert src.count("__SEED__") == 1, "Thiếu hoặc thừa chỗ đặt __SEED__"
    gon = json.dumps(json.loads(seed_text), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    out = src.replace("__SEED__", gon)
    io.open(GOC / "index.html", "w", encoding="utf-8", newline="\n").write(out)
    return len(out.encode("utf-8"))


def ban_ke_hoach(k):
    dv = k["dauViec"]
    so = {d["id"]: d["so"] for d in dv}
    L = []
    a = L.append
    a(f"# KẾ HOẠCH TRIỂN KHAI NĂM HỌC {k['namHoc']}")
    a("")
    a(f"**Đơn vị:** {k['donVi']}  ")
    a(f"**Phiên bản khung:** {k['phienBan']}, lập ngày {dmy(k['ngayLap'])}  ")
    a("**Dùng cho:** cuộc họp Ban chủ nhiệm và nhóm trưởng các nhà Mascot chiều 09/10/2026  ")
    a(f"**Trạng thái:** {k['trangThaiKhung']}")
    a("")
    a("Bản này sinh từ cùng nguồn dữ liệu với app quản lý (`app-ke-hoach/`). Khi họp, ghi người phụ trách, hạn và quyết định vào app rồi xuất biên bản; không cần điền tay vào bản này.")
    a("")
    a("## Cách đọc")
    a("")
    a("- **Việc cụ thể** là các việc đủ nhỏ để giao cho một người hoặc một nhà.")
    a("- **Hạn gợi ý** do agent đề xuất, tính từ ngày 09/10/2026, phần lớn đặt vào Chủ nhật. Ô để trống là việc phụ thuộc một mốc chưa có (ngày tuyển quân, ngày tổ chức workshop).")
    a("- **Cần chốt** là các câu hỏi nên có câu trả lời ngay trong cuộc họp, vì các việc phía sau phụ thuộc vào đó.")
    a("")
    a("## Tổng quan 14 đầu việc")
    a("")
    a("| # | Đầu việc | Nhóm việc | Điều kiện khởi động | Mốc gợi ý đầu – cuối |")
    a("|---|---|---|---|---|")
    for d in dv:
        g = sorted(v["goiY"] for v in d["viec"] if v.get("goiY"))
        moc = f"{dmy(g[0])} – {dmy(g[-1])}" if g else ""
        a(f"| {d['so']} | {d['ten']} | {d['nhom']} | {d['dieuKien']} | {moc} |")
    a("")
    a("## Thứ tự khởi động")
    a("")
    for d in dv:
        for p in d.get("phuThuoc", []):
            them = f" {d['thayThe']}" if d.get("thayThe") else ""
            a(f"- Đầu việc {so[p]} xong thì mở đầu việc {d['so']} ({d['ten']}).{them}")
    a("- Đầu việc 13 (tiêu chí danh hiệu) và 14 (điểm cộng) nên soạn và công bố cùng lúc, vì danh hiệu xét trên điểm cộng.")
    a("- Đầu việc 12 (tuyển quân) quyết định lịch của đầu việc 10 (tập huấn Junior).")
    a("- Làm ngay được sau cuộc họp: 1, 2, 6, 7, 9, 11, 12, 13, 14, và phần chạy thử QR tạm của đầu việc 5.")
    a("")
    a("## Ba điểm agent đề nghị lưu ý trước khi họp")
    a("")
    a("1. **Giá trị cốt lõi, sứ mệnh, tầm nhìn (đầu việc 12).** Trong hồ sơ CLB ngày 30/09/2026, năm giá trị và câu sứ mệnh còn ở trạng thái ứng viên; chưa có câu tầm nhìn nào được ghi nhận. Muốn truyền thông tuyển quân dựa trên các nội dung này thì cần chốt chính thức trước: câu chữ chính xác, người duyệt, ngày hiệu lực. Việc 12.1 dành cho điều đó.")
    a("2. **Câu “điều mà trước giờ chưa có CLB nào làm được”.** Đây là nhận định so sánh chưa có nguồn kiểm chứng. Dùng nội bộ để khích lệ thì được; khi đưa lên bài truyền thông công khai nên thay bằng điều CLB tự chứng minh được, đúng với nguyên tắc liêm chính và thực chất.")
    a("3. **Dữ liệu cá nhân.** Các đầu việc 3, 4, 5, 14 đều tạo ra dữ liệu gắn với từng thành viên (mã QR, chuyên cần, điểm cộng, năng lực, có thể cả điểm học tập). Nên chốt một lần cho cả bốn việc: ai được xem, lưu ở đâu, thành viên đồng ý bằng cách nào.")
    a("")
    for d in dv:
        a("---")
        a("")
        a(f"## {d['so']}. {d['ten']}")
        a("")
        a(f"**Nhóm việc:** {d['nhom']}  ")
        dk = d["dieuKien"] + (f" {d['thayThe']}" if d.get("thayThe") else "")
        a(f"**Điều kiện khởi động:** {dk}")
        a("")
        a(f"**Mục tiêu.** {d['mucTieu']}")
        a("")
        if d.get("boiCanh"):
            a(f"**Đã có, cần biết.** {d['boiCanh']}")
            a("")
        if d.get("lienQuan"):
            a("**Liên quan:** " + ", ".join(f"đầu việc {so[x]}" for x in d["lienQuan"]) + ".")
            a("")
        a("**Sản phẩm đầu ra**")
        a("")
        for s in d["sanPham"]:
            a(f"- {s}")
        a("")
        a("**Việc cụ thể để phân công**")
        a("")
        a("| # | Việc | Hạn gợi ý | Phụ trách | Hạn chốt |")
        a("|---|---|---|---|---|")
        for i, v in enumerate(d["viec"], 1):
            g = f"{thu(v['goiY'])} {dmy(v['goiY'])}" if v.get("goiY") else (v.get("luuY") or "")
            a(f"| {d['so']}.{i} | {v['ten']} | {g} | | |")
        a("")
        a("**Cần chốt tại cuộc họp**")
        a("")
        for i, c in enumerate(d["canChot"], 1):
            a(f"{i}. {c}")
        a("")
        if d.get("theoNha"):
            a("**Theo dõi theo từng nhà:** " + "; ".join(d["theoNha"]) + ".")
            a("")
    a("---")
    a("")
    a("## Lịch mốc gợi ý theo tháng")
    a("")
    moc = sorted((v["goiY"], d["so"], i, v["ten"]) for d in dv for i, v in enumerate(d["viec"], 1) if v.get("goiY"))
    thang = ""
    for ngay, s, i, ten in moc:
        if ngay[:7] != thang:
            thang = ngay[:7]
            a("")
            a(f"### Tháng {thang[5:]}/{thang[:4]}")
            a("")
        a(f"- {thu(ngay)} {ngay[8:]}/{ngay[5:7]} · {s}.{i} {ten}")
    a("")
    a("## Lịch sử cập nhật")
    a("")
    a(f"- {dmy(k['ngayLap'])}: Lập khung bản {k['phienBan']} theo 14 đầu việc người dùng nêu; mục tiêu, việc cụ thể, câu cần chốt và hạn gợi ý là đề xuất của agent.")
    a("")
    return "\n".join(L)


def main():
    seed_text = (NGUON / "ke-hoach.json").read_text(encoding="utf-8")
    k = json.loads(seed_text)
    ids = [v["id"] for d in k["dauViec"] for v in d["viec"]]
    assert len(ids) == len(set(ids)), "Trùng mã việc"
    for d in k["dauViec"]:
        for p in d.get("phuThuoc", []) + d.get("lienQuan", []):
            assert any(x["id"] == p for x in k["dauViec"]), f"{d['id']} trỏ tới {p} không tồn tại"
    kb = dong_goi_app(seed_text)
    md = ban_ke_hoach(k)
    ten = f"KE_HOACH_TRIEN_KHAI_NAM_HOC_{k['namHoc'].replace('–', '-')}.md"
    io.open(GOC.parent / ten, "w", encoding="utf-8", newline="\n").write(md)
    print(f"index.html: {kb / 1024:.0f} KB · {len(k['dauViec'])} đầu việc · {len(ids)} việc cụ thể · {ten}")


if __name__ == "__main__":
    main()
