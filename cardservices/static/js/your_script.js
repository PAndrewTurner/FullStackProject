// Import the functions you need from the SDKs you need
//import { initializeApp } from "firebase/app";
//import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

document.addEventListener('DOMContentLoaded', (event) => {
    const loginButton = document.getElementById('loginButton');
    if (loginButton) {
        loginButton.addEventListener('click', function() {
            // Your login logic here
        });
    } else {
        console.error('Login button element not found!');
    }
});

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
//const firebaseConfig = {
//  apiKey: "AIzaSyCmE7pclF-elhD_BybfUi5rbnoLopaCjos",
//  authDomain: "cardservices-c108a.firebaseapp.com",
//  projectId: "cardservices-c108a",
//  storageBucket: "cardservices-c108a.appspot.com",
//  messagingSenderId: "581581917182",
//  appId: "1:581581917182:web:4341531479eebf480c8eaf",
//  measurementId: "G-4PLDD26ZBG"
//};

// Initialize Firebase
// const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);
