import { initializeApp } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js";
// import app from './firebase-init.js';

// Web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCmE7pclF-elhD_BybfUi5rbnoLopaCjos",
    authDomain: "cardservices-c108a.firebaseapp.com",
    projectId: "cardservices-c108a",
    storageBucket: "cardservices-c108a.appspot.com",
    messagingSenderId: "581581917182",
    appId: "1:581581917182:web:4341531479eebf480c8eaf",
    measurementId: "G-4PLDD26ZBG"
  };
  
  // Initialize Firebase
  // firebase.initializeApp(firebaseConfig);
  
  // Check to see if Firebase Analytics is supported in the current environment
  if (firebase.analytics.isSupported()) {
    firebase.analytics();
  }
  
  // Initialize Firebase Authentication UI
  //const ui = new firebaseui.auth.AuthUI(firebase.auth());
  function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
  
    firebase.auth().signInWithEmailAndPassword(email, password)
        .then((userCredential) => {
            // Signed in 
            const user = userCredential.user;

            localStorage.setItem('userName', user.displayName || 'User');
            // Redirect to home page or wherever you want
            window.location.href = '/main/dashboard/';
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            document.getElementById('error-message').innerText = errorMessage;
        });
  
  }
    document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('loginButton').addEventListener('click', login);
    });  
// Function to sign out the user
function signOut() {
    firebase.auth().signOut().then(() => {
        // Sign-out successful.
        window.location.href = '/main/hello/'; // Redirect to the login page after signing out
    }).catch((error) => {
        // An error happened.
        console.error('Sign out error:', error);
    });
}

// Add an event listener to sign out when the "Sign Out" button is clicked
document.getElementById('signOutButton').addEventListener('click', signOut);
  // FirebaseUI config object
  const uiConfig = {
    callbacks: {
      signInSuccessWithAuthResult: function(authResult, redirectUrl) {
        // Redirect to the credit/ page after successful sign-in
        window.location.href = '/main/dashboard/';
        return true; // Prevent the default behavior (redirect to signInSuccessUrl)
      }
    },
    signInFlow: 'popup', // Use popup for sign-in
    signInOptions: [
      firebase.auth.GoogleAuthProvider.PROVIDER_ID,
      firebase.auth.EmailAuthProvider.PROVIDER_ID
    ]
  };
  
  // The start method will wait until the DOM is loaded.
  ui.start('#firebaseui-auth-container', uiConfig);
  