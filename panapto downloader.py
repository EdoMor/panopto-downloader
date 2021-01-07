from requests import get, exceptions
import shutil


baseurl='url goes here'+'/{:05d}.ts'
ts_file_list=[]

def download_file(url):
    local_filename = url.split('/')[-1]
    print('downloading '+local_filename)
    # NOTE the stream=True parameter below
    with get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
    return local_filename

i=0
while True:
    fileurl=baseurl.format(i)
    if i==733:
        raise ValueError('maximum video overflow')
    try:
        download_file(fileurl)
    except exceptions.HTTPError as e:
        print('done')
        break
    i+=1


for j in range(0,i):
    ts_file_list.append("{:05d}.ts".format(j))

with open('new.ts', 'wb') as merged:
    for ts_file in ts_file_list:
        with open(ts_file, 'rb') as mergefile:
            shutil.copyfileobj(mergefile, merged)
            print('murging'+ts_file)
print('done. new.ts was succsesfully downloaded')
exit(0)