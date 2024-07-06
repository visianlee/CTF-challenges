#将上面的文件用脚本分隔，加上冒号；
f=open('usbdata.txt','r')
fi=open('out.txt','w')
while 1:
  a=f.readline().strip()
  if a:
    if len(a)==16:#键盘流量的话len为16鼠标为8
      out=''
      for i in range(0,len(a),2):
        if i+2 != len(a):
          out+=a[i]+a[i+1]+":"
        else:
          out+=a[i]+a[i+1]
      fi.write(out)
      fi.write('\n')
  else:
    break
fi.close()