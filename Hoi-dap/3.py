import requests
import json

# URL của tệp JSON
url = "https://mocki.io/v1/641d1b89-50ca-401a-9c6c-e149d4a6e562"  # Thay thế bằng URL thực tế của tệp JSON

try:
    # Gửi yêu cầu GET đến URL
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không (status code 200)
    if response.status_code == 200:
        # Giải mã dữ liệu JSON từ nội dung nhận được
        data = response.json()

        # Câu hỏi 2: In ra số keyword và danh sách keyword có trong thông tin 1 nhóm.
        num_keywords = len(data.keys())
        keyword_list = list(data.keys())
        print(f"Câu hỏi 2: {num_keywords} ({', '.join(keyword_list)})")

        # Câu hỏi 3: In ra số thành viên mặc định của 1 nhóm.
        num_members = len(data["members"])
        print(f"Câu hỏi 3: Số thành viên mặc định của nhóm là {num_members}")

        # Câu hỏi 4: In ra thông tin nhóm
        print("Câu hỏi 4: Thông tin nhóm là:")
        print(f"Team ID: {data['team_id']}")
        print(f"Team Name: {data['team_name']}")
        print("Members:")
        for member in data["members"]:
            print(f"Name: {member['name']}, Student ID: {member['student_id']}")
        print(f"Message: {data['message']}")

    else:
        print("Yêu cầu không thành công. Status code:", response.status_code)

except Exception as e:
    print("Có lỗi xảy ra:", str(e))
