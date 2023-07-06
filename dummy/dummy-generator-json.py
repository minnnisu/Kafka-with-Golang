import json
import os
import random

dummy_data = [{"name":"Tasks","account":"56496690"},{"name":"Charlie","account":"95802355"},{"name":"Avery","account":"19112961"},{"name":"Jules","account":"47408171"},{"name":"Quinn","account":"73006359"},{"name":"Shawn","account":"48295626"},{"name":"Avery","account":"63586772"},{"name":"Sasha","account":"22063128"},{"name":"Drew","account":"19568190"},{"name":"Sasha","account":"42065543"},{"name":"James","account":"50124223"},{"name":"Corey","account":"08898534"},{"name":"Jamie","account":"15991543"},{"name":"Dakota","account":"12156377"},{"name":"Greer","account":"92691606"},{"name":"Anderson","account":"65570233"},{"name":"James","account":"34940833"},{"name":"Logan","account":"90511389"},{"name":"Emerson","account":"59891046"},{"name":"London","account":"67477771"},{"name":"Taylor","account":"60458952"},{"name":"Ryan","account":"61829282"},{"name":"Skyler","account":"00330375"},{"name":"Arden","account":"98687554"},{"name":"Kyle","account":"68873747"},{"name":"Robin","account":"05324016"},{"name":"Anderson","account":"47975573"},{"name":"Kennedy","account":"42201041"},{"name":"August","account":"09554896"},{"name":"Jamie","account":"37893954"},{"name":"Noah","account":"65272717"},{"name":"Harper","account":"39122867"},{"name":"Micah","account":"91501413"},{"name":"Cameron","account":"87943395"},{"name":"Jamie","account":"26994132"},{"name":"Rory","account":"85408753"},{"name":"Jules","account":"57002139"},{"name":"Arden","account":"20087686"},{"name":"Jules","account":"28606357"},{"name":"Logan","account":"43372187"},{"name":"Robin","account":"69399605"},{"name":"Hayden","account":"90552252"},{"name":"Reese","account":"17202814"},{"name":"Kyle","account":"78641192"},{"name":"Quinn","account":"76148960"},{"name":"Greer","account":"74602907"},{"name":"Brooklyn","account":"36847747"},{"name":"Arden","account":"24822966"},{"name":"Brooklyn","account":"90325158"},{"name":"River","account":"04037802"},{"name":"Addison","account":"43121117"},{"name":"Noah","account":"09395033"},{"name":"Blake","account":"74914504"},{"name":"Hayden","account":"50474607"},{"name":"Marlowe","account":"97074086"},{"name":"Harper","account":"89831829"},{"name":"Blake","account":"98375074"},{"name":"North","account":"41276761"},{"name":"Austin","account":"61151229"},{"name":"Bowie","account":"22099768"},{"name":"Reagan","account":"94275398"},{"name":"Sawyer","account":"23080111"},{"name":"London","account":"80857201"},{"name":"Riley","account":"86704131"},{"name":"Skyler","account":"26464025"}]

# 빈 JSON 객체 생성
json_data = [] 

mb = 100

size = 15*1024*mb # 1MB / 하나의 데이터

for i in range(size):
    idx = random.randint(0, 64)
    json_data.append(dummy_data[idx])

# JSON 형식으로 변환
json_string = json.dumps(json_data, indent=4)

# 5. 변경된 JSON 데이터를 기존 파일에 쓰기
with open(str(mb) + 'MB_dummy.json', 'w') as file:
    file.write(json_string)
 
file_size = os.path.getsize('./' + str(mb) + 'MB_dummy.json') 
print('File Size:', file_size, 'bytes')