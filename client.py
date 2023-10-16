import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

s.connect((host, port))
allData = ""
path = "E:/data/data.txt" 
s.send(path.encode())

def calculate_sum(data):
    numbers = [int(num) for num in data.split() if num.isdigit()]
    return sum(numbers)

while True:
    data = input("Nhập chuỗi số nguyên (nhập '.' để thoát): ")
    if data == '.':
        break
    allData += data + "\n"
print("allData: " + allData)
s.send(allData.encode())
response = s.recv(1024).decode()
print(response)   

print("\n Tính tổng từ file data.txt: ")
try:
    with open("data.txt", "r") as file:
        dataFile = file.read()
        print(data)
except FileNotFoundError:
    print("Tệp data.txt không tồn tại.")
except IOError as e:
    print(f"Lỗi khi đọc tệp data.txt: {e}")
allDataFile = dataFile.split("\n")   
for i in range(0, len(allDataFile)-1):
    total = calculate_sum(allDataFile[i])
    print(f"Tổng chuỗi dòng {++i} là: {total} \n")
s.close()
