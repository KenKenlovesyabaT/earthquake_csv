import csv

#rf = open("h2019_head.txt", "r", encoding="utf-8")
rf = open("h2019", "r", encoding="utf-8")

def s_to_d(deg1, min1):
    deg2 = deg1.replace(' ', '')
    min2 = min1.replace(' ', '')
    degree = int(deg2)
    minute = int(min2[0:2]) + (float(min2[2:-1]) / 100)
    return degree + (minute / 60)

def mag(data):
    if data[0] == '-':
        return (0+float(data[1]) / 10)
    elif data[0] == 'A':
        return (-1 - (float(data[1]) /10))
    elif data[0] == 'B':
        return (-2 - (float(data[1]) / 10))
    elif data[0] == 'C':
        return (-3 - (float(data[1]) / 10))
    elif data[0] == ' ':
        return float(0)
    else:
        return int(data[0]) + (float(data[1]) / 10)



#with open("sample.csv", "w", encoding="utf-8") as f:
#with open("sample_m3.csv", "w", encoding="utf-8") as f:
with open("sample_m4.csv", "w", encoding="utf-8") as f:
    header = ['ID', 'date', 'lat', 'lng', 'magnitude']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()

    datalist = rf.readlines()
    eq_id = 0
    for data in datalist:
        date = data[1:5] + '-' + data[5:7] + '-' + data[7:9]
        #lat_degree = int(data[21:24])
        #lat_minute = int(data[24:26]) + (float(data[26:28]) / 100)
        latitude = s_to_d (data[21:24], data[24:28])
        #lng_degree = int(data[32:36])
        #lng_minute = int(data[36:38]) + (float(data[38:40]) / 100)
        longitude = s_to_d(data[32:36], data[36:40])
        magnitude = mag(data[52:54])
        if magnitude >= 4:
            writer.writerow({'ID': eq_id, 'date': date, 'lat': latitude, 'lng': longitude, 'magnitude': magnitude})
            eq_id += 1


f.close()
rf.close()


#datalist = rf.readlines()
#for data in datalist:
#    date = data[1:5] + '-' + data[5:7] + '-' + data[7:9]
#    lat_degree = int(data[21:24])
#    lat_minute = int(data[24:26]) + (float(data[26:28]) / 100)
#    latitude = s_to_d (lat_degree, lat_minute, 0)
#    lng_degree = int(data[32:36])
#    lng_minute = int(data[36:38]) + (float(data[38:40]) / 100)
#    longitude = s_to_d(lng_degree, lng_minute, 0)
#    magnitude = mag(data[52:54])
#    print(f"{eq_id}, {date}, {latitude:.4f}, {longitude:.4f}, {magnitude}")
#    eq_id += 1
