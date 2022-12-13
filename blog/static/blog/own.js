
var d = document.getElementsByClassName("mobile-menu-toggle");
console.log(d)
d[0].onclick = function(){  
    var menu = document.getElementById('slide-menu');
    var overlay = document.getElementsByClassName('overlay')[0];
    //menu.style.webkitTransform = "translateX(0)"
    menu.style.transform="translateX(0)";
    menu.style.visibility="visible";
    
    overlay.style.visibility ="visible";
    overlay.style.opacity="100";

    //alert("function working")
    //menu.style="-webkit-transform: translateX(0);transform: translateX(0);visibility: show;"
}
var f = document.getElementsByClassName("hide-litespot-pro-mobile-menu")[0];
    f.onclick = function(){
        var menu = document.getElementById('slide-menu');
        var overlay = document.getElementsByClassName('overlay')[0];
        //menu.style.webkitTransform = "translateX(0)"
        menu.style.transform="translateX(-100%)";
        menu.style.visibility="hidden";
        overlay.style.visibility ="hidden";
        overlay.style.opacity="0";
    }


    var search = document.getElementById('main-search-wrap')
        search.style.display="none"