# Hướng dẫn chạy chương trình Digit Recognition

## Yêu cầu

-   Python 3.x đã được cài đặt trên hệ thống.

## Bước 1: Chuẩn bị môi trường ảo

1. Mở terminal hoặc command prompt.
1. Di chuyển đến thư mục chứa mã nguồn của chương trình.
1. Tạo một môi trường ảo mới bằng cách chạy lệnh sau:

    ```
    python -m venv venv
    ```

1. Kích hoạt môi trường ảo bằng cách chạy lệnh sau:

    ```
    source venv/bin/activate   # Linux/MacOS
    venv\Scripts\activate      # Windows
    ```

## Bước 2: Cài đặt các thư viện cần thiết

5. Cài đặt các thư viện cần thiết bằng lệnh sau:

    ```
    pip install -r requirements.txt
    ```

## Bước 3: Chạy chương trình

6. Chạy chương trình bằng cách chạy lệnh sau:

    ```
    python app.py
    ```

## Sử dụng chương trình

7. Khi chạy chương trình, một cửa sổ mới sẽ xuất hiện với giao diện ứng dụng nhận dạng chữ số viết tay.
8. Vẽ một chữ số trên ô vẽ trắng.
9. Nhấn nút "Predict" để dự đoán chữ số đã vẽ.
10. Kết quả dự đoán sẽ hiển thị bên dưới, cùng với xác suất của mỗi lớp.
11. Bạn có thể xóa hình vẽ bằng cách nhấn nút "Clear" và vẽ một chữ số mới.

Chúc mừng bạn đã sử dụng thành công chương trình nhận dạng chữ số viết tay!
