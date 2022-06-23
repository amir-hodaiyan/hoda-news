let ts = document.getElementById('Clock').innerText.split(':')
let hour = parseInt(ts[0]);
let min = parseInt(ts[1]);
let sec = parseInt(ts[2]);

function timer() {
    if (sec < 59) {
        sec += 1;
    } else {
        sec = 0
        if (min < 59) {
            min += 1;
        } else {
            min = 0;
            if (hour < 23) {
                hour += 1;
            } else {
                hour = 0
            }
        }
    }
}

function showTime() {
    let h = hour;
    let m = min;
    let s = sec;

    (s < 10) ? s = '0' + s : s;
    (m < 10) ? m = '0' + m : m;
    (h < 10) ? h = '0' + h : h;

    document.getElementById('Clock').innerHTML = h + ":" + m + ":" + s
    timer();
    setTimeout(showTime, 1000);
}

showTime();