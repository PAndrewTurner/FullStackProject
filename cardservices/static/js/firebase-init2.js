import { initializeApp } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js";

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

// Initialize Firebase Authentication UI
//const ui = new firebaseui.auth.AuthUI(firebase.auth());

// Initialize Firebase Analytics if supported
if (firebase.analytics && firebase.analytics.isSupported()) {
    firebase.analytics();
}

// FirebaseUI config object
const uiConfig = {
    callbacks: {
      signInSuccessWithAuthResult: function(authResult, redirectUrl) {
        return true;
    },
    
    uiShown: function() {
        // The widget is rendered.
        // Hide the loader.
        //document.getElementById('loader').style.display = 'none';
      }

    },
    // Will use popup for IDP Providers sign-in flow instead of the default, redirect.

    signInFlow: 'popup',
    signInSuccessUrl: '/main/credit/',
    signInOptions: [
      // List of OAuth providers supported.
      firebase.auth.GoogleAuthProvider.PROVIDER_ID,
      //firebase.auth.FacebookAuthProvider.PROVIDER_ID,
      //firebase.auth.TwitterAuthProvider.PROVIDER_ID,
      //firebase.auth.GithubAuthProvider.PROVIDER_ID,
      firebase.auth.EmailAuthProvider.PROVIDER_ID,
      //firebase.auth.PhoneAuthProvider.PROVIDER_ID,
      //firebaseui.auth.AnonymousAuthProvider.PROVIDER_ID
    ],
    // Terms of service url.
    //tosUrl: '<your-tos-url>',
    // Privacy policy url.
    //privacyPolicyUrl: '<your-privacy-policy-url>'
  };
  firebase.auth().onAuthStateChanged((user) => {
    if (!user) {
      // User is signed in, you can handle redirection here if needed
      window.location.href = '/main/credit/'; // Redirect to the intended page
    }
  });
  
// Initialize Firebase
// firebase.initializeApp(firebaseConfig);
// Login function

function login() {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  firebase.auth().signInWithEmailAndPassword(email, password)
      .then((userCredential) => {
          // Signed in 
          const user = userCredential.user;
          // Redirect to home page or wherever you want
          window.location.href = '/main/credit/';
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
    // Redirect to the login page after signing out
    window.location.href = '/main/hello/'; // Adjust the URL to your login page
  }).catch((error) => {
    // An error happened.
    console.error('Sign out error:', error);
  });
};
  // Add an event listener to sign out when the browser window is closed
  window.addEventListener('beforeunload', signOut);
  // The start method will wait until the DOM is loaded.
  ui.start('#firebaseui-auth-container', uiConfig);
  



