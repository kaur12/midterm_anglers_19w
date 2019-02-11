// JavaScript Document

(function() {
	console.log("Javascript is linked up");

	var button = document.querySelector("#button");
	var burgerCon = document.querySelector("#contactForm")

	function popUpForm() {
		console.log("button clicked");
		// add class or toggle to button and burgercon
		contactForm.classList.toggle("slideToggle");
		button.classList.toggle("expanded");
	}

	button.addEventListener("click", popUpForm);

	var story = "this is a story about Ray's dog";

	var secondary = 'this has "double" qoutes inside';

})();

