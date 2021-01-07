# panopto-downloader

downloads panopto video from stream to solve the problem where if there is a camera and a monitor you can't download the camera video without the monitor

(assuming you are using chrome)
1. open the panopto video you want to download and open developer tools (ctrl+shift+i)
2. in the network tab search for .ts
3. right click on any of the files and click on copy->copy link address
4. paste the url without the /#####.ts at the end where it sais 'url goes here'
5. make shure the script is running from a new folder as its "janky as hell" <-- **this step is importent**
6. new.ts is the finished product take it and delete the folder
