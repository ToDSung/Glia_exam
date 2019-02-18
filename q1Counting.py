def Counting_file_name():    
    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]


    file_name_dict = {}

    for url in urls:
        split_words = url.split('/')
        if split_words[-1] in file_name_dict:
            file_name_dict[split_words[-1]] += 1
        else:
            file_name_dict[split_words[-1]] = 1

    output_list = sorted(file_name_dict.items(), key=lambda d: (-d[1],d[0]))
    for i in output_list[0:3]:
        print(i[0],end=' ')
        print(i[1])
    
if __name__ == '__main__':
    Counting_file_name()