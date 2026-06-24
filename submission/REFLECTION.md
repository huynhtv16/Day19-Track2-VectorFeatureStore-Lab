# Reflection — Lab 19

**Tên:** Tran Van Huynh
**Path đã chạy:** lite

---

## Câu hỏi (≤ 200 chữ)

> Trên golden set 50 queries, mode nào thắng ở loại query nào (`exact` /
> `paraphrase` / `mixed`), và tại sao? Khi nào bạn **không** dùng hybrid
> (i.e. khi nào pure BM25 hoặc pure vector là lựa chọn đúng)?

Trên golden set, hybrid thắng trung bình: 78.6% Precision@10, cao hơn BM25
77.8% và vector 73.2%. Với `exact`, BM25 và hybrid cùng mạnh vì query chứa
từ khóa kỹ thuật xuất hiện trực tiếp trong corpus. Với `mixed`, hybrid thắng
rõ nhất vì nó cộng được tín hiệu lexical của BM25 và tín hiệu semantic của
vector bằng RRF. Với `paraphrase`, trong lite path vector chưa thắng vì model
`bge-small-en-v1.5` không tối ưu cho tiếng Việt; nếu dùng `bge-m3`, kỳ vọng
semantic sẽ tốt hơn.

Tôi sẽ không dùng hybrid khi latency/cost rất chặt và một mode đã đủ tốt:
BM25 cho exact keyword search, filtering, log/audit; pure vector cho semantic
recall hoặc câu hỏi paraphrase khi embedding multilingual tốt. Hybrid cũng
không cần thiết nếu hệ thống nhỏ, yêu cầu ranking đơn giản, hoặc khó vận hành
hai index cùng lúc.

---

## Điều ngạc nhiên nhất khi làm lab này

Điều ngạc nhiên nhất là hybrid không cần công thức phức tạp: chỉ RRF 1-based
đã đủ ổn định hơn hai mode riêng lẻ trên mixed queries.

---

