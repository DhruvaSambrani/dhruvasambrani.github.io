var animation = anime({
    targets: '.card',
    translateX: [-10, 0],
    opacity: [0, 1],
    duration: 500,
    easing: 'linear',
    autoplay: false,
    delay: anime.stagger(150)
})

var nameanim = anime({
    targets: '.landing-name',
    keyframes: [
        { innerHTML: "$ |" },
        { innerHTML: "$ `|" },
        { innerHTML: "$ I|" },
        { innerHTML: "$ F|" },
        { innerHTML: "$ U|" },
        { innerHTML: "$ D|" },
        { innerHTML: "$ Dg|" },
        { innerHTML: "$ Dm|" },
        { innerHTML: "$ DL|" },
        { innerHTML: "$ Dh|" },
        { innerHTML: "$ Dh|" },
        { innerHTML: "$ Dh^|" },
        { innerHTML: "$ Dhe|" },
        { innerHTML: "$ Dhd|" },
        { innerHTML: "$ Dhw|" },
        { innerHTML: "$ Dhr|" },
        { innerHTML: "$ DhrQ|" },
        { innerHTML: "$ DhrV|" },
        { innerHTML: "$ DhrL|" },
        { innerHTML: "$ DhrW|" },
        { innerHTML: "$ Dhru|" },
        { innerHTML: "$ Dhrua|" },
        { innerHTML: "$ Dhrup|" },
        { innerHTML: "$ DhruX|" },
        { innerHTML: "$ Dhruj|" },
        { innerHTML: "$ Dhruv|" },
        { innerHTML: "$ Dhruvb|" },
        { innerHTML: "$ DhruvF|" },
        { innerHTML: "$ DhruvR|" },
        { innerHTML: "$ Dhruvi|" },
        { innerHTML: "$ Dhruva|" },
        { innerHTML: "$ Dhruvaj|" },
        { innerHTML: "$ Dhruva[|" },
        { innerHTML: "$ Dhruvas|" },
        { innerHTML: "$ DhruvaJ|" },
        { innerHTML: "$ Dhruva |" },
        { innerHTML: "$ Dhruva W|" },
        { innerHTML: "$ Dhruva Y|" },
        { innerHTML: "$ Dhruva Z|" },
        { innerHTML: "$ Dhruva M|" },
        { innerHTML: "$ Dhruva S|" },
        { innerHTML: "$ Dhruva SB|" },
        { innerHTML: "$ Dhruva S_|" },
        { innerHTML: "$ Dhruva Sx|" },
        { innerHTML: "$ Dhruva Sf|" },
        { innerHTML: "$ Dhruva Sa|" },
        { innerHTML: "$ Dhruva SaM|" },
        { innerHTML: "$ Dhruva Say|" },
        { innerHTML: "$ Dhruva Saq|" },
        { innerHTML: "$ Dhruva SaW|" },
        { innerHTML: "$ Dhruva Sam|" },
        { innerHTML: "$ Dhruva SamQ|" },
        { innerHTML: "$ Dhruva Samp|" },
        { innerHTML: "$ Dhruva Samv|" },
        { innerHTML: "$ Dhruva Samu|" },
        { innerHTML: "$ Dhruva Samb|" },
        { innerHTML: "$ Dhruva SambD|" },
        { innerHTML: "$ Dhruva SambZ|" },
        { innerHTML: "$ Dhruva SambN|" },
        { innerHTML: "$ Dhruva SambK|" },
        { innerHTML: "$ Dhruva Sambr|" },
        { innerHTML: "$ Dhruva Sambrl|" },
        { innerHTML: "$ Dhruva SambrY|" },
        { innerHTML: "$ Dhruva Sambrg|" },
        { innerHTML: "$ Dhruva SambrD|" },
        { innerHTML: "$ Dhruva Sambra|" },
        { innerHTML: "$ Dhruva SambraG|" },
        { innerHTML: "$ Dhruva Sambrar|" },
        { innerHTML: "$ Dhruva Sambran|" },
        { innerHTML: "$ Dhruva Sambrat|" },
        { innerHTML: "$ Dhruva Sambran|" },
        { innerHTML: "$ Dhruva Sambran\|" },
        { innerHTML: "$ Dhruva SambranG|" },
        { innerHTML: "$ Dhruva SambranP|" },
        { innerHTML: "$ Dhruva Sambran]|" },
        { innerHTML: "$ Dhruva Sambrani" },
    ],
    duration: 2750,
    easing: 'easeInOutSine',
    update: function (anim) {
        var obj = document.getElementsByClassName('landing-name')[0]
        obj.innerHTML = obj.innerHTML.slice(0, obj.innerHTML.length - 2)
    }
}).play()

pages = document.getElementsByClassName('page')

window.onscroll = function () {
    setSnap('start')
    updateLocation()
}
updateLocation()

function updateLocation() {
    var winHeight = $(window).height();
    var docHeight = $(document).height();
    var max = docHeight - winHeight;
    var value = $(window).scrollTop();
    var angle = value / max * Math.PI / 2
    updateKet(Math.abs(Math.cos(angle)), Math.abs(Math.sin(angle)))
}

function updateKet(v_0, v_1) {
    x = v_0.toFixed(3)
    y = v_1.toFixed(3)
    $('#ket')[0].innerHTML = x + "|0⟩ + " + y + "|1⟩"
}

function setSnap(align_type) {
    for (const key in pages) {
        if (pages.hasOwnProperty(key)) {
            const element = pages[key];
            element.style.scrollSnapAlign = align_type
        }
    }
}

function setDisplay(k, display_type) {
    for (const key in k) {
        if (k.hasOwnProperty(key)) {
            const element = k[key];
            element.style.display = display_type
        }
    }
}

function expand(obj_id) {
    obj = document.getElementById(obj_id)
    var k = document.getElementsByClassName(obj_id)

    if (obj.style.maxHeight != "10000px") {
        setSnap('none')
        setDisplay(k, "block")
        anime({
            targets: k,
            maxHeight: [0, 10000],
            opacity: [0, 1],
            duration: 650,
            easing: 'easeInOutCirc',
            autoplay: false
        }).play()
    } else {
        setSnap('none')
        anime({
            targets: k,
            maxHeight: [10000, 0],
            opacity: [1, 0],
            visibility: ["visible", "collapse"],
            duration: 500,
            easing: 'easeInOutCirc',
            autoplay: false
        }).play()
        setDisplay(k, "none")
    }
}



function caesar(text, shift) {
    return text.replace(/./g, function (a) {
        return String.fromCharCode(a.charCodeAt(0) + shift);
    });
}
function openSite(text, shift) {
    actual = caesar(text, -shift);
    open(actual, "_target");
}

function addToolTip(ele, text, shift) {
    actual = caesar(text, -shift);
    ele.title = actual;
}
function removeToolTip(ele) {
    ele.title = "";
}
