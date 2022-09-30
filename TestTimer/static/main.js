
const testBox = document.getElementById('test-box')
var testtime = 0;
const countdownBox = document.getElementById('countdown-box')
console.log(countdownBox)
const ringer = new Audio('/static/ring.mp3')
var isPaused = false


const startnow = new Date().getTime()

if (testBox != null) {
    testtime = startnow + (testBox.textContent * 60 * 1000);
    //console.log(testtime)
    const stop = false
    var intervalid = setInterval(timerDisplay, 100);
}

function timerDisplay() {

    const now = new Date().getTime()

    var diff = testtime - now

    const h = Math.floor((testtime / (1000 * 60 * 60)) - (now / (1000 * 60 * 60)))
    const m = Math.floor(((testtime / (1000 * 60)) - (now / (1000 * 60))) % 60)
    var s = Math.floor(((testtime / (1000)) - (now / (1000))) % 60)


    //s = 5;
    //x -= 1;
    //diff = x;
    //console.log(diff)
    //console.log(isPaused)

    if (diff > 0 && isPaused == false) {
        countdownBox.innerHTML = h + " : " + m + " : " + s
    }
    else if (diff <= 0 && isPaused == false) {
        countdownBox.innerHTML = "0" + " : " + "0" + " : " + "0"
        ringer.play()
        clearInterval(intervalid)

    }
}

function startTimer() {
    // get selected radio button
    var radId = displayRadioButtonVal()
    // directing to timer page
    window.location.href = "temp/timer".replace("temp", radId);

}

function pauseStart() {
    if (isPaused == false) {
        isPaused = true
    }
    else {
        isPaused = false
    }
}

function displayRadioButtonVal() {
    var ele = document.getElementsByName('section_select');
    for (i = 0; i < ele.length; i++) {
        if (ele[i].checked)
            return ele[i].id
    }


}