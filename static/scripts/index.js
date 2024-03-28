document.addEventListener('DOMContentLoaded', (event) => {
    const characters = ['ሀ','ለ','ሐ','መ','ረ','ሰ','ሸ','ቀ',
                        'ቐ','በ','ተ','ቸ','ነ','ኘ','አ','ከ',
                        'ኸ','ወ','ዐ','ዘ','ዠ','የ','ደ','ጀ',
                        'ገ','ጠ','ጨ','ጰ','ፀ','ፈ','ፐ','ቨ']
    const body = document.body;
    
    function createCharacterElement(character) {
        const element = document.createElement('div');
        element.textContent = character;
        element.style.position = 'absolute';
        element.style.left = Math.random() * window.innerWidth + 'px';
        element.style.top = Math.random() * window.innerHeight + 'px';
        element.style.fontSize = '1em';
        element.style.color = 'rgba(49, 255, 255, 0.8)';
        element.style.pointerEvents = 'none';
        return element;
    }
    
    function animateCharacter(element) {
        const speed = Math.random() + 0.5;
        const direction = Math.random() > 0.5 ? 1 : -1;
        const moveCharacter = () => {
            let top = parseFloat(element.style.top);
            top += speed * direction;
            if (top < 0 || top > window.innerHeight) {
                element.style.top = Math.random() * window.innerHeight + 'px';
            } else {
                element.style.top = top + 'px';
            }
            requestAnimationFrame(moveCharacter);
        };
        requestAnimationFrame(moveCharacter);
    }
    
    characters.forEach((character) => {
        const element = createCharacterElement(character);
        body.appendChild(element);
        animateCharacter(element);
    });
});
