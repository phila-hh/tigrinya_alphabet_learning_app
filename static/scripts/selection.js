// JavaScript file for handling character selection and form submission

function toggleSelection(element, character) {
    // Function to toggle selection of a character
    var hiddenInput = element.querySelector('input[type="hidden"]');
    if (hiddenInput.value === "0") {
        hiddenInput.value = "1";  // Set value to 1 if not selected
        element.classList.add('selected');  // Add 'selected' class to visually indicate selection
    } else {
        hiddenInput.value = "0";  // Set value to 0 if already selected
        element.classList.remove('selected');  // Remove 'selected' class
    }
}

function submitForm() {
    // Function to submit the form
    document.getElementById("selectionForm").submit();  // Submit the form
}

function clearSelectionAndSubmit() {
    // Function to clear all selected charactersvfrom the form and submit it
    var selectedBoxes = document.querySelectorAll('.quiz-box.selected');
    selectedBoxes.forEach(function(box) {
        var hiddenInput = box.querySelector('input[type="hidden"]');
        hiddenInput.value = "0";  // Reset value to 0
        box.classList.remove('selected');  // Remove 'selected' class
    });
    submitForm();  // Submit the form after clearing selections
}

function playAudio(audioPath) {
    // Function to play audio
    var audio = new Audio(audioPath);
    audio.play();
}
