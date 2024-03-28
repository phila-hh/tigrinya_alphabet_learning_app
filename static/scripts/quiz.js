// JavaScript file for checking answers on thecquiz

function checkAnswers() {
    // Get all answer fields
    var answerFields = document.querySelectorAll('.answer-field');

    // Iterate through each answer field
    answerFields.forEach(function(field) {
        var userInput = field.value.trim().toLowerCase();  // Get user input (case insensitive)
        var correctValue = field.dataset.correct.trim().toLowerCase();  // Get correct value (case insensitive)
        var parentBox = field.parentElement;

        // Compare user input with correct value
        if (userInput === correctValue) {
            parentBox.classList.remove('incorrect');
            parentBox.classList.add('correct');
        } else {
            parentBox.classList.remove('correct');
            parentBox.classList.add('incorrect');
        }
    });
}
