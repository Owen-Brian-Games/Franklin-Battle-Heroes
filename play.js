let attackButton = document.getElementById("attack");
let selector = document.getElementById("attackSelector");
let playerName = document.getElementById("playerName");
let playerHealthDisplay = document.getElementById("playerHealth");
let enemyHealthDisplay = document.getElementById("enemyHealth");
let infoDisplay = document.getElementById("infoDisplay");
let abilityPointsDisplay = document.getElementById("abilityDisplay");
let option1 = document.getElementById("option1");
let option2 = document.getElementById("option2");
let option3 = document.getElementById("option3");

let turnNumber = 0;
let canAttack = true;
let playerHealth = 100;
let abilityCharge = 0;
let enemyHealth = 100;

let waitTime = 2000;

let character;
let attack1;
let attack1f;
let attack2;
let attack2f;
let ability;
let abilityChargeReq;

function setInfoDisplay(text) {
	infoDisplay.textContent = text;
}

function updateStats() {
	playerHealthDisplay.textContent = playerHealth;
	enemyHealthDisplay.textContent = enemyHealth;
	abilityPointsDisplay.textContent = "Ability Points: " + abilityCharge.toString();
}

function getCharacterInfo () {
	character = getSelectedChar();
	console.log("Selected: " + character)
	if (character == "Franklin") {
		attack1 = 25;
		attack1f = 0.25;
		attack2 = 15;
		attack2f = 0;
		ability = 100;
		abilityChargeReq = 3;
		option1.textContent = "1: 25 Damage - 25% Failure";
		option2.textContent = "2: 15 Damage - 0% Failure";
		option3.textContent = "Ability: 100 Damage - 3 Points Req."
	} else {
		console.log("Invalid Character Name");
	}

}

function calculateFailure(chanceDecimal) {
	chanceDecimal = 1 / chanceDecimal
	let output = Math.floor(Math.random() * chanceDecimal * 10);
	if (output <= 10) {
		return false;
	} else {
		return true;
	}
}

function enemyAttack () {
	if (turnNumber == 4) {
		if (calculateFailure(0.5)) {
			playerHealth -= 80;
			setInfoDisplay("Enemy used Ability!")
			setTimeout(setInfoDisplay, waitTime, "Player's Turn")
		} else {
			setInfoDisplay("Enemy Missed!")
			setTimeout(setInfoDisplay, waitTime, "Player's Turn")
		}
	} else {
		if (calculateFailure(0.33)) {
			playerHealth -= 20;
			setInfoDisplay("Enemy Attacked!")
			setTimeout(setInfoDisplay, waitTime, "Player's Turn")
		} else {
			setInfoDisplay("Enemy Missed!")
			setTimeout(setInfoDisplay, waitTime, "Player's Turn")
		}
	}

	canAttack = true;
	updateStats();

}

attackButton.onclick = function () {
	if (canAttack) {
		turnNumber += 1;
		let selectorValue = selector.value;
		if (selectorValue == "1") {
			if (calculateFailure(attack1f)) {
				enemyHealth -= attack1;
				setInfoDisplay("Player Attacked!");
			} else {
				setInfoDisplay("Player Missed!");
			}
			abilityCharge += 1;
		} else if (selectorValue == "2") {
			if (calculateFailure(attack2f)) {
				enemyHealth -= attack2;
				setInfoDisplay("Player Attacked!");
			} else {
				setInfoDisplay("Player Missed!");
			}
			abilityCharge += 1;

		} else if (selectorValue == "ability") {
			if (abilityCharge >= abilityChargeReq) {
				setInfoDisplay("Player used ability!")
				enemyHealth -= ability;
				abilityCharge = 0;
			} else {
				setInfoDisplay("Not Enough Points, Miss!");
			}
		} else {
			console.log("Invalid Selection");
		}
		canAttack = false;
		updateStats();
		setTimeout(enemyAttack, waitTime);
	}
}

getCharacterInfo();
playerName.textContent = character;
setInfoDisplay("Player's Turn");
updateStats();