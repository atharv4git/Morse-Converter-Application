// Read Morse code using Web Audio API
function readMorse() {
    var morseCode = document.getElementsByName("morse-code")[0].value;
    var dotDuration = 100; // in milliseconds
    var dashDuration = 3 * dotDuration; // in milliseconds
    var pauseDuration = dotDuration; // in milliseconds

    var audioContext = new AudioContext();
    var oscillator = audioContext.createOscillator();
    oscillator.type = "sine";
    oscillator.connect(audioContext.destination);

    for (var i = 0; i < morseCode.length; i++) {
        var char = morseCode.charAt(i);
        if (char == ".") {
            oscillator.frequency.setValueAtTime(800, audioContext.currentTime);
            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + (dotDuration / 1000));
        } else if (char == "-") {
            oscillator.frequency.setValueAtTime(800, audioContext.currentTime);
            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + (dashDuration / 1000));
        }
        if (i != morseCode.length - 1) {
            // add pause between characters
            oscillator.frequency.setValueAtTime(0, audioContext.currentTime + (pauseDuration / 1000));
            oscillator.start(audioContext.currentTime + (pauseDuration / 1000));
            oscillator.stop(audioContext.currentTime + (pauseDuration / 1000) + 0.01);
        }
    }
}

// Read text using Web Speech API
function readText() {
    var text = document.getElementsByName("text")[0].value;
    var speechSynthesis = window.speechSynthesis;
    var utterance = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(utterance);
}
