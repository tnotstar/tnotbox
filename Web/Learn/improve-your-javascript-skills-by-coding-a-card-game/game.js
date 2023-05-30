const cardObjectDefinitions = [
    { id: 1, positionClass: 'card-pos-a', imagePath: "images/card-KingHearts.png" },
    { id: 2, positionClass: 'card-pos-b', imagePath: "images/card-JackClubs.png" },
    { id: 3, positionClass: 'card-pos-c', imagePath: "images/card-QueenDiamonds.png" },
    { id: 4, positionClass: 'card-pos-d', imagePath: "images/card-AceSpades.png" },
]

const backCardImagePath = "images/card-back-Blue.png";

function createCard(id, positionClass, imagePath) {
    const cardElement = document.createElement('div');
    const cardInnerElement = document.createElement('div');

    const cardFrontElement = document.createElement('div');
    const cardFromImage = document.createElement('img');

    const cardBackElement = document.createElement('div');
    const cardBackImage = document.createElement('img');


    cardElement.id = id;
    cardElement.classList.add('card');
    cardElement.appendChild(cardInnerElement);

    cardInnerElement.classList.add('card-inner');
    cardInnerElement.appendChild(cardFrontElement);
    cardInnerElement.appendChild(cardBackElement);


    cardFrontElement.classList.add('card-front');
    cardFrontElement.appendChild(cardFromImage);
    
    cardFromImage.src = imagePath;
    cardFromImage.classList.add('card-img');

    cardBackElement.classList.add('card-back');
    cardBackElement.appendChild(cardBackImage);

    cardBackImage.src = backCardImagePath;
    cardBackImage.classList.add('card-img');

    const cardPositioned = document.querySelector(`.${positionClass}`);
    cardPositioned.appendChild(cardElement);

    const cardContainer = document.querySelector('.card-container');
    cardContainer.appendChild(cardPositioned);
}

function createAllCards() {
    cardObjectDefinitions.forEach((card) => {
        createCard(card.id, card.positionClass, card.imagePath);
    })
}

createAllCards();