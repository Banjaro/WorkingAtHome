/* krpano 1.17 radar plugin (build 2014-04-03) */
var krpanoplugin=function(){function z(){var f=k,d=g/2;if(r){var c=a.getmouse(!0);c.x*=g/Number(e.width);c.y*=g/Number(e.height);c=180*Math.atan2(c.y-d,c.x-d)/Math.PI;c-=p;null==l?l=c-j.view.hlookat:j.view.hlookat=c-l}var c=(p+s-90+j.view.hlookat)*Math.PI/180,b=0.5*j.view.fov*Math.PI/180;t&&(b=-b);if(0.01<Math.abs(c-w)||0.02<Math.abs(b-x))w=c,x=b,h=!0;h&&(h=!1,f.clearRect(0,0,g,g),f.fillStyle="rgba("+(m>>16&255)+","+(m>>8&255)+","+(m&255)+","+u+")",f.strokeStyle="rgba("+(n>>16&255)+","+(n>>8&255)+
","+(n&255)+","+v+")",f.lineWidth=q,f.beginPath(),f.moveTo(d,d),f.arc(d,d,d-q,c-b,c+b),f.fill(),f.lineTo(d,d),f.stroke())}var j=null,a=null,e=null,k=null,g=256,p=0,s=90,t=!1,m=16777215,n=16777215,u=0.5,v=0.3,q=0,r=!1,l=null,h=!0,y=null,w=0,x=0;this.registerplugin=function(f,d,c){j=f;a=c;"1.0.8.14">j.version||"2011-03-30">j.build?(j.trace(3,"radar plugin - too old krpano version (min. 1.0.8.14)"),a=j=null):(a.registerattribute("heading",0,function(b){p=Number(b);h=!0},function(){return p}),a.registerattribute("headingoffset",
90,function(b){s=Number(b);h=!0},function(){return s}),a.registerattribute("invert",!1,function(b){t="true"==String(b).toLowerCase();h=!0},function(){return t}),a.registerattribute("fillcolor",16777215,function(b){m=parseInt(b);h=!0},function(){return m}),a.registerattribute("linecolor",16777215,function(b){n=parseInt(b);h=!0},function(){return n}),a.registerattribute("fillalpha",0.5,function(b){u=Number(b);h=!0},function(){return u}),a.registerattribute("linealpha",0.3,function(b){v=Number(b);h=
!0},function(){return v}),a.registerattribute("linewidth",0,function(b){q=Number(b);h=!0},function(){return q}),a.handcursor=!1,a.ondown=function(){r=!0;l=null},a.onup=function(){r=!1;l=null},a.registercontentsize(g,g),e=document.createElement("canvas"),e.width=g,e.height=g,e.style.width="100%",e.style.height="100%",e.onselectstart=function(){return!1},a.sprite.appendChild(e),k=e.getContext("2d"),y=setInterval(z,1E3/30))};this.unloadplugin=function(){j&&a&&(clearInterval(y),a.sprite.removeChild(e),
j=a=e=k=null)};this.hittest=function(a,d){return k.isPointInPath(a,d)};this.onresize=function(a,d){g=Math.max(a,d);e.width=a;e.height=d;k.scale(a/g,d/g);h=!0;return!1}};